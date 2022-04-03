"""Sphinx test configuration."""
from sphinx_carousel.multi_theme import select_theme

exclude_patterns = ["_build"]
extensions = ["sphinx_carousel.carousel"]
master_doc = "index"
nitpicky = True
html_theme = select_theme(["alabaster", "classic"])
