# sphinx-carousel

[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]

[github-ci]: https://github.com/Robpol86/sphinx-carousel/actions/workflows/ci.yml/badge.svg?branch=main
[github-link]: https://github.com/Robpol86/sphinx-carousel/actions/workflows/ci.yml
[codecov-badge]: https://codecov.io/gh/Robpol86/sphinx-carousel/branch/main/graph/badge.svg
[codecov-link]: https://codecov.io/gh/Robpol86/sphinx-carousel
[rtd-badge]: https://readthedocs.org/projects/sphinx-carousel/badge/?version=latest
[rtd-link]: https://sphinx-carousel.readthedocs.io/en/latest/?badge=latest
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
[pypi-badge]: https://img.shields.io/pypi/v/sphinx-carousel.svg
[pypi-link]: https://pypi.org/project/sphinx-carousel

A Sphinx extension for creating slideshows using
[Bootstrap 5 Carousels](https://getbootstrap.com/docs/5.1/components/carousel/).

📖 See the documentation at https://sphinx-carousel.readthedocs.io

## Install

Requires Python 3.6 or greater and Sphinx 4.0 or greater.

```shell
pip install sphinx-carousel
```

## Example

```python
# conf.py
extensions = [
    "sphinx_carousel.carousel",
]
```

```rst
===============
An RST Document
===============

.. carousel::

    .. image:: https://i.imgur.com/fmJnevTl.jpg
        :target: https://i.imgur.com/fmJnevT.jpg
    .. image:: https://i.imgur.com/ppGH90Jl.jpg
    .. figure:: https://i.imgur.com/fWyn9A2l.jpg

        An Example Image

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
        labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
        esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
        in culpa qui officia deserunt mollit anim id est laborum.

```
