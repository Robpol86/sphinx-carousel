"""Tests."""
import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="slides-only")
def test(carousel: element.Tag):
    """Test.

    <div id="carousel-UUID" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="_images/local.jpg" class="d-block w-100" alt="Local Alt">
            </div>
            <div class="carousel-item">
                <img src="https://i.imgur.com/ppGH90Jl.jpg" class="d-block w-100" alt="https://i.imgur.com/ppGH90Jl.jpg">
            </div>
        </div>
    </div>
    """
    carousel_inner = carousel.find_all("div", ["carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["carousel-item"])

    item = carousel_items[0]
    assert item["class"] == ["carousel-item", "active"]
    img = item.find_all("img")[0]
    assert img["src"] == "_images/local.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == "Local Alt"

    item = carousel_items[1]
    assert item["class"] == ["carousel-item"]
    img = item.find_all("img")[0]
    assert img["src"] == "https://i.imgur.com/ppGH90Jl.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]
