"""Tests."""
import pytest
from bs4 import BeautifulSoup


@pytest.mark.sphinx("html", testroot="slides-only")
def test_with_alt(index_html: BeautifulSoup):
    """Test with :alt: specified.

    <div class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="a.jpg" class="d-block w-100" alt="A">
        </div>
        <div class="carousel-item">
          <img src="b.jpg" class="d-block w-100" alt="B">
        </div>
        <div class="carousel-item">
          <img src="c.jpg" class="d-block w-100" alt="C">
        </div>
      </div>
    </div>
    """
    carousel_slide = index_html.find_all("div", ["carousel", "slide"])
    assert len(carousel_slide) == 1
    carousel_inner = carousel_slide[0].find_all("div", ["carousel-inner"])
    assert len(carousel_inner) == 1

    carousel_items = carousel_inner[0].find_all("div", ["carousel-item"])
    assert len(carousel_items) == 3
    assert "active" in carousel_items[0]["class"]
    assert "active" not in carousel_items[1]["class"]
    assert "active" not in carousel_items[2]["class"]

    for item_div, letter in zip(carousel_items, ["A", "B", "C"]):
        image = item_div.find_all("img")[0]
        assert image.get("src") == f"_images/{letter.lower()}.jpg"
        assert image.get("alt") == letter
        assert image["class"] == ["d-block", "w-100"]
