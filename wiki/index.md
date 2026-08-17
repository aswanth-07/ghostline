---
title: Ghostline Wiki
updated: 2026-07-29
status: active
---

# Ghostline

Ghostline is a procedural stealth-infiltration game and reinforcement-learning
benchmark with a deterministic 60 Hz simulation, validated furnished facilities,
a scrolling pixel-art presentation, six contract tiers, and a player-equivalent
recurrent policy.

Human play and policy control run the same simulation, read the same structured
observation, and choose from the same 36 semantic actions. Nothing the policy
sees is hidden from a player.

## Frozen product decisions

- Quota-based data theft followed by extraction.
- Three integrity points, tier-scaled mission clock, escalating recoverable
  trace, dash, and disruption pulse.
- Cameras, human guards, and late-tier response drones; no player weapon combat.
- Keyboard, cursor and touch play, plus Agent Lab and a static Chrome-first web
  showcase; no gamepad and no multiplayer scope.
- Player-equivalent structured observations; no renderer-only or hidden live
  enemy state.
- The published policy is trained by fair-teacher behavior cloning, four DAgger
  recovery rounds, and low-rate consolidation. PPO, GAE and RND are implemented
  and tested, but the released checkpoint claims no PPO improvement: the pilot
  was measured, rejected, and is published as
  `benchmarks/neural/ppo-pilot-rejected.json`.

## A note on the contract name

Every immutable artifact — the checkpoint, the ONNX graph, the 3,000-episode
audit — records its observation contract as `GhostlineEnv-v2`. The public
environment id is `GhostlineEnv-v1`. Both refer to the same released game.

The label is historical. Those artifacts are bound to content hashes, so
rewriting the string inside them would invalidate the evidence it is meant to
authenticate. `env_v1.py` gives the exact released environment its stable public
name without touching the fingerprinted bytes, and reports the old label as
`historical_internal_contract`.

## Pages

- `implementation.md`: simulation, generator, presentation, and the public
  contract.
- `training.md`: teacher, imitation lineage, seed namespaces, and evaluation.
- `setup.md`: install, play, verify, train, record, and package.
- `assets.md`: visual and audio workflow, with authorship disclosure.
- `web-deployment.md`: static Pygbag/ONNX Runtime Web architecture, build,
  Chrome QA, and Vercel release.
