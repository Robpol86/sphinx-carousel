"""Tests."""
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="dark/default")
def test_default(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide", "scbs-carousel-dark"]

    carousel = carousels[1]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide"]

    carousel = carousels[2]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide"]


@pytest.mark.sphinx("html", testroot="dark/sphinx-conf")
def test_conf(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide", "scbs-carousel-dark"]

    carousel = carousels[1]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide"]

    carousel = carousels[2]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide", "scbs-carousel-dark"]
