=====
Usage
=====

.. carousel::
    :data-bs-interval: false
    :show_controls:
    :show_indicators:
    :show_captions_below:
    :show_buttons_on_top:
    :show_shadows:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
        :target: https://i.imgur.com/fmJnevT.jpg
    .. image:: https://i.imgur.com/ppGH90Jl.jpg
    .. figure:: https://i.imgur.com/fWyn9A2l.jpg

        An Example Image

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
        aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
        occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

TODO update below.

.. tabbed:: reStructuredText

    .. code-block:: rst

        .. carousel::

            .. image:: https://i.imgur.com/fmJnevTl.jpg
            .. image:: https://i.imgur.com/ppGH90Jl.jpg
            .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. tabbed:: MyST Markdown

    .. code-block:: md

        ````{carousel}

        ```{image} https://i.imgur.com/fmJnevTl.jpg
        ```
        ```{image} https://i.imgur.com/ppGH90Jl.jpg
        ```
        ```{image} https://i.imgur.com/fWyn9A2l.jpg
        ```
        ````
