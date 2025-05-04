"""
Components/SliverAppbar
=======================

.. versionadded:: 1.0.0

.. rubric:: EZESliverAppbar is a Material Design widget in KivyMD which gives
    scrollable or collapsible
    `EZETopAppBar <https://kivymd.readthedocs.io/en/latest/components/toolbar/>`_

.. note:: This widget is a modification of the
    `silverappbar.py <https://github.com/kivymd-extensions/akivymd/blob/main/kivymd_extensions/akivymd/uix/silverappbar.py>`_ module.

Usage
-----

.. code-block:: kv

    EZEScreen:

        EZESliverAppbar:

            EZESliverAppbarHeader:

                # Custom content.
                ...

            # Custom list.
            EZESliverAppbarContent:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-usage.png
    :align: center

Example
-------

.. code-block:: python

    from kivy.lang.builder import Builder

    from eze.app import EZEApp
    from eze.uix.card import EZECard

    KV = '''
    <CardItem>
        size_hint_y: None
        height: "86dp"
        padding: "4dp"
        radius: 12

        FitImage:
            source: "avatar.jpg"
            radius: root.radius
            size_hint_x: None
            width: root.height

        EZEBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            spacing: "6dp"
            padding: "12dp", 0, 0, 0
            pos_hint: {"center_y": .5}

            EZELabel:
                text: "Title text"
                font_style: "H5"
                bold: True
                adaptive_height: True

            EZELabel:
                text: "Subtitle text"
                theme_text_color: "Hint"
                adaptive_height: True


    EZEScreen:

        EZESliverAppbar:
            background_color: "2d4a50"

            EZESliverAppbarHeader:

                EZERelativeLayout:

                    FitImage:
                        source: "bg.jpg"

            EZESliverAppbarContent:
                id: content
                orientation: "vertical"
                padding: "12dp"
                spacing: "12dp"
                adaptive_height: True
    '''


    class CardItem(EZECard):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.elevation = 1


    class Example(EZEApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for x in range(10):
                self.root.ids.content.add_widget(CardItem())


    Example().run()
"""


__all__ = ("EZESliverAppbar", "EZESliverAppbarHeader", "EZESliverAppbarContent")

import os
from typing import Union

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    VariableListProperty,
)

from eze import uix_path
from eze.uix.boxlayout import EZEBoxLayout
from eze.uix.toolbar import EZETopAppBar

