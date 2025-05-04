"""
Components/RecycleView
======================

.. versionadded:: 1.0.0

:class:`~kivy.uix.recycleview.RecycleView` class equivalent. Simplifies working
with some widget properties. For example:

RecycleView
-----------

.. code-block:: kv

    RecycleView:

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

EZERecycleView
-------------

.. code-block:: kv

    EZERecycleView:
        eze_bg_color: app.theme_cls.primary_color
"""

__all__ = ("EZERecycleView",)

from kivy.uix.recycleview import RecycleView

from eze.theming import ThemableBehavior
from eze.uix import EZEAdaptiveWidget
from eze.uix.behaviors import DeclarativeBehavior


class EZERecycleView(
    DeclarativeBehavior, ThemableBehavior, RecycleView, EZEAdaptiveWidget
):
    """
    Recycle view class. For more information, see in the
    :class:`~kivy.uix.recycleview.RecycleView` class documentation.
    """
