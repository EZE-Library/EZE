"""
Components/ScrollView
=====================

.. versionadded:: 1.0.0

:class:`~kivy.uix.scrollview.ScrollView` class equivalent. Simplifies working
with some widget properties. For example:

ScrollView
----------

.. code-block:: kv

    ScrollView:

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

EZEScrollView
------------

.. code-block:: kv

    EZEScrollView:
        eze_bg_color: app.theme_cls.primary_color
"""

__all__ = ("EZEScrollView",)

from kivy.uix.scrollview import ScrollView

from eze.uix.behaviors import (
    DeclarativeBehavior,
    SpecificBackgroundColorBehavior,
)


class EZEScrollView(
    DeclarativeBehavior, SpecificBackgroundColorBehavior, ScrollView
):
    """
    ScrollView class. For more information, see in the
    :class:`~kivy.uix.scrollview.ScrollView` class documentation.
    """
