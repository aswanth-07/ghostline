from contextlib import contextmanager

import pytest

from ghostline import resources


def test_packaged_asset_keeps_resource_alive_and_propagates_consumer_errors(tmp_path, monkeypatch):
    asset = tmp_path / "_assets" / "example.txt"
    asset.parent.mkdir()
    asset.write_text("example")
    monkeypatch.setattr(resources, "files", lambda _package: tmp_path)
    state = {"open": False}

    @contextmanager
    def resolve(path):
        state["open"] = True
        try:
            yield path
        finally:
            state["open"] = False

    monkeypatch.setattr(resources, "as_file", resolve)
    failure = OSError("asset consumer failed")
    with pytest.raises(OSError) as caught:
        with resources.runtime_asset_path("example.txt") as path:
            assert path == asset
            assert state["open"]
            raise failure
    assert caught.value is failure
    assert not state["open"]


def test_unavailable_package_resource_falls_back_to_checkout(tmp_path, monkeypatch):
    asset = tmp_path / "example.txt"
    asset.write_text("example")

    class MissingResource:
        def joinpath(self, *_parts):
            return self

        def is_file(self):
            raise OSError("package unavailable")

    monkeypatch.setattr(resources, "files", lambda _package: MissingResource())
    monkeypatch.chdir(tmp_path)
    with resources.runtime_asset_path("example.txt") as path:
        assert path == asset
