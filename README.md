# Ghostline

**Steal the data. Outsmart security. Make your escape.**

Ghostline is a single-player, pixel-art stealth game set in procedurally generated
facilities. Slip past cameras, evade patrols, and download enough data to open
an extraction route. Every mission is a race between your next move, the clock,
and a rising trace signal.

[**Play in your browser**](https://ghostline-rho.vercel.app) ·
[How to play](#how-to-play) · [The six levels](#six-levels-of-escalating-security) ·
[Run locally](#play-locally) · [Under the hood](#under-the-hood)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12–3.14-blue.svg)](pyproject.toml)

[![Ghostline gameplay: the trained runner steals data and escapes a Level 6 facility](assets/screenshots/ghostline-demo.gif)](videos/ghostline-demo.mp4)

*Gameplay from Level 6 — Ghostline, played by the trained AI runner.
[Watch the full recording](videos/ghostline-demo.mp4) or
[view a still frame](assets/screenshots/gameplay-stealth-v3.png).*

## How to play

1. **Infiltrate.** Explore the facility and locate the amber data terminals.
2. **Download.** Stand near a terminal to hack it automatically. Collect the
   mission's data quota; extra data is a score opportunity if you can afford the risk.
3. **Evade.** Break line of sight to cool your trace. Dash out of danger, or use
   a limited disruption pulse to disable electronics and jam guard radios.
4. **Extract.** Once you have enough data, reach the green extraction relay
   before the timer expires or your integrity runs out.

| Control | Action |
|---|---|
| `WASD` | Move |
| `Shift` | Dash — fast, noisy, and limited by energy |
| `Space` | Disruption pulse — available from Level 2 |
| `Esc` | Pause |

Touch play provides an on-screen stick and dash, pulse, and pause buttons.
The local player also offers remappable controls, contrast options, reduced
motion, sound captions, and an optional timer assist.

Want to study another route? Open **Agent Lab** locally or select
**Agent Takeover** in the browser. The trained runner uses the same game rules
and player-visible information. You can take control again from the browser toolbar.

## Six levels of escalating security

Each level introduces a harder mission. A **level** sets the security and quota;
a **map seed** identifies a particular facility layout. Replay a seed to practice
its route, or leave the browser seed blank for a fresh mission.

| Level | Mission | What you face | Data quota | Time limit |
|---|---|---|---:|---:|
| **1** | **Orientation** | Learn to download and extract, with no cameras or guards | 3 | 1:55 |
| **2** | **Surveillance** | Sweeping cameras and your first disruption pulse | 4 | 2:15 |
| **3** | **Patrol** | Guards that investigate noise and share alerts | 5 | 2:40 |
| **4** | **Countermeasure** | A larger facility, more cameras, and more pulse charges | 6 | 3:00 |
| **5** | **Lockdown** | Response drones deploy when trace reaches its maximum | 7 | 3:25 |
| **6** | **Ghostline** | Dense security and drones that deploy at a lower trace threshold | 8 | 3:45 |

In the local game's **Play Levels** menu, a successful escape unlocks the next
level. The browser mission selector and Agent Lab let you explore all six.
These are replayable procedural missions, rather than six fixed maps.

## Play locally

Requires Python **3.12–3.14**. Run these commands from the cloned repository:

```bash
git clone https://github.com/aswanth-07/ghostline.git
cd ghostline
python -m venv .venv
```

Activate the environment with `source .venv/bin/activate` on macOS/Linux, or
`.\.venv\Scripts\Activate.ps1` in Windows PowerShell, then install and play:

```bash
python -m pip install --constraint requirements.lock -e .
ghostline play
```

To watch the bundled neural policy on the gameplay video's exact map:

```bash
python -m pip install --constraint requirements.lock -e ".[agent]"
ghostline lab --level 6 --seed 2000000
```

Use `ghostline play --level 1 --seed 42` to practice a repeatable mission.
See [setup and packaging](wiki/setup.md) for recording, training, and Windows builds.

## Under the hood

Ghostline is also a reinforcement-learning benchmark. Human input and policy
actions drive the same deterministic **60 Hz simulation**. The policy chooses
at **10 Hz** from **36 semantic actions**: nine movement choices, dash on/off,
and pulse on/off. It receives structured versions of the information available
through the player's HUD, minimap, and facility telemetry.

| Layer | Responsibility |
|---|---|
| [Simulation](src/ghostline/simulation.py) and [generation](src/ghostline/generation.py) | Game rules, seeded facilities, collision, security, and extraction |
| [Environment](src/ghostline/env_v1.py) | Public `GhostlineEnv-v1` Gymnasium interface |
| [Model](src/ghostline/model.py) | Local-grid convolution, masked entity attention, and a 384-unit recurrent GRU |
| [Presentation](src/ghostline/presentation.py) and [app](src/ghostline/app.py) | Pixel-art rendering, controls, progression, menus, and Agent Lab |
| [Browser player](web/) | Pygbag/WebAssembly simulation with lazy ONNX Runtime Web inference |
| [Benchmarks](benchmarks/) | Episode records, training lineage, export parity, and the final-test ledger |

### Design decisions

- **One simulation for play and learning.** Rendering stays outside the rules
  engine, allowing headless training without a second implementation of the game.
- **Player-equivalent observations.** The policy gets no privileged live enemy
  coordinates. This constrains the agent and makes matched-map comparisons meaningful.
- **Frozen release mechanics.** Six source modules, including the simulation,
  environment adapter, and scripted policy, are fingerprinted. Preserving them keeps the shipped model and published evidence valid.
- **Measured deployment choices.** FP32 ONNX ships because an INT8 candidate changed
  actions during parity testing. The browser loads inference only when requested.

## The trained runner

The released policy learned through behavior cloning, four DAgger recovery
rounds, and low-rate consolidation. Its final evaluation covers **3,000 held-out
missions**, with 500 per level:

| Level | Successful escapes | Wilson 95% interval | Median time |
|---|---:|---:|---:|
| 1 — Orientation | 99.8% | 98.9–100.0% | 13.0 s |
| 2 — Surveillance | 100.0% | 99.2–100.0% | 12.7 s |
| 3 — Patrol | 96.4% | 94.4–97.7% | 21.9 s |
| 4 — Countermeasure | 98.0% | 96.4–98.9% | 23.2 s |
| 5 — Lockdown | 99.0% | 97.7–99.6% | 27.9 s |
| 6 — Ghostline | 89.6% | 86.6–92.0% | 31.1 s |

Source: [raw episode records](benchmarks/neural/champion-final-8m-500.episodes.csv)
and [aggregate report](benchmarks/neural/champion-final-8m-500.json).
The [final-test ledger](benchmarks/final-test-slices.json) prevents reusing a
consumed or retired evaluation slice. Rechecking the stored evidence does not
consume new missions.

**Limits of the result:** successful escape does not imply quiet play. The
policy can survive high trace, its routes are not proven optimal, and no matched
human study supports a superhuman claim. The released policy claims no PPO
improvement: the [PPO pilot](benchmarks/neural/ppo-pilot-rejected.json) was rejected.
Training is documented, but the archived artifacts do not support complete
reproduction from scratch. See the [model card](models/model-card.md) and
[training limitations](wiki/training.md#known-limitations).

### Verify the evidence

```bash
python -m pip install --constraint requirements.lock -e ".[dev]"
python -m pytest -q
python scripts/verify_release_evidence.py
python scripts/fuzz_ghostline_levels.py --seeds 10000
```

The evidence verifier recomputes per-level aggregates and confidence intervals
from the recorded episodes, validates artifact hashes and reward totals, and
checks the ONNX graph and environment fingerprint. It does not retrain the model
or rerun the consumed final-test slice.

Historical APIs and evidence use the field name `tier` for the level number.
The CLI accepts `--level`; older `--tier` commands remain compatible. Immutable
artifacts also retain the historical label `GhostlineEnv-v2`, which names the
same released mechanics exposed publicly as `GhostlineEnv-v1`.

## Documentation and development

- [Architecture](wiki/implementation.md) — simulation boundaries and observation contract.
- [Training and evaluation](wiki/training.md) — data collection, rejected experiments, and evidence.
- [Browser deployment](wiki/web-deployment.md) — static build and browser verification.
- [Contributing](CONTRIBUTING.md) — bug reports, development setup, and compatibility requirements.
- [Changelog](CHANGELOG.md) — release history.

Multi-agent adversarial research continues in
[ghostline-marl](https://github.com/aswanth-07/ghostline-marl); this repository
contains the released single-player game.

## Assets and license

Sprite atlases were AI-assisted and hand-cleaned. Provenance and processing
are documented in [the asset manifest](assets/licenses.json) and
[asset notes](wiki/assets.md). Generated imagery does not define collisions,
navigation, or visibility. Audio is synthesized in the project.

MIT — [License](LICENSE) · [Third-party notices](THIRD_PARTY_NOTICES.md).
