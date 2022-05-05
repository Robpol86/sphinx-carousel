===============
Getting Started
===============

Install
=======

Install the library with pip:

.. tabbed:: Install from PyPI

    .. code-block:: bash

        pip install sphinx-carousel

.. tabbed:: Install from GitHub

    .. code-block:: bash

        pip install git+https://github.com/Robpol86/sphinx-carousel@main

Enable
======

Add ``sphinx_carousel.carousel`` to your extensions list in your ``conf.py`` file:

.. code-block:: python

    extensions = [
         "sphinx_carousel.carousel",
    ]

Configuration
=============

The following optional configuration settings are available for use in your ``conf.py`` file:

.. option:: carousel_bootstrap_add_css_js

    *Default:* |LABEL_BOOTSTRAP_ADD_CSS_JS|

    Include Bootstrap CSS and javascript files on pages that contain carousels via ``<link>`` and ``<script>`` HTML tags.

    If you're using a Sphinx theme or another Sphinx extension that includes Bootstrap you can set this to ``False`` to avoid
    multiple Bootstrap files from being loaded. You'll also want to look at the :option:`carousel_bootstrap_prefix` option.

.. option:: carousel_bootstrap_prefix

    *Default:* |LABEL_BOOTSTRAP_PREFIX|

    Prefix all CSS classes with this string.

    If you set :option:`carousel_bootstrap_add_css_js` to ``False`` you'll want to set this to an empty string.

.. option:: carousel_show_buttons_on_top

    *Default:* |LABEL_SHOW_BUTTONS_ON_TOP|

    Set :ref:`:show_buttons_on_top: <extended_features:Buttons on Top>` on all carousels by default. Can be disabled on a
    per-usage basis with ``:no_buttons_on_top:``.

.. option:: carousel_show_captions_below

    *Default:* |LABEL_SHOW_CAPTIONS_BELOW|

    Set :ref:`:show_captions_below: <extended_features:Captions Below>` on all carousels by default. Can be disabled on a
    per-usage basis with ``:no_captions_below:``.

.. option:: carousel_show_controls

    *Default:* |LABEL_SHOW_CONTROLS|

    Set :ref:`:show_controls: <native_features:Controls>` on all carousels by default. Can be disabled on a
    per-usage basis with ``:no_controls:``.

.. option:: carousel_show_dark

    *Default:* |LABEL_SHOW_DARK|

    Set :ref:`:show_dark: <native_features:Dark Mode>` on all carousels by default. Can be disabled on a
    per-usage basis with ``:no_dark:``.

.. option:: carousel_show_fade

    *Default:* |LABEL_SHOW_FADE|

    Set :ref:`:show_fade: <native_features:Crossfade>` on all carousels by default. Can be disabled on a
    per-usage basis with ``:no_fade:``.

.. option:: carousel_show_indicators

    *Default:* |LABEL_SHOW_INDICATORS|

    Set :ref:`:show_indicators: <native_features:Indicators>` on all carousels by default. Can be disabled on a
    per-usage basis with ``:no_indicators:``.

.. option:: carousel_show_shadows

    *Default:* |LABEL_SHOW_SHADOWS|

    Set :ref:`:show_shadows: <extended_features:Shadows>` on all carousels by default. Can be disabled on a
    per-usage basis with ``:no_shadows:``.
