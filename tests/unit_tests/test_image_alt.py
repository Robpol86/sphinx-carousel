"""Tests."""
import pytest
from bs4 import BeautifulSoup


@pytest.mark.sphinx("html", testroot="image-alt")
def test(index_html: BeautifulSoup):
    """Test.

    <div class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="_images/a.jpg" class="d-block w-100" alt="A">
        </div>
        <div class="carousel-item">
          <img src="_images/b.jpg" class="d-block w-100" alt="_images/b.jpg">
        </div>
        <div class="carousel-item">
          <img src="_images/c.jpg" class="d-block w-100" alt="C">
        </div>
      </div>
    </div>
    """
    carousel_slide = index_html.find_all("div", ["carousel", "slide"])[0]
    carousel_inner = carousel_slide.find_all("div", ["carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["carousel-item"])

    item = carousel_items[0]
    assert item["class"] == ["carousel-item", "active"]
    img = item.find_all("img")[0]
    assert img["src"] == "_images/a.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == "A"

    item = carousel_items[1]
    assert item["class"] == ["carousel-item"]
    img = item.find_all("img")[0]
    assert img["src"] == "_images/b.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]

    item = carousel_items[2]
    assert item["class"] == ["carousel-item"]
    img = item.find_all("img")[0]
    assert img["src"] == "_images/c.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == "C"
