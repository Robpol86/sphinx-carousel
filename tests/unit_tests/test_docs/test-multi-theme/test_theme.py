"""Tests."""
from sphinx_carousel.multi_theme import Theme


def test():
    """Test."""
    theme = Theme("name")
    assert theme.name == "name"
    assert theme.subdir == ""

    theme = Theme("name", "subdir")
    assert theme.name == "name"
    assert theme.subdir == "subdir"

    assert repr(theme) == "Theme(name='name', subdir='subdir')"
