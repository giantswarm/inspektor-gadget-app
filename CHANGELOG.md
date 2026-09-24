# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- changed: `app.giantswarm.io` label group was changed to `application.giantswarm.io`
- fixed: the `helm.sh/chart` label is valid for any chart version; the 63-character cut of a long version no longer ends in `.`, `_` or `-`, which made the API server refuse every labelled object
- fixed: `Chart.yaml` carries the `io.giantswarm.application.team: planeteers` annotation that app-build-suite and the repository tooling read
- fixed: every object of the published chart carries `application.giantswarm.io/team: "planeteers"` instead of an empty value; the label reads the `io.giantswarm.application.team` annotation, the only team annotation app-build-suite keeps in the packaged `Chart.yaml`, and the redundant `application.giantswarm.io/team` annotation is gone

[Unreleased]: https://github.com/giantswarm/inspektor-gadget-app/tree/main
