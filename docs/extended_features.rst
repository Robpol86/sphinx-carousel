=================
Extended Features
=================

These options are for additional features that aren't part of the standard Bootstrap carousels feature set.

Captions Below
==============

Display figure captions below the image instead of overlayed on top by using ``:show_captions_below:``. Enable this by
default with :option:`carousel_show_captions_below`.

.. carousel::
    :show_captions_below:
    :show_controls:

    .. figure:: https://i.imgur.com/fmJnevTl.jpg

        Title and Description

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.

    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :show_captions_below:
        :show_controls:

        .. figure:: https://i.imgur.com/fmJnevTl.jpg

            Title and Description

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua.

        .. image:: https://i.imgur.com/fWyn9A2l.jpg

Shadows
=======

Display a shadow around :ref:`controls <native_features:Controls>` and :ref:`indicators <native_features:Indicators>` to
improve their visibility by using ``:show_shadows:``. Enable this by default with :option:`carousel_show_shadows`.

.. carousel::
    :show_controls:
    :show_indicators:
    :show_shadows:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :show_controls:
        :show_indicators:
        :show_shadows:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. image:: https://i.imgur.com/fWyn9A2l.jpg

With Dark Mode
--------------

Compatible with :ref:`dark mode <native_features:Dark Mode>`.

.. carousel::
    :show_controls:
    :show_indicators:
    :show_dark:
    :show_shadows:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :show_controls:
        :show_indicators:
        :show_dark:
        :show_shadows:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. image:: https://i.imgur.com/fWyn9A2l.jpg

Buttons on Top
==============

Move :ref:`controls <native_features:Controls>` and :ref:`indicators <native_features:Indicators>` to the top of the
carousel by using ``:show_buttons_on_top:``. Enable this by default with :option:`carousel_show_buttons_on_top`.

This is a work around for the annoyance of controls and indicators moving when captions are used or when images with
different aspect ratios are used in one carousel.

.. carousel::
    :show_controls:
    :show_indicators:
    :show_buttons_on_top:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :show_controls:
        :show_indicators:
        :show_buttons_on_top:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. image:: https://i.imgur.com/fWyn9A2l.jpg
