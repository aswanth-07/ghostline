# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Put the game, mission objectives, controls, and six named levels first in the
  README and browser onboarding; refresh the animated gameplay preview.
- Add `--level`, `--levels`, `--episodes-per-level`, and
  `--initial-curriculum-level` CLI names, retaining historical aliases and
  serialized fields for compatibility.
- Label native Agent Lab history as recent runs, since its entries are not
  necessarily from the same map seed.
- Correct training examples and document all six fingerprinted source modules.

### Fixed

- Preserve asset-consumer errors while falling back cleanly when package resources
  are unavailable.
- Remove the model loader's circular dependency on imitation training code.

### Removed

- Hosted CI and automated release workflows; verification and packaging run locally.

- Retired `neon_arena` prototype and its exclusive test suites. The active
  Ghostline game and compatibility environment remain supported; the prototype
  remains available in Git history.
- Redundant placeholder files in populated asset and benchmark directories.

## [1.0.0]

First public release: the finished single-agent game, its trained policy, and
the evidence chain that backs the result.

### The result

- Recurrent 384-unit policy evaluated once over 3,000 held-out contracts —
  99.8 / 100.0 / 96.4 / 98.0 / 99.0 / **89.6%** across the six levels.
- Evaluation consumed a one-way final-test slice. The ledger records the
  consumed slice alongside six retired ones, including three failed teacher
  audits.

### Game

- Six procedurally generated contract levels with cameras, patrolling guards and
  late-level response drones, over a deterministic 60 Hz simulation.
- Keyboard, cursor and touch play; Agent Lab for watching the trained policy on
  any seed.
- Static browser build: the simulation runs in WebAssembly through Pygbag, with
  ONNX Runtime Web loaded lazily and only on agent takeover.
- Windows player executable that excludes the training stack.

### Benchmark

- `GhostlineEnv-v1`, a Gymnasium environment with `Discrete(36)` and a
  structured player-equivalent observation.
- The install surface contains only the finished single-agent game, training
  and deployment dependencies; the separate research track does not leak into
  this release through an optional extra or transitive package.
- Frozen mechanics bound to environment fingerprint `521c449a…e129`; loading a
  checkpoint against a different fingerprint fails closed.
- `verify_release_evidence.py` recomputes every published aggregate from the raw
  episode records rather than comparing checksums.

### Published negative results

- Dynamic INT8 export was 28% smaller and produced 5 action mismatches in 1,000
  recurrent transitions. Rejected; FP32 ships.
- A PPO pilot scored a worst-level 84% against the matched rollback's 90%.
  Rejected and not resumed.

### Known limitations

Median maximum trace saturates at 100.0 on levels 3, 4 and 6 — the policy solves
contracts without playing quietly. Path efficiency is 0.58–0.79. No superhuman
claim is made; that requires a matched-seed human cohort which has not been
collected. See [known limitations](wiki/training.md#known-limitations).
