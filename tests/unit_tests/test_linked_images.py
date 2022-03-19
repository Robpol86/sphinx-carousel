"""Tests."""
import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="linked-images")
def test(carousel: element.Tag):
    """Test.

    <div id="carousel-UUID" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <a href="https://imgur.com/ppGH90J">
                    <img src="https://i.imgur.com/ppGH90Jl.jpg" class="d-block w-100" alt="https://i.imgur.com/ppGH90Jl.jpg">
                </a>
            </div>
        </div>
    </div>
    """
    carousel_inner = carousel.find_all("div", ["carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["carousel-item"])

    item = carousel_items[0]
    assert item["class"] == ["carousel-item", "active"]
    a_href = item.next
    assert a_href["href"] == "https://imgur.com/ppGH90J"
    img = a_href.next
    assert img["src"] == "https://i.imgur.com/ppGH90Jl.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]
