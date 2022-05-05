"""Sphinx configuration file."""
# pylint: disable=invalid-name
import time

from sphinx_multi_theme.theme import MultiTheme, Theme

from sphinx_carousel import __version__ as version


# General configuration.
author = "Robpol86"
copyright = f'{time.strftime("%Y")}, {author}'  # pylint: disable=redefined-builtin  # noqa
html_last_updated_fmt = f"%c {time.tzname[time.localtime().tm_isdst]}"
exclude_patterns = []
extensions = [
    "notfound.extension",  # https://sphinx-notfound-page.readthedocs.io
    "sphinx_carousel.carousel",
    "sphinx_copybutton",  # https://sphinx-copybutton.readthedocs.io
    "sphinx_multi_theme.multi_theme",  # https://sphinx-multi-theme.readthedocs.io
    "sphinx_panels",  # https://sphinx-panels.readthedocs.io
    "sphinxext.opengraph",  # https://sphinxext-opengraph.readthedocs.io
]
language = "en"
project = "sphinx-carousel"
pygments_style = "vs"
release = version


# Options for HTML output.
html_copy_source = False
html_theme = MultiTheme(
    [
        Theme("sphinx_rtd_theme", "Read the Docs"),  # https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/
    ]
)


# Extension settings.
multi_theme_print_files = True
ogp_site_name = project
ogp_type = "website"
ogp_use_first_image = True
