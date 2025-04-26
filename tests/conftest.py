"""Configuration for pytest."""

from __future__ import annotations

from pathlib import Path

import pytest
import sphinx
from packaging import version

pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


@pytest.fixture(scope="session")
def rootdir():
    """Set root directory to use testing sphinx project."""
    current_ver = version.parse(sphinx.__version__)
    delimter_ver = version.parse("7.2.0")
    if current_ver < delimter_ver:
        from sphinx.testing.path import path

        return path(__file__).parent.abspath() / "roots"
    return Path(__file__).parent.resolve() / "roots"
