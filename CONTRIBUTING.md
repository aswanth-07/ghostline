# Contributing

Ghostline is a released single-player game and research benchmark. Bug reports,
reproducible failures, documentation fixes, and questions about the method are
welcome. Open an issue with the level, map seed, platform, and steps to reproduce.
Discuss feature proposals before implementation so they fit the release contract.

## Setup

```bash
python -m venv .venv && . .venv/bin/activate    # Windows: .\.venv\Scripts\Activate.ps1
python -m pip install --constraint requirements.lock -e ".[dev]"
python -m pytest -q
```

Always install through `requirements.lock`. CI runs `pip check`, and an
unpinned resolve will pass locally and fail there.

## Preserve the released contract

The fingerprint covers six modules under `src/ghostline/`: `config.py`, `env.py`,
`generation.py`, `policies.py`, `simulation.py`, and `types.py`. Preserve them
when making presentation or documentation changes.

Those six files are hashed together into the environment fingerprint
`521c449a8bd9a540977a918f5b094dd3aeff44cc579a55f75e22a74bab20e129`. Changing a
source byte, apart from normalized line endings, invalidates the trained checkpoint, the
3,000-episode benchmark, the ONNX parity record and the throughput report, all
of which are bound to that hash. `verify_release_evidence.py` will fail, and it
is meant to.

If a mechanics change is genuinely needed, it belongs in a new environment
version with its own fingerprint and its own evidence, not in an edit to these.

The same reasoning applies to the strings inside published artifacts. Those
records say `GhostlineEnv-v2` where the public id is `GhostlineEnv-v1`; both
name the same environment and the label is historical. Rewriting it inside a
hash-bound artifact destroys the evidence it authenticates.

## Before opening a pull request

```bash
python -m pytest -q
python scripts/verify_release_evidence.py
python scripts/fuzz_ghostline_levels.py --seeds 10000
```

For renderer changes, also run `python scripts/qa_scaled_visuals.py` and check
the captures. The capture harness declares its own copy of each screen; a
regression pins it against the live menus, because that duplication has drifted
before and once hid real UI clipping from every tracked screenshot.

## Review expectations

- **Measure before claiming.** The repository publishes its rejected INT8
  export and its rejected PPO pilot next to the accepted result. A change that
  did not work is worth recording.
- **Tests should be able to fail.** Prefer a check that would catch the
  regression you are guarding against; a green assertion that cannot go red is
  not coverage.
- Match the surrounding style rather than introducing a new one.
