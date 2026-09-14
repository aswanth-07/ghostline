# Ghostline

Ghostline is a single-player pixel-art stealth game set in procedurally generated facilities. Steal enough data to open an extraction route, avoid cameras and patrols, and escape before the clock or your integrity runs out. Security raises your trace when it detects you; breaking line of sight lowers it.

[Play in your browser](https://ghostline-rho.vercel.app). Read [how to play](#how-to-play), [run the game locally](#run-locally), or review the [policy results](#policy-results).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12–3.14-blue.svg)](pyproject.toml)

[![Ghostline gameplay showing the trained runner escaping a Level 6 facility](assets/screenshots/ghostline-demo.gif)](videos/ghostline-demo.mp4)

*The bundled neural policy completes a Level 6 mission. [Watch the full recording](videos/ghostline-demo.mp4) or [view a still frame](assets/screenshots/gameplay-stealth-v3.png).*

## How to play

1. Explore the facility and find the amber data terminals.
2. Stand near a terminal to download from it. Collect the required quota before taking extra data for score.
3. Break line of sight when security spots you. Dash to move quickly or use a limited disruption pulse to disable electronics and jam guard radios.
4. Reach the green extraction relay after meeting the quota. You lose if time or integrity reaches zero.

| Control | Action |
|---|---|
| `WASD` | Move |
| `Shift` | Dash: fast, noisy, and limited by energy |
| `Space` | Use the disruption pulse, available from Level 2 |
| `Esc` | Pause |

Touch controls include an on-screen stick plus dash, pulse, and pause buttons. The local game also supports remappable controls, contrast options, reduced motion, sound captions, and an optional timer assist.

Open Agent Lab locally or choose Agent Takeover in the browser to watch the trained runner. The policy follows the same rules and receives only player-visible information. You can take control again from the browser toolbar.

## Six security levels

A level sets the security, quota, and time limit. A map seed identifies one facility layout, so replaying the same seed produces the same mission.

| Level | Mission | What you face | Data quota | Time limit |
|---|---|---|---:|---:|
| **1** | **Orientation** | Learn to download and extract, with no cameras or guards | 3 | 1:55 |
| **2** | **Surveillance** | Sweeping cameras and your first disruption pulse | 4 | 2:15 |
| **3** | **Patrol** | Guards that investigate noise and share alerts | 5 | 2:40 |
| **4** | **Countermeasure** | A larger facility, more cameras, and more pulse charges | 6 | 3:00 |
| **5** | **Lockdown** | Response drones deploy when trace reaches its maximum | 7 | 3:25 |
| **6** | **Ghostline** | Dense security and drones that deploy at a lower trace threshold | 8 | 3:45 |

A successful escape in the local Play Levels menu unlocks the next level. The browser mission selector and Agent Lab let you choose any of the six. Each level generates many layouts rather than loading one fixed map.

## Run locally

Ghostline supports Python 3.12 through 3.14. Clone the repository and create a virtual environment:

```bash
git clone https://github.com/aswanth-07/ghostline.git
cd ghostline
python -m venv .venv
```

Activate it with `source .venv/bin/activate` on macOS or Linux. In Windows PowerShell, use `.\.venv\Scripts\Activate.ps1`. Then install Ghostline through the locked dependency set:

```bash
python -m pip install --constraint requirements.lock -e .
ghostline play
```

Practice a repeatable mission with `ghostline play --level 1 --seed 42`.

Install the optional policy dependencies to replay the map used in the gameplay video:

```bash
python -m pip install --constraint requirements.lock -e ".[agent]"
ghostline lab --level 6 --seed 2000000
```

The [setup and packaging guide](wiki/setup.md) covers recording, training, and Windows builds.

## How Ghostline works

Ghostline is both a game and a reinforcement learning benchmark. Human input and policy actions drive the same deterministic simulation at 60 Hz. The policy acts at 10 Hz and chooses from 36 actions formed by nine movement choices, dash on or off, and pulse on or off.

The policy receives structured versions of information shown through the player's heads-up display, minimap, and facility telemetry. It does not receive hidden live enemy positions.

| Part | What it does |
|---|---|
| [Simulation](src/ghostline/simulation.py) and [generation](src/ghostline/generation.py) | Defines game rules, seeded facilities, collision, security, and extraction |
| [Environment](src/ghostline/env_v1.py) | Provides the public `GhostlineEnv-v1` Gymnasium interface |
| [Model](src/ghostline/model.py) | Combines a local-grid convolution, masked entity attention, and a 384-unit gated recurrent unit |
| [Presentation](src/ghostline/presentation.py) and [app](src/ghostline/app.py) | Draws the game and handles controls, progression, menus, and Agent Lab |
| [Browser build](web/) | Runs the Pygbag and WebAssembly simulation and loads ONNX Runtime Web only when policy control is requested |
| [Benchmarks](benchmarks/) | Stores episode records, training history, export parity results, and the final-test ledger |

The design follows four release constraints:

- Play and learning use one simulation. Rendering stays outside the rules engine, which allows headless training without a second copy of the game rules.
- The policy sees no privileged live enemy coordinates. This keeps matched-map comparisons tied to information a player could observe.
- Six source modules are fingerprinted, including the simulation, environment adapter, and scripted policy. Changing them would invalidate the released model and its evidence.
- The browser ships the 32-bit floating-point ONNX model. An 8-bit quantized candidate was smaller but changed actions during parity testing.

## Policy results

The released policy learned from behavior cloning, four Dataset Aggregation recovery rounds, and a final low-learning-rate consolidation stage. The final evaluation contains 3,000 held-out missions, with 500 missions at each level.

| Level | Successful escapes | Wilson 95% interval | Median time |
|---|---:|---:|---:|
| 1 — Orientation | 99.8% | 98.9–100.0% | 13.0 s |
| 2 — Surveillance | 100.0% | 99.2–100.0% | 12.7 s |
| 3 — Patrol | 96.4% | 94.4–97.7% | 21.9 s |
| 4 — Countermeasure | 98.0% | 96.4–98.9% | 23.2 s |
| 5 — Lockdown | 99.0% | 97.7–99.6% | 27.9 s |
| 6 — Ghostline | 89.6% | 86.6–92.0% | 31.1 s |

The [raw episode records](benchmarks/neural/champion-final-8m-500.episodes.csv) and [aggregate report](benchmarks/neural/champion-final-8m-500.json) contain the source data. The [final-test ledger](benchmarks/final-test-slices.json) prevents reuse of a consumed or retired evaluation slice. Checking stored evidence does not consume new missions.

Successful escape does not mean quiet or optimal play. The policy can survive high trace, and its routes have not been proven optimal. No matched human study supports a superhuman claim. A current-policy Proximal Policy Optimization pilot performed worse on its validation seeds, so the release keeps the behavior-cloning and Dataset Aggregation checkpoint and claims no improvement from that pilot. The [rejected pilot report](benchmarks/neural/ppo-pilot-rejected.json) records the comparison.

The repository documents training, but the archived artifacts do not support complete reproduction from scratch. The [model card](models/model-card.md) and [training limitations](wiki/training.md#known-limitations) describe these limits.

## Verify the evidence

Install the development dependencies and run the local checks:

```bash
python -m pip install --constraint requirements.lock -e ".[dev]"
python -m pytest -q
python scripts/verify_release_evidence.py
python scripts/fuzz_ghostline_levels.py --seeds 10000
```

The evidence verifier recomputes each level's aggregates and confidence intervals from the recorded episodes. It also checks artifact hashes, reward totals, the ONNX graph, and the environment fingerprint. It does not retrain the model or rerun the consumed final-test slice.

Historical APIs and evidence use the field name `tier` for the level number. The command line accepts `--level`, while older `--tier` commands remain compatible. Immutable artifacts also retain the historical label `GhostlineEnv-v2`; the public environment name for the same released mechanics is `GhostlineEnv-v1`.

## Documentation

- [Architecture](wiki/implementation.md): simulation boundaries and the observation contract
- [Training and evaluation](wiki/training.md): data collection, rejected experiments, and evidence
- [Browser deployment](wiki/web-deployment.md): static builds and browser verification
- [Contributing](CONTRIBUTING.md): bug reports, development setup, and compatibility requirements
- [Changelog](CHANGELOG.md): release history

The separate [ghostline-marl](https://github.com/aswanth-07/ghostline-marl) repository contains the active multi-agent adversarial research. This repository contains the released single-player game.

## Assets and license

The sprite atlases were made with AI assistance and cleaned by hand. The [asset manifest](assets/licenses.json) and [asset notes](wiki/assets.md) record their source and processing steps. Generated images do not define collision, navigation, or visibility. The project synthesizes its audio.

Ghostline uses the [MIT License](LICENSE). See [third-party notices](THIRD_PARTY_NOTICES.md) for bundled dependencies and assets.
