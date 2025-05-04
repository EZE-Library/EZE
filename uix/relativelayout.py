"""
Components/RelativeLayout
=========================

:class:`~kivy.uix.relativelayout.RelativeLayout` class equivalent.
Simplifies working with some widget properties. For example:

RelativeLayout
--------------

.. code-block:: kv

    RelativeLayout:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: (0, 0)
                size: self.size
                radius: [25, ]

EZERelativeLayout
----------------

.. code-block:: kv

    EZERelativeLayout:
        radius: [25, ]
        eze_bg_color: app.theme_cls.primary_color
"""

from kivy.uix.relativelayout import RelativeLayout

from eze.theming import ThemableBehavior
from eze.uix import EZEAdaptiveWidget
from eze.uix.behaviors import DeclarativeBehavior


class EZERelativeLayout(
    DeclarativeBehavior, ThemableBehavior, RelativeLayout, EZEAdaptiveWidget
):
    """
    Relative layout class. For more information, see in the
    :class:`~kivy.uix.relativelayout.RelativeLayout` class documentation.
    """
