"""Tests."""
import pytest

from sphinx_carousel.multi_theme import parse_themes


def test():
    """Test."""
    # 0
    with pytest.raises(IndexError):
        parse_themes([])

    # 1
    primary, secondaries = parse_themes(["a"])
    assert primary.name == "a"
    assert primary.subdir == ""
    assert [t.name for t in secondaries] == []
    assert [t.subdir for t in secondaries] == []

    # 2
    primary, secondaries = parse_themes(["a", "b"])
    assert primary.name == "a"
    assert primary.subdir == ""
    assert [t.name for t in secondaries] == ["b"]
    assert [t.subdir for t in secondaries] == ["theme_b"]

    # 3
    primary, secondaries = parse_themes(["a", "b", "c"])
    assert primary.name == "a"
    assert primary.subdir == ""
    assert [t.name for t in secondaries] == ["b", "c"]
    assert [t.subdir for t in secondaries] == ["theme_b", "theme_c"]

    # 4
    primary, secondaries = parse_themes(["a", "b", "c", "c"])
    assert primary.name == "a"
    assert primary.subdir == ""
    assert [t.name for t in secondaries] == ["b", "c", "c"]
    assert [t.subdir for t in secondaries] == ["theme_b", "theme_c", "theme_c2"]

    # 7
    primary, secondaries = parse_themes(["a", "b", "c", "d", "c", "c", "c"])
    assert primary.name == "a"
    assert primary.subdir == ""
    assert [t.name for t in secondaries] == ["b", "c", "d", "c", "c", "c"]
    assert [t.subdir for t in secondaries] == ["theme_b", "theme_c", "theme_d", "theme_c2", "theme_c3", "theme_c4"]
