"""
Components/SegmentedControl
===========================

.. versionadded:: 1.0.0

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-control-preview.jpg
    :align: center

Usage
=====

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from eze.app import EZEApp


            KV = '''
            EZEScreen:

                EZESegmentedControl:
                    pos_hint: {"center_x": .5, "center_y": .5}

                    EZESegmentedControlItem:
                        text: "Male"

                    EZESegmentedControlItem:
                        text: "Female"

                    EZESegmentedControlItem:
                        text: "All"
            '''


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from eze.app import EZEApp
            from eze.uix.screen import EZEScreen
            from eze.uix.segmentedcontrol import (
                EZESegmentedControl, EZESegmentedControlItem
            )


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        EZEScreen(
                            EZESegmentedControl(
                                EZESegmentedControlItem(
                                    text="Male"
                                ),
                                EZESegmentedControlItem(
                                    text="Female"
                                ),
                                EZESegmentedControlItem(
                                    text="All"
                                ),
                                pos_hint={"center_x": 0.5, "center_y": 0.5}
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-usage.gif
    :align: center

Events
======

.. code-block:: kv

    EZESegmentedControl:
        on_active: app.on_active(*args)

.. code-block:: python

    def on_active(
        self,
        segmented_control: EZESegmentedControl,
        segmented_item: EZESegmentedControlItem,
    ) -> None:
        '''Called when the segment is activated.'''
"""

__all__ = ("EZESegmentedControl", "EZESegmentedControlItem")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
    VariableListProperty,
)

from eze import uix_path
from eze.uix.boxlayout import EZEBoxLayout
from eze.uix.button import EZERaisedButton
from eze.uix.card import EZESeparator
from eze.uix.label import EZELabel
from eze.uix.relativelayout import EZERelativeLayout

with open(
    os.path.join(uix_path, "segmentedcontrol", "segmentedcontrol.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class EZESegmentedControlItem(EZELabel):
    """
    Implements a label to place on the :class:`~SegmentPanel` panel.

    See :class:`~eze.uix.label.EZELabel` class documentation for more
    information.
    """


# TODO: Add an attribute for the color of the active segment label.
class EZESegmentedControl(EZERelativeLayout):
    """
    Implements a segmented control panel.

    For more information, see in the
    :class:`~eze.uix.relativelayout.EZERelativeLayout` class documentation.

    :Events:
        `on_active`
            Called when the segment is activated.
    """

    eze_bg_color = ColorProperty([0, 0, 0, 0])
    """
    Background color of the segment panel in (r, g, b, a) or string format.

    .. code-block:: kv

        EZESegmentedControl:
            eze_bg_color: "brown"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-md-bg-color.png
        :align: center

    :attr:`eze_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    segment_color = ColorProperty([0, 0, 0, 0])
    """
    Color of the active segment in (r, g, b, a) or string format.

    .. code-block:: kv

        EZESegmentedControl:
            eze_bg_color: "brown"
            segment_color: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-segment-color.png
        :align: center

    .. code-block:: kv

        EZESegmentedControl:
            eze_bg_color: "brown"
            segment_color: "red"

            EZESegmentedControlItem:
                text: "[color=fff]Male[/color]"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-text-color.png
        :align: center

    :attr:`segment_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    segment_panel_height = NumericProperty("42dp")
    """
    Height of the segment panel.

    .. code-block:: kv

        EZESegmentedControl:
            segment_panel_height: "56dp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-segment-panel-height.png
        :align: center

    :attr:`segment_panel_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'42dp'`.
    """

    separator_color = ColorProperty(None)
    """
    The color of the separator between the segments in (r, g, b, a) or string
    format.

    .. code-block:: kv

        EZESegmentedControl:
            eze_bg_color: "brown"
            segment_color: "red"
            separator_color: "white"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-separator-color.png
        :align: center

    :attr:`separator_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    radius = VariableListProperty([16], length=4)
    """
    Radius of the segment panel.

    .. code-block:: kv

        EZESegmentedControl:
            radius: 0

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-segment-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[16, 16, 16, 16]`.
    """

    segment_switching_transition = StringProperty("in_cubic")
    """
    Name of the animation type for the switch segment.

    :attr:`segment_switching_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'in_cubic'`.
    """

    segment_switching_duration = NumericProperty(0.2)
    """
    Name of the animation type for the switch segment.

    :attr:`segment_switching_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    current_active_segment = ObjectProperty()
    """
    The current active element of the :class:`~EZESegmentedControlItem` class.

    :attr:`current_active_segment` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    _segment_switch_x = NumericProperty(dp(4))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_active")

        Clock.schedule_once(self.set_default_colors)
        Clock.schedule_once(self._remove_last_separator)

    def set_default_colors(self, *args) -> None:
        """
        Sets the colors of the panel and the switch if the colors are not set
        by the user.
        """

        if self.eze_bg_color == [0, 0, 0, 0]:
            self.eze_bg_color = self.theme_cls.bg_darkest
        if self.segment_color == [0, 0, 0, 0]:
            self.segment_color = self.theme_cls.bg_dark

    def animation_segment_switch(self, widget: EZESegmentedControlItem) -> None:
        """Animates the movement of the switch."""

        Animation(
            _segment_switch_x=widget.x - dp(6),
            t=self.segment_switching_transition,
            d=self.segment_switching_duration,
        ).start(self)

    def update_segment_panel_width(
        self, widget: EZESegmentedControlItem
    ) -> None:
        """
        Sets the width of the panel for the elements of the
        :class:`~EZESegmentedControlItem` class.
        """

        widget.text_size = (None, None)
        widget.texture_update()
        self.ids.segment_panel.width += (
            widget.texture_size[0] + self.ids.segment_panel.spacing
        )

    def update_separator_color(self, widget: EZESeparator) -> None:
        """Updates the color of the separators between segments."""

        widget.color = (
            self.separator_color
            if self.separator_color
            else self.theme_cls.divider_color
        )

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, (SegmentPanel, SegmentSwitch)):
            return super().add_widget(widget)
        if isinstance(widget, EZESegmentedControlItem):
            Clock.schedule_once(
                lambda x: self.update_segment_panel_width(widget)
            )
            widget.bind(on_touch_down=self.on_press_segment)
            self.ids.segment_panel.add_widget(widget)
            separator = EZESeparator(orientation="vertical")
            self.ids.segment_panel.add_widget(separator)
            if not self.ids.segment_panel._started:
                self.ids.segment_panel._started = True
            else:
                self.ids.segment_panel.children_number += 1
            Clock.schedule_once(
                lambda x: self.update_separator_color(separator)
            )

    def on_active(self, *args) -> None:
        """Called when the segment is activated."""

    def on_press_segment(self, widget: EZESegmentedControlItem, touch):
        if widget.collide_point(touch.x, touch.y):
            self.animation_segment_switch(widget)
            self.current_active_segment = widget
            self.dispatch("on_active", widget)

    def _remove_last_separator(self, *args):
        self.ids.segment_panel.remove_widget(self.ids.segment_panel.children[0])


class SegmentSwitch(EZERaisedButton):
    """Implements a switch for the :class:`~EZESegmentedControl` class."""

    _no_ripple_effect = BooleanProperty(True)


class SegmentPanel(EZEBoxLayout):
    """
    Implements a panel for placing items - :class:`~MDSegmentedControlItem`
    for the :class:`~EZESegmentedControl` class.
    """

    children_number = NumericProperty(1)

    _started = BooleanProperty(defaultvalue=False)
