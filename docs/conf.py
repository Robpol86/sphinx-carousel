"""Sphinx configuration file."""
# pylint: disable=invalid-name
import time

from sphinx_multi_theme.theme import MultiTheme, Theme

from sphinx_carousel import __version__ as version, carousel


# General configuration.
author = "Robpol86"
copyright = f'{time.strftime("%Y")}, {author}'  # pylint: disable=redefined-builtin  # noqa
html_last_updated_fmt = f"%c {time.tzname[time.localtime().tm_isdst]}"
exclude_patterns = []
extensions = [
    "notfound.extension",  # https://sphinx-notfound-page.readthedocs.io
    "sphinx.ext.autosectionlabel",  # https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html
    "sphinx_carousel.carousel",
    "sphinx_copybutton",  # https://sphinx-copybutton.readthedocs.io
    "sphinx_design",  # https://sphinx-design.readthedocs.io
    "sphinx_multi_theme.multi_theme",  # https://sphinx-multi-theme.readthedocs.io
    "sphinxext.opengraph",  # https://sphinxext-opengraph.readthedocs.io
]
language = "en"
project = "sphinx-carousel"
pygments_style = "vs"
release = version
rst_epilog = f"""
.. |LABEL_BOOTSTRAP_ADD_CSS_JS| replace:: :guilabel:`{carousel.CONF_DEFAULT_BOOTSTRAP_ADD_CSS_JS}`
.. |LABEL_BOOTSTRAP_PREFIX| replace:: :guilabel:`{carousel.CONF_DEFAULT_BOOTSTRAP_PREFIX}`
.. |LABEL_SHOW_BUTTONS_ON_TOP| replace:: :guilabel:`{carousel.CONF_DEFAULT_SHOW_BUTTONS_ON_TOP}`
.. |LABEL_SHOW_CAPTIONS_BELOW| replace:: :guilabel:`{carousel.CONF_DEFAULT_SHOW_CAPTIONS_BELOW}`
.. |LABEL_SHOW_CONTROLS| replace:: :guilabel:`{carousel.CONF_DEFAULT_SHOW_CONTROLS}`
.. |LABEL_SHOW_DARK| replace:: :guilabel:`{carousel.CONF_DEFAULT_SHOW_DARK}`
.. |LABEL_SHOW_FADE| replace:: :guilabel:`{carousel.CONF_DEFAULT_SHOW_FADE}`
.. |LABEL_SHOW_INDICATORS| replace:: :guilabel:`{carousel.CONF_DEFAULT_SHOW_INDICATORS}`
.. |LABEL_SHOW_SHADOWS| replace:: :guilabel:`{carousel.CONF_DEFAULT_SHOW_SHADOWS}`
"""


# Options for HTML output.
html_copy_source = False
html_theme = MultiTheme(
    [
        Theme("sphinx_rtd_theme", "Read the Docs"),
        Theme("pydata_sphinx_theme", "PyData Sphinx Theme"),
        Theme("sphinx_book_theme", "Sphinx Book Theme"),
    ]
)


# Extension settings.
autosectionlabel_prefix_document = True
multi_theme_print_files = True
ogp_site_name = project
ogp_type = "website"
ogp_use_first_image = True
