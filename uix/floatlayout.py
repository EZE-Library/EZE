"""
Components/FloatLayout
======================

:class:`~kivy.uix.floatlayout.FloatLayout` class equivalent. Simplifies working
with some widget properties. For example:

FloatLayout
-----------

.. code-block:: kv

    FloatLayout:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [25, 0, 0, 0]

EZEFloatLayout
-------------

.. code-block:: kv

    EZEFloatLayout:
        radius: [25, 0, 0, 0]
        eze_bg_color: app.theme_cls.primary_color

.. Warning:: For a :class:`~kivy.uix.floatlayout.FloatLayout`, the
    ``minimum_size`` attributes are always 0, so you cannot use
    ``adaptive_size`` and related options.
"""

from kivy.uix.floatlayout import FloatLayout

from eze.theming import ThemableBehavior
from eze.uix import EZEAdaptiveWidget
from eze.uix.behaviors import DeclarativeBehavior


class EZEFloatLayout(
    DeclarativeBehavior, ThemableBehavior, FloatLayout, EZEAdaptiveWidget
):
    """
    Float layout class. For more information, see in the
    :class:`~kivy.uix.floatlayout.FloatLayout` class documentation.
    """
