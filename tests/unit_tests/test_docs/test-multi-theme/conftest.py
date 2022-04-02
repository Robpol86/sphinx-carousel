"""pytest fixtures."""
from pathlib import Path

import pytest
from bs4 import BeautifulSoup


@pytest.fixture()
def hello_html(outdir: Path) -> BeautifulSoup:
    """Read and parse generated test hello.html."""
    text = (outdir / "hello.html").read_text(encoding="utf8")
    return BeautifulSoup(text, "html.parser")
