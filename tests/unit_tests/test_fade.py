"""Tests."""
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="fade/default")
def test_default(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide", "scbs-carousel-fade"]

    carousel = carousels[1]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide"]

    carousel = carousels[2]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide"]


@pytest.mark.sphinx("html", testroot="fade/sphinx-conf")
def test_conf(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide", "scbs-carousel-fade"]

    carousel = carousels[1]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide"]

    carousel = carousels[2]
    assert carousel["class"] == ["scbs-carousel", "scbs-slide", "scbs-carousel-fade"]
