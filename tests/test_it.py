"""Test cases for generating files."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="default")
def test_default_build(app: SphinxTestApp):  # noqa
    app.build()
    assert (Path(app.srcdir) / "test.css").exists()
