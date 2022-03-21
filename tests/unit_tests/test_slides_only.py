"""Tests."""
import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="slides-only")
def test(carousel: element.Tag):
    """Test.

    <div id="scbs-carousel-UUID" class="scbs-carousel scbs-slide" data-bs-ride="carousel">
        <div class="scbs-carousel-inner">
            <div class="scbs-carousel-item scbs-active">
                <img src="_images/local.jpg" class="scbs-d-block scbs-w-100" alt="Local Alt">
            </div>
            <div class="scbs-carousel-item">
                <img src="https://i.imgur.com/ppGH90Jl.jpg" class="scbs-d-block scbs-w-100"
                    alt="https://i.imgur.com/ppGH90Jl.jpg">
            </div>
        </div>
    </div>
    """
    carousel_inner = carousel.find_all("div", ["scbs-carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["scbs-carousel-item"])

    item = carousel_items[0]
    assert item["class"] == ["scbs-carousel-item", "scbs-active"]
    img = item.find_next()
    assert img["src"] == "_images/local.jpg"
    assert img["class"] == ["scbs-d-block", "scbs-w-100"]
    assert img["alt"] == "Local Alt"

    item = carousel_items[1]
    assert item["class"] == ["scbs-carousel-item"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/ppGH90Jl.jpg"
    assert img["class"] == ["scbs-d-block", "scbs-w-100"]
    assert img["alt"] == img["src"]

    item = carousel_items[2]
    assert item["class"] == ["scbs-carousel-item"]
    img = item.find_next()
    assert img["src"] == "_images/local.jpg"
    assert img["class"] == ["scbs-d-block", "scbs-w-100"]
    assert img["alt"] == "Local Alt"

    item = carousel_items[3]
    assert item["class"] == ["scbs-carousel-item"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/fmJnevTl.jpg"
    assert img["class"] == ["scbs-d-block", "scbs-w-100"]
    assert img["alt"] == img["src"]
