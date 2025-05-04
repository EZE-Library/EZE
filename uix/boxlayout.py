"""
Components/BoxLayout
====================

:class:`~kivy.uix.boxlayout.BoxLayout` class equivalent. Simplifies working
with some widget properties. For example:

BoxLayout
---------

.. code-block:: kv

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

EZEBoxLayout
-----------

.. code-block:: kv

    EZEBoxLayout:
        adaptive_height: True
        eze_bg_color: app.theme_cls.primary_color

Available options are:
----------------------

- adaptive_height_
- adaptive_width_
- adaptive_size_

.. adaptive_height:
adaptive_height
---------------

.. code-block:: kv

    adaptive_height: True

Equivalent

.. code-block:: kv

    size_hint_y: None
    height: self.minimum_height

.. adaptive_width:
adaptive_width
--------------

.. code-block:: kv

    adaptive_width: True

Equivalent

.. code-block:: kv

    size_hint_x: None
    height: self.minimum_width

.. adaptive_size:
adaptive_size
-------------

.. code-block:: kv

    adaptive_size: True

Equivalent

.. code-block:: kv

    size_hint: None, None
    size: self.minimum_size
"""

__all__ = ("EZEBoxLayout",)

from kivy.uix.boxlayout import BoxLayout

from eze.theming import ThemableBehavior
from eze.uix import EZEAdaptiveWidget
from eze.uix.behaviors import DeclarativeBehavior


class EZEBoxLayout(
    DeclarativeBehavior, ThemableBehavior, BoxLayout, EZEAdaptiveWidget
):
    """
    Box layout class.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """
