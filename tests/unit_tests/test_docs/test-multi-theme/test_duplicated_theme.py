"""Tests."""
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

pytestmark = pytest.mark.skipif("not hasattr(os, 'fork')", reason="Unsupported platform: no os.fork()")


@pytest.mark.sphinx("html", testroot="multi-theme/duplicated-theme")
def test(outdir: Path):
    """Test."""
    # Primary theme.
    for file_ in ("index.html", "hello.html"):
        html = BeautifulSoup((outdir / file_).read_text(encoding="utf8"), "html.parser")
        stylesheets = [link["href"] for link in html.find_all("link", rel="stylesheet")]
        assert "_static/alabaster.css" in stylesheets

    # Secondary themes.
    for file_ in ("index.html", "hello.html"):
        for suffix in ("", "2", "3"):
            html = BeautifulSoup((outdir / f"theme_alabaster{suffix}" / file_).read_text(encoding="utf8"), "html.parser")
            stylesheets = [link["href"] for link in html.find_all("link", rel="stylesheet")]
            assert "_static/alabaster.css" in stylesheets
