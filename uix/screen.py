"""
Components/Screen
=================

:class:`~kivy.uix.screenmanager.Screen` class equivalent. Simplifies working
with some widget properties. For example:

Screen
------

.. code-block:: kv

    Screen:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [25, 0, 0, 0]

EZEScreen
--------

.. code-block:: kv

    EZEScreen:
        radius: [25, 0, 0, 0]
        eze_bg_color: app.theme_cls.primary_color
"""

from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import Screen

from eze.theming import ThemableBehavior
from eze.uix import EZEAdaptiveWidget
from eze.uix.behaviors import DeclarativeBehavior
from eze.uix.hero import EZEHeroTo


class MDScreen(DeclarativeBehavior, ThemableBehavior, Screen, EZEAdaptiveWidget):
    """
    Screen is an element intended to be used with a
    :class:`~eze.uix.screenmanager.EZEScreenManager`. For more information,
    see in the :class:`~kivy.uix.screenmanager.Screen` class documentation.
    """

    hero_to = ObjectProperty(deprecated=True)
    """
    Must be a :class:`~eze.uix.hero.EZEHeroTo` class.

    See the documentation of the
    `EZEHeroTo <https://kivymd.readthedocs.io/en/latest/components/hero/>`_
    widget for more detailed information.

    .. deprecated:: 1.0.0
        Use attr:`heroes_to` attribute instead.

    :attr:`hero_to` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    heroes_to = ListProperty()
    """
    Must be a list of :class:`~eze.uix.hero.EZEHeroTo` class.

    .. versionadded:: 1.0.0

    :attr:`heroes_to` is an :class:`~kivy.properties.LiatProperty`
    and defaults to `[]`.
    """

    def on_hero_to(self, screen, widget: EZEHeroTo) -> None:
        """Called when the value of the :attr:`hero_to` attribute changes."""

        if not isinstance(widget, EZEHeroTo) or not issubclass(
            widget.__class__, EZEHeroTo
        ):
            raise TypeError(
                f"The `{widget}` widget must be an `eze.uix.hero.EZEHeroTo` "
                f"class or inherited from this class"
            )
        self.heroes_to = [widget]
