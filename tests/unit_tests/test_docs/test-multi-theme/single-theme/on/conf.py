"""Sphinx test configuration."""
from sphinx_carousel.unrelated import MultiTheme

exclude_patterns = ["_build"]
extensions = ["sphinx_carousel.carousel"]
master_doc = "index"
nitpicky = True
html_theme = MultiTheme.select_theme(["alabaster"])
