"""Tests."""
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="controls")
def test(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0].find_all(recursive=False)

    assert carousel[0]["class"] == ["scbs-carousel-inner"]

    assert carousel[1]["class"] == ["scbs-carousel-control-prev"]
    assert carousel[1]["data-bs-slide"] == "prev"
    spans = carousel[1].find_all(recursive=False)
    assert spans[0]["class"] == ["scbs-carousel-control-prev-icon"]
    assert spans[1]["class"] == ["scbs-visually-hidden"]
    assert spans[1].get_text(strip=True) == "Previous"

    assert carousel[2]["class"] == ["scbs-carousel-control-next"]
    assert carousel[2]["data-bs-slide"] == "next"
    spans = carousel[2].find_all(recursive=False)
    assert spans[0]["class"] == ["scbs-carousel-control-next-icon"]
    assert spans[1]["class"] == ["scbs-visually-hidden"]
    assert spans[1].get_text(strip=True) == "Next"


@pytest.mark.sphinx("html", testroot="controls")
def test_div_id_match(carousel: element.Tag):
    """Test."""
    carousel_main_id = carousel["id"]
    control_target = carousel.find_next("button")["data-bs-target"]
    assert control_target == f"#{carousel_main_id}"


@pytest.mark.sphinx("html", testroot="controls")
def test_toggle(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-inner"]
    assert carousel[1]["class"] == ["scbs-carousel-control-prev"]
    assert carousel[2]["class"] == ["scbs-carousel-control-next"]

    carousel = carousels[1].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-inner"]
    assert len(carousel) == 1

    carousel = carousels[2].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-inner"]
    assert len(carousel) == 1


@pytest.mark.sphinx("html", testroot="controls-conf")
def test_toggle_conf(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-inner"]
    assert carousel[1]["class"] == ["scbs-carousel-control-prev"]
    assert carousel[2]["class"] == ["scbs-carousel-control-next"]

    carousel = carousels[1].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-inner"]
    assert len(carousel) == 1

    carousel = carousels[2].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-inner"]
    assert carousel[1]["class"] == ["scbs-carousel-control-prev"]
    assert carousel[2]["class"] == ["scbs-carousel-control-next"]
