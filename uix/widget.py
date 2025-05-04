"""
Components/Widget
=================

:class:`~kivy.uix.widget.Widget` class equivalent. Simplifies working
with some widget properties. For example:

Widget
------

.. code-block:: kv

    Widget:
        size_hint: .5, None
        height: self.width

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [self.height / 2,]

EZEWidget
--------

.. code-block:: kv

    EZEWidget:
        size_hint: .5, None
        height: self.width
        radius: self.height / 2
        eze_bg_color: app.theme_cls.primary_color
"""

__all__ = ("EZEWidget",)

from kivy.uix.widget import Widget

from eze.theming import ThemableBehavior
from eze.uix import EZEAdaptiveWidget
from eze.uix.behaviors import DeclarativeBehavior


class EZEWidget(DeclarativeBehavior, ThemableBehavior, EZEAdaptiveWidget, Widget):
    """
    See :class:`~kivy.uix.Widget` class documentation for more information.

    .. versionadded:: 1.0.0
    """
