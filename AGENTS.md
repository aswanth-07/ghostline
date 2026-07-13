# Ghostline Agent Instructions

These instructions apply to the Ghostline project.

## Product Direction

- Build a polished top-down three-quarter pixel-art stealth game and rigorous procedural-RL benchmark.
- Keep human play and policy control on the same deterministic simulation rules.
- Preserve keyboard play, Agent Lab, headless training, held-out evaluation, and Windows packaging.
- Do not add player weapon combat, multiplayer, or hidden privileged policy state.
- Keep the approved browser release static and player-equivalent: Pygbag simulation,
  lazy ONNX Runtime Web inference, Chrome-only QA, and a human-play fallback.

## Architecture

- Keep deterministic rules in `ghostline/simulation.py` and procedural content in `ghostline/generation.py`.
- Keep Pygame and audio out of simulation and generation imports.
- Keep reward construction in the Gymnasium wrapper rather than the game simulation.
- Treat `GhostlineEnv-v2`, `Discrete(36)`, and the structured observation dictionary as versioned public contracts.
- Keep `GhostlineEnv-v1` only as a documented compatibility baseline.
- Keep `neon_arena` as legacy reference code; do not extend it with Ghostline behavior.
- Update `wiki/` whenever durable mechanics, observations, actions, reward, training, setup, or asset decisions change.

## Verification

- Run `python -m pytest -q`.
- Run the 10,000-seed generator fuzz test for procedural changes.
- Run a headless performance benchmark and APPO smoke test for simulation/training changes.
- Launch `ghostline play` and verify human control before completion.
- Render and inspect representative title, gameplay, security, pause, and debrief states for presentation changes.
