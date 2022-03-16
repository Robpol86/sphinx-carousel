"""Tests."""
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="controls")
def test(carousels: List[element.Tag]):
    """Test."""
    carousel = list(carousels[0])

    assert carousel[0]["class"] == ["carousel-inner"]

    assert carousel[1]["class"] == ["carousel-control-prev"]
    assert carousel[1]["data-bs-slide"] == "prev"
    spans = list(carousel[1])
    assert spans[0]["class"] == ["carousel-control-prev-icon"]
    assert spans[1]["class"] == ["visually-hidden"]
    assert spans[1].text == "Previous"

    assert carousel[2]["class"] == ["carousel-control-next"]
    assert carousel[2]["data-bs-slide"] == "next"
    spans = list(carousel[2])
    assert spans[0]["class"] == ["carousel-control-next-icon"]
    assert spans[1]["class"] == ["visually-hidden"]
    assert spans[1].text == "Next"


@pytest.mark.sphinx("html", testroot="controls")
def test_uuid_match(carousel: element.Tag):
    """Test."""
    carousel_main_id = carousel["id"]
    control_target = carousel.find_next("button")["data-bs-target"]
    assert control_target == f"#{carousel_main_id}"


@pytest.mark.sphinx("html", testroot="controls")
def test_toggle(carousels: List[element.Tag]):
    """Test."""
    carousel = list(carousels[0])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert carousel[1]["class"] == ["carousel-control-prev"]
    assert carousel[2]["class"] == ["carousel-control-next"]

    carousel = list(carousels[1])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert len(carousel) == 1

    carousel = list(carousels[2])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert len(carousel) == 1


@pytest.mark.sphinx("html", testroot="controls-conf")
def test_toggle_conf(carousels: List[element.Tag]):
    """Test."""
    carousel = list(carousels[0])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert carousel[1]["class"] == ["carousel-control-prev"]
    assert carousel[2]["class"] == ["carousel-control-next"]

    carousel = list(carousels[1])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert len(carousel) == 1

    carousel = list(carousels[2])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert carousel[1]["class"] == ["carousel-control-prev"]
    assert carousel[2]["class"] == ["carousel-control-next"]