with open(
    os.path.join(uix_path, "sliverappbar", "sliverappbar.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class EZESliverAppbarException(Exception):
    pass


class EZESliverAppbarContent(EZEBoxLayout):
    """
    Implements a box for a scrollable list of custom items.

    For more information, see in the
    :class:`~eze.uix.boxlayout.MDBoxLayout` class documentation.
    """

    eze_bg_color = ColorProperty([0, 0, 0, 0])
    """
    See :attr:`~eze.uix.sliverappbar.sliverappbar.EZESliverAppbar.background_color`.

    :attr:`eze_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_bg_color)

    def set_bg_color(self, interval: Union[int, float]) -> None:
        if self.eze_bg_color == [0, 0, 0, 0]:
            self.eze_bg_color = self.theme_cls.bg_normal


class EZESliverAppbarHeader(EZEBoxLayout):
    """
    Sliver app bar header class.

    For more information, see in the
    :class:`~eze.uix.boxlayout.EZEBoxLayout` class documentation.
    """


class EZESliverAppbar(EZEBoxLayout):
    """
    Sliver app bar class.

    For more information, see in the
    :class:`~eze.uix.boxlayout.EZEBoxLayout` class documentation.

    :Events:
        :attr:`on_scroll_content`
            Called when the list of custom content is being scrolled.
    """

    toolbar_cls = ObjectProperty()
    """
    Must be an object of the :class:`~eze.uix.toolbar.toolbar.EZETopAppBar' class.
    See :class:`~eze.uix.toolbar.toolbar.EZETopAppBar` class documentation
    for more information.

    By default, EZESliverAppbar widget uses the EZETopAppBar class with no
    parameters.

    .. code-block:: python

        from kivy.lang.builder import Builder

        from eze.uix.card import EZECard
        from eze.uix.toolbar import EZETopAppBar

        KV = '''
        #:import SliverToolbar __main__.SliverToolbar


        <CardItem>
            size_hint_y: None
            height: "86dp"
            padding: "4dp"
            radius: 12

            FitImage:
                source: "avatar.jpg"
                radius: root.radius
                size_hint_x: None
                width: root.height

            EZEBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "6dp"
                padding: "12dp", 0, 0, 0
                pos_hint: {"center_y": .5}

                EZELabel:
                    text: "Title text"
                    font_style: "H5"
                    bold: True
                    adaptive_height: True

                EZELabel:
                    text: "Subtitle text"
                    theme_text_color: "Hint"
                    adaptive_height: True


        EZEScreen:

            EZESliverAppbar:
                background_color: "2d4a50"
                toolbar_cls: SliverToolbar()

                EZESliverAppbarHeader:

                    EZERelativeLayout:

                        FitImage:
                            source: "bg.jpg"

                EZESliverAppbarContent:
                    id: content
                    orientation: "vertical"
                    padding: "12dp"
                    spacing: "12dp"
                    adaptive_height: True
        '''


        class CardItem(EZECard):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.elevation = 1


        class SliverToolbar(EZETopAppBar):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.shadow_color = (0, 0, 0, 0)
                self.type_height = "medium"
                self.headline_text = "Headline medium"
                self.left_action_items = [["arrow-left", lambda x: x]]
                self.right_action_items = [
                    ["attachment", lambda x: x],
                    ["calendar", lambda x: x],
                    ["dots-vertical", lambda x: x],
                ]


        class Example(EZEApp):
            def build(self):
                self.theme_cls.material_style = "M3"
                return Builder.load_string(KV)

            def on_start(self):
                for x in range(10):
                    self.root.ids.content.add_widget(CardItem())


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-toolbar-cls.gif
        :align: center

    :attr:`toolbar_cls` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    background_color = ColorProperty(None)
    """
    Background color of toolbar in (r, g, b, a) or string format.

    .. code-block:: kv

        EZESliverAppbar:
            background_color: "2d4a50"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-background-color.png
        :align: center

    :attr:`background_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    max_height = NumericProperty(Window.height / 2)
    """
    Distance from top of screen to start of custom list content.

    .. code-block:: kv

        EZESliverAppbar:
            max_height: "200dp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-max-height.png
        :align: center

    :attr:`max_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `Window.height / 2`.
    """

    hide_toolbar = BooleanProperty(True)
    """
    Whether to hide the toolbar when scrolling through a list
    of custom content.

    .. code-block:: kv

        EZESliverAppbar:
            hide_toolbar: False

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-hide-toolbar.gif
        :align: center

        EZESliverAppbar:
            hide_toolbar: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-hide-toolbar-true.gif
        :align: center

    :attr:`hide_toolbar` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    radius = VariableListProperty([20], length=4)
    """
    Box radius for custom item list.

    .. code-block:: kv

        EZESliverAppbar:
            radius: 20

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[20]`.
    """

    max_opacity = NumericProperty(1)
    """
    Maximum background transparency value for the
    :class:`~eze.uix.sliverappbar.sliverappbar.EZESliverAppbarHeader` class.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-max-opacity.gif
        :align: center

    .. code-block:: kv

        EZESliverAppbar:
            max_opacity: .5

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-max-opacity-05.gif
        :align: center

    :attr:`max_opacity` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    _opacity = NumericProperty()
    _scroll_was_moving = BooleanProperty(False)
    _last_scroll_y_pos = 0.0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_scroll_content")

    def on_scroll_content(
        self,
        instance_sliverappbar: object = None,
        value: float = 1.0,
        direction: str = "up",
    ):
        """
        Called when the list of custom content is being scrolled.

        :param instance_sliverappbar: :class:`~EZESliverAppbar`
        :param value: see :attr:`~kivy.uix.scrollview.ScrollView.scroll_y`
        :param direction: scroll direction: 'up/down'
        """

    def on_background_color(
        self, instance_sliver_appbar, color_value: list
    ) -> None:
        if self.toolbar_cls:
            self.toolbar_cls.eze_bg_color = color_value

    def on_toolbar_cls(
        self, instance_sliver_appbar, instance_toolbar_cls: EZETopAppBar
    ) -> None:
        """Called when a value is set to the :attr:`toolbar_cls` parameter."""

        def on_toolbar_cls(*args):
            # If an EZETopAppBar object is already in use, delete it
            # before adding a new EZETopAppBar object.
            for widget in self.ids.float_box.children:
                if issubclass(widget.__class__, EZETopAppBar):
                    self.ids.float_box.remove_widget(widget)

            # Adding a custom EZETopAppBar object.
            if issubclass(instance_toolbar_cls.__class__, EZETopAppBar):
                instance_toolbar_cls.pos_hint = {"top": 1}
                instance_toolbar_cls.elevation = 0
                self.ids.float_box.add_widget(instance_toolbar_cls)
            else:
                raise EZESliverAppbarException(
                    "The `toolbar_cls` parameter must be an object of the "
                    "`eze.uix.toolbar.EZETopAppBar class`"
                )

        # Schedule using for declarative style.
        # Otherwise get AttributeError exception.
        Clock.schedule_once(on_toolbar_cls)

    def on_vbar(self) -> None:
        if not self.background_color:
            self.background_color = self.theme_cls.primary_color

        if not self.toolbar_cls:
            self.toolbar_cls = self.get_default_toolbar()

        scroll_box = self.ids.scroll_box
        vbar = self.ids.scroll.vbar
        toolbar_percent = (self.toolbar_cls.height / scroll_box.height) * 100
        current_percent = (vbar[0] + vbar[1]) * 100
        percent_min = (
            1 - self.max_height / scroll_box.height
        ) * 100 + toolbar_percent

        if self._scroll_was_moving:
            direction = self._get_direction_swipe(self.ids.scroll.scroll_y)
            self._last_scroll_y_pos = self.ids.scroll.scroll_y
            self.dispatch(
                "on_scroll_content", self.ids.scroll.scroll_y, direction
            )

        if self.hide_toolbar:
            if percent_min <= current_percent:
                opacity = (current_percent - percent_min) / (100 - percent_min)
                self._opacity = self.max_opacity * (1 - opacity)
                self.background_color = self.background_color[0:3] + [
                    1 - opacity
                ]
                self.toolbar_cls._hard_shadow_a = 1 - opacity
                self.toolbar_cls._soft_shadow_a = 1 - opacity
            else:
                self.background_color = self.background_color[0:3] + [1]

    def get_default_toolbar(self) -> EZETopAppBar:
        """Called if no value is passed for the toolbar_cls attribute."""

        return EZETopAppBar(
            pos_hint={"top": 1}, eze_bg_color=self.background_color
        )

    def add_widget(self, widget, index=0, canvas=None):
        if issubclass(widget.__class__, EZESliverAppbarContent):
            Clock.schedule_once(lambda x: self._set_radius(widget))
            self.ids.scroll_box.add_widget(widget)
        elif issubclass(widget.__class__, EZESliverAppbarHeader):
            self.ids.header.add_widget(widget)
        else:
            super().add_widget(widget, index=index, canvas=canvas)

    def _set_radius(self, instance: EZESliverAppbarContent) -> None:
        instance.radius = self.radius

    def _get_direction_swipe(self, current_percent: float) -> str:
        if self._last_scroll_y_pos > current_percent:
            direction = "up"
        else:
            direction = "down"
        return direction
