"""Tests."""
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="external-image")
def test(carousels: List[element.Tag]):
    """Test.

    <div class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="https://i.imgur.com/fmJnevTl.jpg" class="d-block w-100" alt="https://i.imgur.com/fmJnevTl.jpg">
        </div>
        <div class="carousel-item">
          <img src="https://i.imgur.com/ppGH90Jl.jpg" class="d-block w-100" alt="https://i.imgur.com/ppGH90Jl.jpg">
        </div>
        <div class="carousel-item">
          <img src="https://i.imgur.com/fWyn9A2l.jpg" class="d-block w-100" alt="https://i.imgur.com/fWyn9A2l.jpg">
        </div>
      </div>
    </div>
    """
    carousel_slide = carousels[0]
    carousel_inner = carousel_slide.find_all("div", ["carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["carousel-item"])

    item = carousel_items[0]
    assert item["class"] == ["carousel-item", "active"]
    img = item.find_all("img")[0]
    assert img["src"] == "https://i.imgur.com/fmJnevTl.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]

    item = carousel_items[1]
    assert item["class"] == ["carousel-item"]
    img = item.find_all("img")[0]
    assert img["src"] == "https://i.imgur.com/ppGH90Jl.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]

    item = carousel_items[2]
    assert item["class"] == ["carousel-item"]
    img = item.find_all("img")[0]
    assert img["src"] == "https://i.imgur.com/fWyn9A2l.jpg"
    assert img["class"] == ["d-block", "w-100"]
    assert img["alt"] == img["src"]
