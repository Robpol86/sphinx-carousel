"""Tests."""
# pylint: disable=too-many-statements
from textwrap import dedent

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="captions")
def test(carousel: element.Tag):
    """Test."""
    carousel_inner = carousel.find_all("div", ["scbs-carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["scbs-carousel-item"])

    item = carousel_items.pop(0)
    assert item["class"] == ["scbs-carousel-item", "scbs-active"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/a.jpg"
    carousel_caption = img.find_next_sibling()
    assert carousel_caption["class"][0] == "scbs-carousel-caption"
    title = carousel_caption.find_next()
    assert title.name == "h5"
    assert title.get_text(strip=True) == "Just the title."
    assert title.find_next_sibling() is None

    item = carousel_items.pop(0)
    assert item["class"] == ["scbs-carousel-item"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/b.jpg"
    carousel_caption = img.find_next_sibling()
    assert carousel_caption["class"][0] == "scbs-carousel-caption"
    title = carousel_caption.find_next()
    assert title.name == "h5"
    assert title.get_text(strip=True) == "Title and Description"
    description = title.find_next_sibling()
    assert description.name == "p"
    assert description.get_text(strip=True) == dedent(
        """\
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua."""
    )

    item = carousel_items.pop(0)
    assert item["class"] == ["scbs-carousel-item"]
    a_href = item.find_next()
    assert a_href["href"] == "https://imgur.com/c"
    img = a_href.find_next()
    assert img["src"] == "https://i.imgur.com/c.jpg"
    carousel_caption = a_href.find_next_sibling()
    assert carousel_caption["class"][0] == "scbs-carousel-caption"
    title = carousel_caption.find_next()
    assert title.name == "h5"
    assert title.get_text(strip=True) == "Linked with title."
    assert title.find_next_sibling() is None

    item = carousel_items.pop(0)
    assert item["class"] == ["scbs-carousel-item"]
    a_href = item.find_next()
    assert a_href["href"] == "https://imgur.com/d"
    img = a_href.find_next()
    assert img["src"] == "https://i.imgur.com/d.jpg"
    carousel_caption = a_href.find_next_sibling()
    assert carousel_caption["class"][0] == "scbs-carousel-caption"
    title = carousel_caption.find_next()
    assert title.name == "h5"
    assert title.get_text(strip=True) == "Linked with title and description."
    description = title.find_next_sibling()
    assert description.name == "p"
    assert description.get_text(strip=True) == dedent(
        """\
        LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD
        TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA."""
    )

    item = carousel_items.pop(0)
    assert item["class"] == ["scbs-carousel-item"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/e.jpg"
    carousel_caption = img.find_next_sibling()
    assert carousel_caption["class"][0] == "scbs-carousel-caption"
    description = carousel_caption.find_next()
    assert description.name == "p"
    assert description.get_text(strip=True) == "Just the description."

    item = carousel_items.pop(0)
    assert item["class"] == ["scbs-carousel-item"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/f.jpg"
    carousel_caption = img.find_next_sibling()
    assert carousel_caption["class"][0] == "scbs-carousel-caption"
    description = carousel_caption.find_next()
    assert description.get_text(strip=True) == dedent(
        """\
        This is part of the description.

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua."""
    )

    item = carousel_items.pop(0)
    assert item["class"] == ["scbs-carousel-item"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/g.jpg"
    carousel_caption = img.find_next_sibling()
    assert carousel_caption["class"][0] == "scbs-carousel-caption"
    description = carousel_caption.find_next()
    assert description.get_text(strip=True) == dedent(
        """\
        A

        B

        C"""
    )

    assert not carousel_items
