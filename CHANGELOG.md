# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0]

First public release: the finished single-agent game, its trained policy, and
the evidence chain that backs the result.

### The result

- Recurrent 384-unit policy evaluated once over 3,000 held-out contracts —
  99.8 / 100.0 / 96.4 / 98.0 / 99.0 / **89.6%** across the six tiers.
- Evaluation consumed a one-way final-test slice. The ledger records the
  consumed slice alongside six retired ones, including three failed teacher
  audits.

### Game

- Six procedurally generated contract tiers with cameras, patrolling guards and
  late-tier response drones, over a deterministic 60 Hz simulation.
- Keyboard, cursor and touch play; Agent Lab for watching the trained policy on
  any seed.
- Static browser build: the simulation runs in WebAssembly through Pygbag, with
  ONNX Runtime Web loaded lazily and only on agent takeover.
- Windows player executable that excludes the training stack.

### Benchmark

- `GhostlineEnv-v1`, a Gymnasium environment with `Discrete(36)` and a
  structured player-equivalent observation.
- Frozen mechanics bound to environment fingerprint `521c449a…e129`; loading a
  checkpoint against a different fingerprint fails closed.
- `verify_release_evidence.py` recomputes every published aggregate from the raw
  episode records rather than comparing checksums.

### Published negative results

- Dynamic INT8 export was 28% smaller and produced 5 action mismatches in 1,000
  recurrent transitions. Rejected; FP32 ships.
- A PPO pilot scored a worst-tier 84% against the matched rollback's 90%.
  Rejected and not resumed.

### Known limitations

Median maximum trace saturates at 100.0 on tiers 3, 4 and 6 — the policy solves
contracts without playing quietly. Path efficiency is 0.58–0.79. No superhuman
claim is made; that requires a matched-seed human cohort which has not been
collected. See [known limitations](wiki/training.md#known-limitations).
