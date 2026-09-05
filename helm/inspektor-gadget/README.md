# inspektor-gadget

Please add description

**Homepage:** <https://github.com/giantswarm/inspektor-gadget-app>

## Source Code

* <https://github.com/some-org/some-repo>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| config.hookMode | string | `"auto"` | How to get containers start/stop notifications (auto, crio, podinformer, nri, fanotify+ebpf) |
| config.fallbackPodInformer | bool | `true` | Whether to use the fallback pod informer |
| config.containerdSocketPath | string | `"/run/containerd/containerd.sock"` | Containerd CRI Unix socket path |
| config.crioSocketPath | string | `"/run/crio/crio.sock"` | CRI-O CRI Unix socket path |
| config.dockerSocketPath | string | `"/run/docker.sock"` | Docker Engine API Unix socket path |
| config.podmanSocketPath | string | `"/run/podman/podman.sock"` | Podman API Unix socket path |
| config.experimental | bool | `false` | Enable experimental features |
| config.eventsBufferLength | string | `"16384"` | Events buffer length. A low value could impact horizontal scaling. |
| config.daemonLogLevel | string | `"info"` | Daemon log level. Valid values are: "trace", "debug", "info", "warning", "error", "fatal", "panic" |
| config.verifyGadgets | bool | `true` | Verify image-based gadgets |
| config.gadgetsPublicKeys | list | `["-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEoDOC0gYSxZTopenGmX3ZFvQ1DSfh\nIr4EKRt5jC+mXaJ7c7J+oREskYMn/SfZdRHNSOjLTZUMDm60zpXGhkFecg==\n-----END PUBLIC KEY-----\n"]` | Public keys used to verify image-based gadgets |
| config.allowedGadgets | list | `[]` | List of allowed gadgets |
| config.disallowGadgetsPulling | bool | `false` | Disallow pulling gadgets |
| config.mountPullSecret | bool | `false` | Mount pull secret (gadget-pull-secret) to pull image-based gadgets from a private registry |
| config.appArmorProfile | string | `"unconfined"` | AppArmor profile for the gadget container |
| config.otelMetricsListen | bool | `false` | Enable the OpenTelemetry metrics listener |
| config.otelMetricsAddress | string | `"0.0.0.0:2224"` | Address to listen on for OpenTelemetry metrics |
| image.repository | string | `"ghcr.io/inspektor-gadget/inspektor-gadget"` | Container image repository. Upstream's image; there is no gsoci mirror yet. |
| image.pullPolicy | string | `"IfNotPresent"` | Pull policy for the container image |
| image.tag | string | `""` | Tag for the container image; empty means the chart's appVersion |
| nodeSelector | object | `{"kubernetes.io/os":"linux"}` | Node selector for the gadget DaemonSet |
| affinity | object | `{}` | Affinity for the gadget DaemonSet |
| capabilities | object | `{}` | Capabilities for the gadget container; empty means the upstream default set |
| tolerations | list | `[]` | Extra tolerations for the gadget DaemonSet |
| skipLabels | bool | `false` | Skip the Helm labels (upstream default is true; Giant Swarm charts carry the team label) |
| additionalLabels | object | `{"enabled":false,"labels":{}}` | Labels added to all resources when `enabled` is true |
