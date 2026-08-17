---
title: Ghostline Implementation
updated: 2026-07-29
status: active
---

# Architecture

Ghostline registers two Gymnasium environments:

- `GhostlineEnv-v1` is the released game and policy benchmark.
- `GhostlineLegacyEnv-v0` is a compatibility-only predecessor, kept so old
  scripts keep running.

The released artifacts record their observation contract as `GhostlineEnv-v2`.
That is a historical internal label from when the evidence was frozen, and it
names the same environment. `env_v1.py` is a zero-mechanics wrapper that gives
the released environment its stable public name without touching the
fingerprinted bytes; it reports both, as `contract` and
`historical_internal_contract`. Rewriting the label inside a signed artifact
would invalidate the hash chain that authenticates it.

## Layer boundaries

- `simulation.py`, `generation.py`, `types.py` and `config.py` are the frozen
  simulation and facility contract. They are hashed together into the
  environment fingerprint
  `521c449a8bd9a540977a918f5b094dd3aeff44cc579a55f75e22a74bab20e129`,
  so any edit to them invalidates every checkpoint and every benchmark record.
- `env.py` is the Gymnasium adapter; `env_v1.py` is the public-name wrapper.
- `model.py` owns the recurrent policy. `imitation.py`, `torchrl_train.py` and
  `evaluation.py` own learning and measurement.
- `presentation.py`, `app.py` and `audio.py` consume simulation state and event
  streams. Pygame never enters a simulation or generation import, which a
  regression enforces across all sixteen training-path modules.
- Human, scripted and neural controllers emit the same semantic actions.

Simulation runs at 60 Hz. Policies decide at 10 Hz through six-tick action
repeat. A replay is deterministic from contract, tier, seed and action sequence.

## Public contract

`GhostlineEnv-v1` exposes `Discrete(36)`:

`9 movement x 2 dash x 2 pulse`

The observation is a dictionary of ego, objective, local-grid, terminal,
security-entity, ray and action-mask records. Everything in it is also readable
by a human from the HUD, the minimap or facility telemetry — the actor and the
critic receive no hidden live enemy coordinates. That constraint is what makes
the human and policy results comparable at all.

## Procedural generation

`LevelGenerator` builds a furnished facility from a seed and a tier, then
validates it before the simulation will accept it: reachable quota and
extraction, a safe spawn, valid patrol routes, and route loops so no contract
depends on a single corridor. A seed that fails validation is rejected rather
than repaired.

The release gate is a 10,000-seed audit through
`scripts/fuzz_ghostline_levels.py`, which must report zero invalid levels.

## Policy

The shipped policy is a recurrent actor-critic:

- a convolutional encoder over the local grid;
- masked attention pooling over terminals and perceived security entities;
- MLP encoders for ego, objective and rays;
- a 384-unit GRU;
- separate policy and value decoders;
- goal-bearing and visible-danger auxiliary heads;
- exact action masking before sampling or argmax.

The checkpoint stores its observation contract, action count, recurrent width
and a normalized source fingerprint. Loading fails closed on any mismatch, so a
checkpoint cannot be silently paired with an environment it was not trained on.

## Presentation contract

The renderer presents a 640x360 world with native-resolution UI, integer
desktop scaling, smooth physical cones, eight-direction locomotion, persistent
security readability, a compact HUD, a minimap, captions and touch controls.

### Frame budget

The browser build interprets Python, so frame cost is dominated by the number of
Python-level draw calls rather than by pixels. Two caches keep that count low:

- **Terrain** is painted once per level into a floor surface and a wall surface
  and then blitted. The simulation never writes to the level grid, so terrain is
  a pure function of grid, room roles and seed. Tile coordinates are exact
  multiples of the tile size and adding an integer commutes with rounding, so the
  blit lands on the same pixels the per-tile path produced. Floor and walls stay
  separate surfaces because vision cones composite between them, and the wall
  layer carries per-pixel alpha so it cannot erase a cone.
- **Vision-cone fans** are memoised by quantised observer pose. The cast depends
  only on static geometry, so a guard that holds, aims or waits re-uses its rays
  while screen projection still runs every frame. The cache is bounded and
  cleared wholesale rather than tracking recency.

Both invalidate on `(seed, tier, level identity)`. A cached frame is
pixel-identical to one drawn with a cold cache; cone-pose quantisation is the
only approximation and is bounded by regression at well under 0.5% of pixels.
Isolated gameplay draw cost on the reference desktop is 2.14 ms per frame
against a 16.67 ms budget, measured across tiers 1, 3, 4 and 6.

## Verification gates

- Gymnasium API checker, observation bounds and action masks.
- Deterministic replay, collision, line-of-sight and cone parity, trace, damage,
  guard orders, reward sums and termination.
- 10,000 generated facilities with zero validation failures.
- Headless throughput against an explicit floor.
- Held-out evaluation from a seed namespace disjoint from training and
  validation.
- PyTorch/ONNX deterministic action parity over at least 1,000 recurrent
  transitions.
- Browser and Vercel QA in Chrome only.
