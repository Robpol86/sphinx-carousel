.. _install:

============
Installation
============

To install the library:

.. tabbed:: Install from PyPI

    .. code-block:: bash

        pip install sphinx-carousel

.. tabbed:: Install from GitHub

    .. code-block:: bash

        pip install git+https://github.com/Robpol86/sphinx-carousel@main

Once the package is installed add ``sphinx_carousel.carousel`` to your extensions list in your ``conf.py`` file.

.. code-block:: python

    # conf.py
    extensions = [
         # ... other extensions here
         "sphinx_carousel.carousel",
    ]
