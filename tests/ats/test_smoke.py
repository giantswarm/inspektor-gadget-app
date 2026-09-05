"""app-test-suite smoke for the inspektor-gadget chart.

app-test-suite 1.x (the generated execute-chart-tests CircleCI job) creates a kind
cluster, installs the packaged chart with `helm upgrade --install --wait` (namespace and
values file: .ats/main.yaml) and then runs `pytest -m smoke` in this directory. The smoke
proves that the chart installs on a bare cluster and that the gadget DaemonSet runs on
every node.
"""

import logging
import os
from typing import List

import pykube
import pytest
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.k8s.daemon_set import wait_for_daemon_sets_to_run

logger = logging.getLogger(__name__)

# app-test-suite exports the release namespace (app-tests-deploy-namespace in .ats/main.yaml).
namespace = os.environ.get("ATS_RELEASE_NAMESPACE", "gadget")
daemon_sets = ["gadget"]
timeout = 180


@pytest.mark.smoke
def test_api_working(kube_cluster: Cluster) -> None:
    """The test cluster is reachable."""
    assert kube_cluster.kube_client is not None
    assert len(pykube.Node.objects(kube_cluster.kube_client)) >= 1


@pytest.mark.smoke
@pytest.mark.flaky(reruns=1, reruns_delay=15)
def test_daemon_sets_ready(kube_cluster: Cluster) -> None:
    """The gadget DaemonSet has a ready pod on every scheduled node."""
    ready: List[pykube.DaemonSet] = wait_for_daemon_sets_to_run(
        kube_cluster.kube_client, daemon_sets, namespace, timeout
    )
    assert len(ready) == len(daemon_sets)
    for ds in ready:
        status = ds.obj["status"]
        wanted = int(status.get("desiredNumberScheduled", 0))
        got = int(status.get("numberReady", 0))
        assert wanted >= 1, f"{namespace}/{ds.name}: no node scheduled"
        assert got == wanted, f"{namespace}/{ds.name}: {got}/{wanted} pods ready"
        logger.info("DaemonSet %s/%s ready on %d node(s)", namespace, ds.name, got)
