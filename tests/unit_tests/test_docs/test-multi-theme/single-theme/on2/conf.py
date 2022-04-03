"""Sphinx test configuration."""
import os

from sphinx_carousel.multi_theme import MultiTheme

assert os.environ["SPHINX_MULTI_THEME"] == "false"

exclude_patterns = ["_build"]
extensions = ["sphinx_carousel.carousel"]
master_doc = "index"
nitpicky = True
html_theme = MultiTheme.select_theme(["alabaster", "classic"])
