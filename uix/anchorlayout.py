"""
Components/AnchorLayout
=======================

.. versionadded:: 1.0.0

:class:`~kivy.uix.anchorlayout.AnchorLayout` class equivalent. Simplifies working
with some widget properties. For example:

AnchorLayout
------------

.. code-block:: kv

    AnchorLayout:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

EZEAnchorLayout
--------------

.. code-block:: kv

    EZEAnchorLayout:
        eze_bg_color: app.theme_cls.primary_color
"""

__all__ = ("EZEAnchorLayout",)

from kivy.uix.anchorlayout import AnchorLayout

from eze.theming import ThemableBehavior
from eze.uix import EZEAdaptiveWidget
from eze.uix.behaviors import DeclarativeBehavior


class EZEAnchorLayout(
    DeclarativeBehavior, ThemableBehavior, AnchorLayout, EZEAdaptiveWidget
):
    """
    Anchor layout class. For more information, see in the
    :class:`~kivy.uix.anchorlayout.AnchorLayout` class documentation.
    """
