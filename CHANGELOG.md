# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.13] - 2026-09-24

- fixed: `Chart.yaml` carries the `io.giantswarm.application.team: planeteers` annotation that app-build-suite and the repository tooling read
- fixed: every object of the published chart carries `application.giantswarm.io/team: "planeteers"` instead of an empty value; the label reads the `io.giantswarm.application.team` annotation, the only team annotation app-build-suite keeps in the packaged `Chart.yaml`, and the redundant `application.giantswarm.io/team` annotation is gone

## [0.1.11] - 2026-09-24

- fixed: the `helm.sh/chart` label is valid for any chart version; the 63-character cut of a long version no longer ends in `.`, `_` or `-`, which made the API server refuse every labelled object

## [0.1.0] - 2026-06-26

- changed: `app.giantswarm.io` label group was changed to `application.giantswarm.io`

[Unreleased]: https://github.com/giantswarm/inspektor-gadget-app/compare/v0.1.13...HEAD
[0.1.13]: https://github.com/giantswarm/inspektor-gadget-app/compare/v0.1.11...v0.1.13
[0.1.11]: https://github.com/giantswarm/inspektor-gadget-app/compare/v0.1.0...v0.1.11
[0.1.0]: https://github.com/giantswarm/inspektor-gadget-app/releases/tag/v0.1.0
