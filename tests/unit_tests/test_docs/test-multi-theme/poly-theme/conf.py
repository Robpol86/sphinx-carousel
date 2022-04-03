"""Sphinx test configuration."""
from sphinx_carousel.multi_theme import MultiTheme

exclude_patterns = ["_build"]
extensions = ["sphinx_carousel.carousel"]
master_doc = "index"
nitpicky = True
html_theme = MultiTheme.select_theme(["alabaster", "classic", "traditional"])
