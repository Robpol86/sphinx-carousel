"""Tests."""
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="id-data-ride")
def test_id(carousels: List[element.Tag]):
    """Test.

    <div id="customId" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="_images/a.jpg" class="d-block w-100" alt="_images/a.jpg">
        </div>
      </div>
    </div>
    """
    carousel_slide = carousels[0]
    assert carousel_slide.has_attr("id")
    assert carousel_slide["id"] == "customId"
    assert carousel_slide.has_attr("data-ride")
    assert carousel_slide["data-ride"] == "carousel"

    carousel_inner = carousel_slide.find_all("div", ["carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["carousel-item"])
    item = carousel_items[0]
    assert item["class"] == ["carousel-item", "active"]
    img = item.find_all("img")[0]
    assert img["src"] == "_images/a.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]


@pytest.mark.sphinx("html", testroot="id-data-ride")
def test_no_data_ride(carousels: List[element.Tag]):
    """Test.

    <div class="carousel slide">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="_images/a.jpg" class="d-block w-100" alt="_images/a.jpg">
        </div>
      </div>
    </div>
    """
    carousel_slide = carousels[1]
    assert carousel_slide.has_attr("id")
    assert len(carousel_slide["id"]) == 45
    assert carousel_slide["id"].startswith("carousel-")
    assert not carousel_slide.has_attr("data-ride")

    carousel_inner = carousel_slide.find_all("div", ["carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["carousel-item"])
    item = carousel_items[0]
    assert item["class"] == ["carousel-item", "active"]
    img = item.find_all("img")[0]
    assert img["src"] == "_images/a.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]
