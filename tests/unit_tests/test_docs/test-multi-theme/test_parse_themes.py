"""Tests."""
import pytest

from sphinx_carousel.multi_theme import parse_themes


def test():
    """Test."""
    with pytest.raises(IndexError):
        parse_themes([])

    assert parse_themes(["a"]) == ("a", [], [])
    assert parse_themes(["a", "b"]) == ("a", ["b"], ["theme_b"])
    assert parse_themes(["a", "b", "c"]) == ("a", ["b", "c"], ["theme_b", "theme_c"])
    assert parse_themes(["a", "b", "c", "c"]) == ("a", ["b", "c", "c"], ["theme_b", "theme_c", "theme_c2"])

    assert parse_themes(["a", "b", "c", "d", "c", "c", "c"]) == (
        "a",
        ["b", "c", "d", "c", "c", "c"],
        ["theme_b", "theme_c", "theme_d", "theme_c2", "theme_c3", "theme_c4"],
    )
