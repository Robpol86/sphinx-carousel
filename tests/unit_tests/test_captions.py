"""Tests."""
import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="captions")
def test(carousel: element.Tag):
    """Test.

    <div id="carousel-UUID" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="https://i.imgur.com/a.jpg" ...>
                <div class="carousel-caption d-none d-md-block">
                    <h5>Just the title.</h5>
                </div>
            </div>
            <div class="carousel-item">
                <img src="https://i.imgur.com/b.jpg" ...>
                <div class="carousel-caption d-none d-md-block">
                    <h5>Title and Description</h5>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                        sed do eiusmod tempor incididunt ut labore et dolore
                        magna aliqua.
                    </p>
                </div>
            </div>
            <div class="carousel-item">
                <a href="https://imgur.com/c">
                    <img src="https://i.imgur.com/c.jpg" ...>
                </a>
                <div class="carousel-caption d-none d-md-block">
                    <h5>Linked with title.</h5>
                </div>
            </div>
            <div class="carousel-item">
                <a href="https://imgur.com/d">
                    <img src="https://i.imgur.com/d.jpg" ...>
                </a>
                <div class="carousel-caption d-none d-md-block">
                    <h5>Linked with title and description.</h5>
                    <p>
                        LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT,
                        SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE
                        MAGNA ALIQUA.
                    </p>
                </div>
            </div>
        </div>
    </div>
    """
    carousel_inner = carousel.find_all("div", ["carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["carousel-item"])

    item = carousel_items[0]
    assert item["class"] == ["carousel-item", "active"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/a.jpg"
    carousel_caption = img.find_next_sibling()
    assert carousel_caption["class"][0] == "carousel-caption"
    title = carousel_caption.find_next()
    assert title.text == "Just the title."
    assert title.find_next_sibling() is None

    item = carousel_items[1]
    assert item["class"] == ["carousel-item"]
    img = item.find_next()
    assert img["src"] == "https://i.imgur.com/b.jpg"
    carousel_caption = img.find_next_sibling()
    assert carousel_caption["class"][0] == "carousel-caption"
    title = carousel_caption.find_next()
    assert title.text == "Title and Description"
    description = title.find_next_sibling()
    assert description.text.startswith("Lorem ipsum dolor sit amet")
    assert description.text.endswith("magna aliqua.")

    item = carousel_items[2]
    assert item["class"] == ["carousel-item"]
    a_href = item.find_next()
    assert a_href["href"] == "https://imgur.com/c"
    img = a_href.find_next()
    assert img["src"] == "https://i.imgur.com/c.jpg"
    carousel_caption = a_href.find_next_sibling()
    assert carousel_caption["class"][0] == "carousel-caption"
    title = carousel_caption.find_next()
    assert title.text == "Linked with title."
    assert title.find_next_sibling() is None

    item = carousel_items[3]
    assert item["class"] == ["carousel-item"]
    a_href = item.find_next()
    assert a_href["href"] == "https://imgur.com/d"
    img = a_href.find_next()
    assert img["src"] == "https://i.imgur.com/d.jpg"
    carousel_caption = a_href.find_next_sibling()
    assert carousel_caption["class"][0] == "carousel-caption"
    title = carousel_caption.find_next()
    assert title.text == "Linked with title and description."
    description = title.find_next_sibling()
    assert description.text.startswith("LOREM IPSUM DOLOR SIT AMET")
    assert description.text.endswith("MAGNA ALIQUA.")
