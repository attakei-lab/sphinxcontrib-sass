from os import PathLike
from pathlib import Path
from typing import Dict

import sass
from sphinx.application import Sphinx
from sphinx.util import logging


logger = logging.getLogger(__name__)


Targets = Dict[PathLike, PathLike]


def build_sass_sources(app: Sphinx, env):
    logger.debug("Building stylesheet files")
    out_dir = Path(app.config.sass_out_dir)
    targets: Targets = app.config.sass_targets
    output_style = app.config.sass_output_style
    # Create output directory
    out_dir.mkdir(exist_ok=True, parents=True)
    # Build css files
    for src, dst in targets.items():
        src_ = Path(src)
        content = src_.read_text()
        css = sass.compile(
            string=content, output_style=output_style, include_paths=[str(src_.parent)]
        )
        Path(dst).write_text(css)


def setup(app: Sphinx):
    """
    Setup function for this extension.
    """
    logger.debug(f"Using {__name__}")
    app.add_config_value("sass_out_dir", None, "html")
    app.add_config_value("sass_targets", {}, "html")
    app.add_config_value("sass_output_style", "nested", "html")
    app.connect("env-updated", build_sass_sources)
