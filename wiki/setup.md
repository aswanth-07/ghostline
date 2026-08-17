---
title: Ghostline Setup and Release
updated: 2026-07-28
status: active
---

# Setup and release

Python 3.13 is the locked release baseline. CI also checks the base runtime on
Python 3.12 and 3.14. Use the repository `.venv` and `requirements.lock` for
every command. Other local virtual environments are unsupported.

## Install and play

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install --constraint requirements.lock -e .
ghostline play
```

The base install has no PyTorch, ONNX Runtime, recording codec or packager
dependency. The environment runs headlessly with deterministic scripted
controllers.

## Agent Lab and development

```powershell
# Lightweight published-v1 ONNX inference; no PyTorch.
python -m pip install --constraint requirements.lock -e ".[agent]"
ghostline lab --tier 6 --seed 2000000

# Tests, lock maintenance, and distributions.
python -m pip install --constraint requirements.lock -e ".[dev]"
python -m pytest -q
```

A missing or incompatible policy falls back to human or scripted control, so a
broken checkpoint can never prevent play.

## Contract smoke

```powershell
python -c "import gymnasium as gym, ghostline; e=gym.make('GhostlineEnv-v1'); print(e.action_space)"
```

The expected action space is `Discrete(36)`.

## Correctness and generation

```powershell
# Level contract: 10,000 seeds, zero invalid levels.
python scripts/fuzz_ghostline_levels.py --seeds 10000

# Release throughput gate.
python scripts/benchmark_ghostline.py --decisions 10000 --tier 6 --workers 22 --minimum-decisions-per-second 3000 --output benchmarks/system/headless-throughput.json
```

## Reproducing the training lineage

```powershell
python -m pip install --constraint requirements.lock -e ".[train]"

ghostline imitate collect --output artifacts/teacher-data --episodes-per-tier 100 --overwrite
ghostline imitate bc --dataset artifacts/teacher-data --output artifacts/bc-current
ghostline imitate dagger --base-dataset artifacts/teacher-data --initial-checkpoint artifacts/bc-current/best.pt --output artifacts/dagger --beta-start 0
ghostline train --hours 24 --experiment ghostline-universal --init-checkpoint PATH_FROM_DAGGER_OUTPUT --initial-curriculum-tier 6
```

These reproduce the published lineage. The resulting checkpoint and evidence
metadata carry the historical internal label `GhostlineEnv-v2`; the public
environment id is `GhostlineEnv-v1`. Both name the same environment.

## Recording, ONNX export, and Windows package

The package ships the verified champion:

```powershell
python -m pip install --constraint requirements.lock -e ".[train,media,build]"
ghostline record --model models/ghostline-policy.pt --tier 6 --seed 2000000 --output videos/ghostline-demo.mp4
ghostline export --model models/ghostline-policy.pt --output models/ghostline-policy.fp32.onnx --quantize --deployment-output models/ghostline-policy.onnx --parity-samples 1000
Copy-Item models/ghostline-policy.fp32.parity.json benchmarks/neural/champion-onnx-parity.json
python scripts/verify_release_evidence.py
ghostline package --model models/ghostline-policy.onnx
.\dist\Ghostline.exe --release-smoke-test
```

The ONNX metadata must still say historical `GhostlineEnv-v2` because release
verification binds those exact bytes. Packaging maps that artifact to public
v1 in UI and documentation. It must not relabel graph metadata.

The FP32 export is canonical. Dynamic INT8 becomes the deployment graph only
after at least 1,000 recurrent transitions produce zero deterministic-action
mismatches; otherwise verified FP32 is deployed.

The player executable contains the game, declared runtime art, ONNX Runtime,
the verified policy, licenses, and notices. It excludes Torch, trainers,
TensorBoard, and recording codecs. `--human-only` is diagnostic and not a
portfolio release.

## Wheel and clean-install gate

```powershell
python -m build
python scripts/verify_source_archive.py
python scripts/verify_clean_install.py
```

The clean-install probe installs the base wheel in an isolated environment,
confirms Pygame and Torch imports stay deferred, steps the environment, checks
the 36-action space, verifies the historical-contract annotation, and renders a
headless frame.

The archive audit enumerates the documentation it expects and fails closed on
any other page under `wiki/`, so the manifest lists each published page by name
instead of globbing the directory. A directory-wide pattern packages whatever
Markdown happens to sit on disk at build time, which is not the same set as the
pages the project publishes. Delete `src/ghostline.egg-info/` before rebuilding
after a manifest change: setuptools reuses the cached `SOURCES.txt` and would
otherwise ship the previous file list.

## Static web build

```powershell
# Human-only diagnostic.
python scripts/build_web.py --human-only

# Published v1 portfolio build.
python scripts/build_web.py --model models/ghostline-policy.onnx
```

The runtime stage copies an explicit module allowlist rather than the whole
package, so the browser bundle cannot silently grow. Interactive QA uses Chrome
only.

## Dependency lock

After deliberately changing direct pins in `pyproject.toml`:

```powershell
python -m piptools compile --extra=agent --extra=build --extra=dev --extra=media --extra=train --extra=web --output-file=requirements.lock --strip-extras pyproject.toml
python -m pip check
```

Never change dependencies during a long run. Stop, update the lock, run every
smoke gate, and resume only from a checkpoint whose full contract still
matches.
