"""Tests."""
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

pytestmark = pytest.mark.skipif("not hasattr(os, 'fork')", reason="Unsupported platform: no os.fork()")


@pytest.mark.sphinx("html", testroot="multi-theme/subdirs")
def test(outdir: Path):
    """Test."""
    # Primary theme.
    html = BeautifulSoup((outdir / "index.html").read_text(encoding="utf8"), "html.parser")
    stylesheets = [link["href"] for link in html.find_all("link", rel="stylesheet")]
    assert "_static/alabaster.css" in stylesheets
    html = BeautifulSoup((outdir / "sub" / "hello.html").read_text(encoding="utf8"), "html.parser")
    stylesheets = [link["href"] for link in html.find_all("link", rel="stylesheet")]
    assert "../_static/alabaster.css" in stylesheets

    # Secondary theme.
    html = BeautifulSoup((outdir / "theme_classic" / "index.html").read_text(encoding="utf8"), "html.parser")
    stylesheets = [link["href"] for link in html.find_all("link", rel="stylesheet")]
    assert "_static/classic.css" in stylesheets
    html = BeautifulSoup((outdir / "theme_classic" / "sub" / "hello.html").read_text(encoding="utf8"), "html.parser")
    stylesheets = [link["href"] for link in html.find_all("link", rel="stylesheet")]
    assert "../_static/classic.css" in stylesheets


def test_broken_links():
    """Spin up an HTTP server and search for broken links or stylesheets."""
    # TODO: https://brianli.com/2021/06/how-to-find-broken-links-with-python/
    pytest.skip("TODO")
