===============
Native Features
===============

Below are options that expose native features of Bootstrap carousels.

Controls
========

`Official documentation for this feature <https://getbootstrap.com/docs/5.1/components/carousel/#with-controls>`__

Display previous and next controls overlayed on top of the carousel by using ``:show_controls:``. Enable this by default with
:option:`carousel_show_controls`.

.. carousel::
    :show_controls:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :show_controls:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. image:: https://i.imgur.com/fWyn9A2l.jpg

Indicators
==========

`Official documentation for this feature <https://getbootstrap.com/docs/5.1/components/carousel/#with-indicators>`__

Display image indicators overlayed on top of the carousel by using ``:show_indicators:``. Enable this by default with
:option:`carousel_show_indicators`.

.. carousel::
    :show_indicators:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :show_indicators:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. image:: https://i.imgur.com/fWyn9A2l.jpg

Crossfade
=========

`Official documentation for this feature <https://getbootstrap.com/docs/5.1/components/carousel/#crossfade>`__

Animate slides with a fade transition instead of a slide by using ``:show_fade:``. Enable this by default with
:option:`carousel_show_fade`.

.. carousel::
    :show_controls:
    :show_fade:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :show_controls:
        :show_fade:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. image:: https://i.imgur.com/fWyn9A2l.jpg

Dark Mode
=========

`Official documentation for this feature <https://getbootstrap.com/docs/5.1/components/carousel/#dark-variant>`__

Show darker :ref:`controls <native_features:Controls>`, :ref:`indicators <native_features:Indicators>`, and captions by using
``:show_dark:``. Enable this by default with :option:`carousel_show_dark`.

.. carousel::
    :show_controls:
    :show_indicators:
    :show_dark:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. figure:: https://i.imgur.com/fWyn9A2l.jpg

        Title and Description

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. code-block:: rst

    .. carousel::
        :show_controls:
        :show_indicators:
        :show_dark:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. figure:: https://i.imgur.com/fWyn9A2l.jpg

            Title and Description

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.

Additional Options
==================

The following are `additional options <https://getbootstrap.com/docs/5.1/components/carousel/#options>`_ supported by
Bootstrap carousels.

Interval
--------

Can be an integer or "false" to disable automatic cycling/animation.

.. carousel::
    :data-bs-interval: false
    :show_controls:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :data-bs-interval: false
        :show_controls:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. image:: https://i.imgur.com/fWyn9A2l.jpg

Keyboard, Touch, Wrap
---------------------

.. carousel::
    :data-bs-keyboard: false
    :data-bs-touch: false
    :data-bs-wrap: false
    :show_controls:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :data-bs-keyboard: false
        :data-bs-touch: false
        :data-bs-wrap: false
        :show_controls:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. image:: https://i.imgur.com/fWyn9A2l.jpg

Pause, Ride
-----------

.. carousel::
    :data-bs-pause: false
    :data-bs-ride: false
    :show_controls:

    .. image:: https://i.imgur.com/fmJnevTl.jpg
    .. image:: https://i.imgur.com/fWyn9A2l.jpg

.. code-block:: rst

    .. carousel::
        :data-bs-pause: false
        :data-bs-ride: false
        :show_controls:

        .. image:: https://i.imgur.com/fmJnevTl.jpg
        .. image:: https://i.imgur.com/fWyn9A2l.jpg
