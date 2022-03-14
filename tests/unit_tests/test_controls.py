"""Tests."""
import pytest
from bs4 import BeautifulSoup


@pytest.mark.sphinx("html", testroot="controls")
def test(index_html: BeautifulSoup):
    """Test."""
    carousel = list(index_html.find_all("div", ["carousel", "slide"])[0])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert len(carousel) == 1

    carousel = list(index_html.find_all("div", ["carousel", "slide"])[1])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert len(carousel) == 1

    carousel = list(index_html.find_all("div", ["carousel", "slide"])[2])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert carousel[1]["class"] == ["carousel-control-prev"]
    assert carousel[2]["class"] == ["carousel-control-next"]


@pytest.mark.sphinx("html", testroot="controls-conf")
def test_conf(index_html: BeautifulSoup):
    """Test."""
    carousel = list(index_html.find_all("div", ["carousel", "slide"])[0])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert carousel[1]["class"] == ["carousel-control-prev"]
    assert carousel[2]["class"] == ["carousel-control-next"]

    carousel = list(index_html.find_all("div", ["carousel", "slide"])[1])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert len(carousel) == 1

    carousel = list(index_html.find_all("div", ["carousel", "slide"])[2])
    assert carousel[0]["class"] == ["carousel-inner"]
    assert carousel[1]["class"] == ["carousel-control-prev"]
    assert carousel[2]["class"] == ["carousel-control-next"]
