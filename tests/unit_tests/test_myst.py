"""Tests."""
import pytest
from bs4 import BeautifulSoup


@pytest.mark.sphinx("html", testroot="myst")
def test(index_html: BeautifulSoup):
    """Test."""
    carousel_slide = index_html.find_all("div", ["carousel", "slide"])[0]
    carousel_inner = carousel_slide.find_all("div", ["carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["carousel-item"])

    item = carousel_items[0]
    assert item["class"] == ["carousel-item", "active"]
    img = item.find_all("img")[0]
    assert img["src"] == "https://i.imgur.com/fmJnevTl.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]
