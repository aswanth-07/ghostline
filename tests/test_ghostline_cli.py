"""Level-oriented commands retain the released argument contract."""

import sys

import pytest

from ghostline.cli import build_parser, main


@pytest.mark.parametrize("command", ["play", "lab", "record", "evaluate"])
def test_level_and_historical_tier_select_the_same_mission(command):
    parser = build_parser()
    current = parser.parse_args([command, "--level", "4"])
    historical = parser.parse_args([command, "--tier", "4"])
    assert vars(current) == vars(historical)
    assert current.tier == 4
    for invalid in ("0", "7"):
        with pytest.raises(SystemExit):
            parser.parse_args([command, "--level", invalid])


def test_collection_and_training_level_aliases_preserve_parameters():
    parser = build_parser()
    prefix = ["imitate", "collect", "--output", "artifacts/example"]
    current = parser.parse_args(prefix + ["--levels", "2,4", "--episodes-per-level", "7"])
    historical = parser.parse_args(prefix + ["--tiers", "2,4", "--episodes-per-tier", "7"])
    assert vars(current) == vars(historical)
    assert current.tiers == "2,4"
    assert current.episodes_per_tier == 7
    assert vars(parser.parse_args(["train", "--initial-curriculum-level", "3"])) == vars(
        parser.parse_args(["train", "--initial-curriculum-tier", "3"])
    )


def test_play_level_and_seed_reach_the_game(monkeypatch):
    from ghostline import app

    observed = {}

    class Player:
        def __init__(self, **kwargs):
            observed.update(kwargs)

        def run(self):
            return 0

    monkeypatch.setattr(app, "GameApp", Player)
    monkeypatch.setattr(sys, "argv", ["ghostline", "play", "--level", "3", "--seed", "42"])
    with pytest.raises(SystemExit) as result:
        main()
    assert result.value.code == 0
    assert observed == {"initial_tier": 3, "seed": 42, "mode": "play"}
