"""Tests."""
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="indicators/default")
def test(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0].find_all(recursive=False)
    assert carousel[1]["class"] == ["scbs-carousel-inner"]

    assert carousel[0]["class"] == ["scbs-carousel-indicators"]
    buttons = carousel[0].find_all(recursive=False)
    assert len(buttons) == 3

    assert buttons[0]["data-bs-slide-to"] == "0"
    assert buttons[1]["data-bs-slide-to"] == "1"
    assert buttons[2]["data-bs-slide-to"] == "2"

    assert buttons[0]["aria-label"] == "Slide 1"
    assert buttons[1]["aria-label"] == "Slide 2"
    assert buttons[2]["aria-label"] == "Slide 3"

    assert buttons[0].get("class") == ["scbs-active"]
    assert buttons[1].has_attr("class") is False
    assert buttons[2].has_attr("class") is False

    assert buttons[0].get("aria-current") == "true"
    assert buttons[1].has_attr("aria-current") is False
    assert buttons[2].has_attr("aria-current") is False


@pytest.mark.sphinx("html", testroot="indicators/default")
def test_div_id_match(carousel: element.Tag):
    """Test."""
    carousel_main_id = carousel["id"]
    control_target = carousel.find_next("button")["data-bs-target"]
    assert control_target == f"#{carousel_main_id}"


@pytest.mark.sphinx("html", testroot="indicators/default")
def test_toggle(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-indicators"]
    assert carousel[1]["class"] == ["scbs-carousel-inner"]

    carousel = carousels[1].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-inner"]
    assert len(carousel) == 1

    carousel = carousels[2].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-inner"]
    assert len(carousel) == 1


@pytest.mark.sphinx("html", testroot="indicators/sphinx-conf")
def test_toggle_conf(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-indicators"]
    assert carousel[1]["class"] == ["scbs-carousel-inner"]

    carousel = carousels[1].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-inner"]
    assert len(carousel) == 1

    carousel = carousels[2].find_all(recursive=False)
    assert carousel[0]["class"] == ["scbs-carousel-indicators"]
    assert carousel[1]["class"] == ["scbs-carousel-inner"]
