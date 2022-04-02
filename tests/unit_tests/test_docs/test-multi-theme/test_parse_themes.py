"""Tests."""
import pytest

from sphinx_carousel.unrelated import MultiTheme


def test():
    """Test."""
    with pytest.raises(IndexError):
        MultiTheme.parse_themes([])

    assert MultiTheme.parse_themes(["a"]) == ("a", [], [])
    assert MultiTheme.parse_themes(["a", "b"]) == ("a", ["b"], ["theme_b"])
    assert MultiTheme.parse_themes(["a", "b", "c"]) == ("a", ["b", "c"], ["theme_b", "theme_c"])
    assert MultiTheme.parse_themes(["a", "b", "c", "c"]) == ("a", ["b", "c", "c"], ["theme_b", "theme_c", "theme_c2"])
    assert MultiTheme.parse_themes(["a", "b", "c", "d", "c"]) == (
        "a",
        ["b", "c", "d", "c"],
        ["theme_b", "theme_c", "theme_d", "theme_c2"],
    )
