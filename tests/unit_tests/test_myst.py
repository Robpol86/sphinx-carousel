"""Tests."""
import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="myst")
def test(carousel: element.Tag):
    """Test."""
    carousel_inner = carousel.find_all("div", ["carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["carousel-item"])

    item = carousel_items[0]
    assert item["class"] == ["carousel-item", "active"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/fmJnevTl.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]
