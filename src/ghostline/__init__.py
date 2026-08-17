"""Ghostline game, simulation, and reinforcement-learning environment."""

import importlib
import sys

__all__: list[str] = []
__version__ = "1.0.0"


def register_env() -> None:
    """Register the public Gymnasium environment once."""
    import gymnasium as gym

    if "GhostlineEnv-v1" not in gym.registry:
        gym.register("GhostlineEnv-v1", entry_point="ghostline.env_v1:PublishedGhostlineEnvV1")
    if "GhostlineLegacyEnv-v0" not in gym.registry:
        gym.register("GhostlineLegacyEnv-v0", entry_point="ghostline.env:GhostlineEnvV1")


if sys.platform != "emscripten":
    GhostlineEnv = getattr(
        importlib.import_module("ghostline.env_v1"),
        "PublishedGhostlineEnvV1",
    )
    __all__.append("GhostlineEnv")
    register_env()
