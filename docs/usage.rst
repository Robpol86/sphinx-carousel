=====
Usage
=====

To use `Bootstrap Carousels <https://getbootstrap.com/docs/4.6/components/carousel/>`_ in a document use the ``carousel``
Sphinx directive to define a carousel, and within it use one or more
`image <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#images>`_ directives or if you want captions
use one or more `figure <https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure>`_ directives. Below is an
example carousel using an image and a figure.

.. note::

    Captions are hidden on mobile viewports. A workaround is to use
    :ref:`show_captions_below <extended_features:Captions Below>`.

.. carousel::
    :show_controls:

    .. image:: https://i.imgur.com/fmJnevTl.jpg

    .. figure:: https://i.imgur.com/fWyn9A2l.jpg

        Title and Description

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. tab-set::

    .. tab-item:: reStructuredText

        .. code-block:: rst

            .. carousel::
                :show_controls:

                .. image:: https://i.imgur.com/fmJnevTl.jpg

                .. figure:: https://i.imgur.com/fWyn9A2l.jpg

                    Title and Description

                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                    eiusmod tempor incididunt ut labore et dolore magna aliqua.

    .. tab-item:: MyST

        .. code-block:: md

            ````{carousel}
            :show_controls:

            ```{image} https://i.imgur.com/fmJnevTl.jpg
            ```

            ```{figure} https://i.imgur.com/fWyn9A2l.jpg
            Title and Description

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            ```
            ````

    .. tab-item:: MyST Code Fences

        .. code-block:: md

            ```{carousel}
            :show_controls:

            :::{image} https://i.imgur.com/fmJnevTl.jpg
            :::

            :::{figure} https://i.imgur.com/fWyn9A2l.jpg
            Title and Description

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            :::
            ```

Linked Images
=============

Since we're using the standard image/figure directives we can use the ``:target:`` option to turn images into hyperlinks:

.. carousel::
    :show_controls:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
        :target: https://google.com

    .. figure:: https://i.imgur.com/fWyn9A2l.jpg
        :target: https://imgur.com

        Title and Description

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. tab-set::

    .. tab-item:: reStructuredText

        .. code-block:: rst

            .. carousel::
                :show_controls:

                .. image:: https://i.imgur.com/fmJnevTl.jpg
                    :target: https://google.com

                .. figure:: https://i.imgur.com/fWyn9A2l.jpg
                    :target: https://imgur.com

                    Title and Description

                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                    eiusmod tempor incididunt ut labore et dolore magna aliqua.

    .. tab-item:: MyST

        .. code-block:: md

            ````{carousel}
            :show_controls:

            ```{image} https://i.imgur.com/fmJnevTl.jpg
            :target: https://google.com
            ```

            ```{figure} https://i.imgur.com/fWyn9A2l.jpg
            :target: https://imgur.com

            Title and Description

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            ```
            ````

    .. tab-item:: MyST Code Fences

        .. code-block:: md

            ```{carousel}
            :show_controls:

            :::{image} https://i.imgur.com/fmJnevTl.jpg
            :target: https://google.com
            :::

            :::{figure} https://i.imgur.com/fWyn9A2l.jpg
            :target: https://imgur.com

            Title and Description

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            :::
            ```

Captions Without Titles
=======================

If you have an image with a short caption it may look better without bold text. Use the ``:no_title:`` option with the
``.. figure-carousel::`` directive to accomplish this:

.. carousel::
    :show_controls:

    .. figure:: https://i.imgur.com/fmJnevTl.jpg

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.

    .. figure-carousel:: https://i.imgur.com/fWyn9A2l.jpg
        :no_title:

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. tab-set::

    .. tab-item:: reStructuredText

        .. code-block:: rst

            .. carousel::
                :show_controls:

                .. figure:: https://i.imgur.com/fmJnevTl.jpg

                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                    eiusmod tempor incididunt ut labore et dolore magna aliqua.

                .. figure-carousel:: https://i.imgur.com/fWyn9A2l.jpg
                    :no_title:

                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                    eiusmod tempor incididunt ut labore et dolore magna aliqua.

    .. tab-item:: MyST

        .. code-block:: md

            ````{carousel}
            :show_controls:

            ```{figure} https://i.imgur.com/fmJnevTl.jpg

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            ```

            ```{figure-carousel} https://i.imgur.com/fWyn9A2l.jpg
            :no_title:

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            ```
            ````

    .. tab-item:: MyST Code Fences

        .. code-block:: md

            ```{carousel}
            :show_controls:

            :::{figure} https://i.imgur.com/fmJnevTl.jpg

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            :::

            :::{figure-carousel} https://i.imgur.com/fWyn9A2l.jpg
            :no_title:

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
            :::
            ```
