"""Tests."""
import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="linked-images")
def test(carousel: element.Tag):
    """Test.

    <div id="carousel-UUID" class="scbs-carousel scbs-slide" data-bs-ride="carousel">
        <div class="scbs-carousel-inner">
            <div class="scbs-carousel-item scbs-active">
                <a href="https://imgur.com/ppGH90J">
                    <img src="https://i.imgur.com/ppGH90Jl.jpg" class="scbs-d-block scbs-w-100"
                        alt="https://i.imgur.com/ppGH90Jl.jpg">
                </a>
            </div>
        </div>
    </div>
    """
    carousel_inner = carousel.find_all("div", ["scbs-carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["scbs-carousel-item"])

    item = carousel_items[0]
    assert item["class"] == ["scbs-carousel-item", "scbs-active"]
    a_href = item.find_next()
    assert a_href["href"] == "https://imgur.com/ppGH90J"
    img = a_href.find_next()
    assert img["src"] == "https://i.imgur.com/ppGH90Jl.jpg"
    assert img["class"] == ["scbs-d-block", "scbs-w-100"]
    assert img["alt"] == img["src"]

    item = carousel_items[1]
    assert item["class"] == ["scbs-carousel-item"]
    a_href = item.find_next()
    assert a_href["href"] == "https://imgur.com/fmJnevT"
    img = a_href.find_next()
    assert img["src"] == "https://i.imgur.com/fmJnevTl.jpg"
    assert img["class"] == ["scbs-d-block", "scbs-w-100"]
    assert img["alt"] == img["src"]
