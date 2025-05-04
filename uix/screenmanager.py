"""
Components/ScreenManager
========================

.. versionadded:: 1.0.0

:class:`~kivy.uix.screenmanager.ScreenManager` class equivalent.
If you want to use Hero animations you need to use
:class:`~eze.uix.screenmanager.EZEScreenManager` not
:class:`~kivy.uix.screenmanager.ScreenManager` class.

Transition
----------

:class:`~eze.uix.screenmanager.EZEScreenManager` class supports the following
transitions:

- :class:`~eze.uix.transition.EZEFadeSlideTransition`
- :class:`~eze.uix.transition.EZESlideTransition`
- :class:`~eze.uix.transition.EZESwapTransition`

You need to use the :class:`~eze.uix.screenmanager.EZEScreenManager` class
when you want to use hero animations on your screens. If you don't need hero
animation use the :class:`~kivy.uix.screenmanager.ScreenManager` class.
"""

from kivy import Logger
from kivy.clock import Clock
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager

from eze.uix.behaviors import DeclarativeBehavior
from eze.uix.hero import EZEHeroFrom


class EZEScreenManager(DeclarativeBehavior, ScreenManager):
    """
    Screen manager. This is the main class that will control your
    :class:`~eze.uix.screen.EZEScreen` stack and memory.

    For more
    information, see in the :class:`~kivy.uix.screenmanager.ScreenManager`
    class documentation.
    """

    current_hero = StringProperty(None, deprecated=True)
    """
    The name of the current tag for the :class:`~eze.uix.hero.EZEHeroFrom`
    and :class:`~eze.uix.hero.EZEHeroTo` objects that will be animated when
    animating the transition between screens.

    .. deprecated:: 1.1.0
        Use :attr:`current_heroes` attribute instead.

    See the `Hero <https://eze.readthedocs.io/en/latest/components/hero/>`_
    module documentation for more information about creating and using Hero
    animations.

    :attr:`current_hero` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    current_heroes = ListProperty()
    """
    A list of names (tags) of heroes that need to be animated when moving
    to the next screen.

    .. versionadded:: 1.1.0

    :attr:`current_heroes` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    # Collection of `EZEHeroFrom` objects on all screens of the current
    # screen manager.
    _heroes_data = ListProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.check_transition)

    def check_transition(self, *args) -> None:
        """Sets the default type transition."""

        from eze.uix.transition.transition import EZETransitionBase

        if not issubclass(self.transition.__class__, EZETransitionBase):
            from eze.uix.transition import EZESlideTransition

            self.transition = EZESlideTransition()

    def get_hero_from_widget(self) -> list:
        """
        Get a list of :class:`~eze.uix.hero.EZEHeroFrom` objects according
        to the tag names specified in the :attr:`~current_heroes` list.
        """

        hero_from_widget = []

        for name_hero in self.current_heroes:
            for hero_widget in self._heroes_data:
                if isinstance(hero_widget, EZEHeroFrom) or issubclass(
                    hero_widget.__class__, EZEHeroFrom
                ):
                    if hero_widget.tag == name_hero:
                        hero_from_widget.append(hero_widget)

        return hero_from_widget

    def on_current_hero(self, instance, value: str) -> None:
        """
        Called when the value of the :attr:`current_hero` attribute changes.
        """

        Logger.warning(
            "EZE: "
            "`eze/uix/screenmanager.EZEScreenManager.current_hero` "
            "attribute is deprecated. "
            "Use `eze/uix/screenmanager.EZScreenManager.current_heroes` "
            "attribute instead."
        )
        if value:
            self.current_heroes = [value]
        else:
            self.current_heroes = []

    def add_widget(self, widget, *args, **kwargs):
        super().add_widget(widget, *args, **kwargs)
        Clock.schedule_once(lambda x: self._create_heroes_data(widget))

    # TODO: Add a method to delete an object from the arrt:`_heroes_data`
    #  collection when deleting an object using the `remove_widget` method.

    def _create_heroes_data(self, widget):
        def find_hero_widget(child_widget):
            widget_hero = None

            for w in child_widget.children:
                if isinstance(w, EZEHeroFrom) or issubclass(
                    w.__class__, EZEHeroFrom
                ):
                    self._heroes_data.append(w)
                find_hero_widget(w)

            return widget_hero

        for child in widget.children:
            if isinstance(child, EZEHeroFrom) or issubclass(
                child.__class__, EZEHeroFrom
            ):
                self._heroes_data.append(child)
            else:
                find_hero_widget(child)
