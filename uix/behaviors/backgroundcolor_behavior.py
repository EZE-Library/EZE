"""
Behaviors/Background Color
==========================

.. note:: The following classes are intended for in-house use of the library.
"""

from __future__ import annotations

__all__ = ("BackgroundColorBehavior", "SpecificBackgroundColorBehavior")

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    ReferenceListProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.utils import get_color_from_hex

from eze.color_definitions import hue, palette, text_colors
from eze.theming import ThemeManager

Builder.load_string(
    """
#:import RelativeLayout kivy.uix.relativelayout.RelativeLayout


<BackgroundColorBehavior>
    canvas:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._background_origin
        Color:
            rgba: self._eze_bg_color
        RoundedRectangle:
            group: "Background_instruction"
            size: self.size
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
            # FIXME: Sometimes the radius has the value [], which get a
            # `GraphicException:
            #     Invalid radius value, must be list of tuples/numerics` error`
            radius: root.radius if root.radius else [0, 0, 0, 0]
            source: root.background
        Color:
            rgba: self.line_color if self.line_color else (0, 0, 0, 0)
        # TODO: maybe we should use SmoothLine,
        #  but this should be tested on all widgets.
        Line:
            width: root.line_width
            rounded_rectangle:
                [ \
                self.x,
                self.y, \
                self.width, \
                self.height, \
                *self.radius, \
                ]
        PopMatrix
""",
    filename="BackgroundColorBehavior.kv",
)


class BackgroundColorBehavior:
    background = StringProperty()
    """
    Background image path.

    :attr:`background` is a :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    radius = VariableListProperty([0], length=4)
    """
    Canvas radius.

    .. code-block:: python

        # Top left corner slice.
        EZEBoxLayout:
            eze_bg_color: app.theme_cls.primary_color
            radius: [25, 0, 0, 0]

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    # FIXME: in this case, we will not be able to animate this property
    #  using the `Animation` class.
    eze_bg_color = ColorProperty([1, 1, 1, 0])
    """
    The background color of the widget (:class:`~kivy.uix.widget.Widget`)
    that will be inherited from the :attr:`BackgroundColorBehavior` class.

    For example:

    .. code-block:: kv

        Widget:
            canvas:
                Color:
                    rgba: 0, 1, 1, 1
                Rectangle:
                    size: self.size
                    pos: self.pos

    similar to code:

    .. code-block:: kv

        <MyWidget@BackgroundColorBehavior>
            md_bg_color: 0, 1, 1, 1

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 0]`.
    """

    line_color = ColorProperty([0, 0, 0, 0])
    """
    If a custom value is specified for the `line_color parameter`, the border
    of the specified color will be used to border the widget:

    .. code-block:: kv

        EZEBoxLayout:
            size_hint: .5, .2
            eze_bg_color: 0, 1, 1, .5
            line_color: 0, 0, 1, 1
            radius: [24, ]

    .. versionadded:: 0.104.2

    :attr:`line_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    line_width = NumericProperty(1)
    """
    Border of the specified width will be used to border the widget.

    .. versionadded:: 1.0.0

    :attr:`line_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    angle = NumericProperty(0)
    background_origin = ListProperty(None)

    _background_x = NumericProperty(0)
    _background_y = NumericProperty(0)
    _background_origin = ReferenceListProperty(_background_x, _background_y)
    _eze_bg_color = ColorProperty([0, 0, 0, 0])
    _origin_line_color = ColorProperty(None)
    _origin_eze_bg_color = ColorProperty(None)

    def __init__(self, **kwarg):
        super().__init__(**kwarg)
        self.bind(
            pos=self.update_background_origin,
            disabled=self.restore_color_origin,
        )

    def restore_color_origin(self, instance_eze_widget, value: bool) -> None:
        """Called when the values of :attr:`disabled` change."""

        if not value:
            if self._origin_line_color:
                self.line_color = self._origin_line_color
            if self._origin_eze_bg_color:
                self.eze_bg_color = self._origin_eze_bg_color

    def on_line_color(self, instance_eze_widget, value: list | str) -> None:
        """Called when the values of :attr:`line_color` change."""

        if not self.disabled:
            self._origin_line_color = value

    def on_eze_bg_color(self, instance_eze_widget, color: list | str):
        """Called when the values of :attr:`md_bg_color` change."""

        if (
            hasattr(self, "theme_cls")
            and self.theme_cls.theme_style_switch_animation
        ):
            Animation(
                _eze_bg_color=color,
                d=self.theme_cls.theme_style_switch_animation_duration,
                t="linear",
            ).start(self)
        else:
            self._eze_bg_color = color

        if not self.disabled:
            self._origin_md_bg_color = color

    def update_background_origin(self, instance_eze_widget, pos: list) -> None:
        """Called when the values of :attr:`pos` change."""

        if self.background_origin:
            self._background_origin = self.background_origin
        else:
            self._background_origin = self.center


class SpecificBackgroundColorBehavior(BackgroundColorBehavior):
    background_palette = OptionProperty(
        "Primary", options=["Primary", "Accent", *palette]
    )
    """
    See :attr:`eze.color_definitions.palette`.

    :attr:`background_palette` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    background_hue = OptionProperty("500", options=hue)
    """
    See :attr:`eze.color_definitions.hue`.

    :attr:`background_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'500'`.
    """

    specific_text_color = ColorProperty([0, 0, 0, 0.87])
    """
    :attr:`specific_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.87]`.
    """

    specific_secondary_text_color = ColorProperty([0, 0, 0, 0.87])
    """
    :attr:`specific_secondary_text_color`is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.89]`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if hasattr(self, "theme_cls"):
            self.theme_cls.bind(
                primary_palette=self._update_specific_text_color,
                accent_palette=self._update_specific_text_color,
                theme_style=self._update_specific_text_color,
            )
        self.bind(
            background_hue=self._update_specific_text_color,
            background_palette=self._update_specific_text_color,
        )
        self._update_specific_text_color(None, None)

    def _update_specific_text_color(
        self, instance_theme_manager: ThemeManager, theme_style: str
    ) -> None:
        if hasattr(self, "theme_cls"):
            palette = {
                "Primary": self.theme_cls.primary_palette,
                "Accent": self.theme_cls.accent_palette,
            }.get(self.background_palette, self.background_palette)
        else:
            palette = {"Primary": "Blue", "Accent": "Amber"}.get(
                self.background_palette, self.background_palette
            )
        color = get_color_from_hex(text_colors[palette][self.background_hue])
        secondary_color = color[:]
        # Check for black text (need to adjust opacity).
        if (color[0] + color[1] + color[2]) == 0:
            color[3] = 0.87
            secondary_color[3] = 0.54
        else:
            secondary_color[3] = 0.7

        if (
            hasattr(self, "theme_cls")
            and self.theme_cls.theme_style_switch_animation
        ):
            Animation(
                specific_text_color=color,
                specific_secondary_text_color=secondary_color,
                d=self.theme_cls.theme_style_switch_animation_duration,
                t="linear",
            ).start(self)
        else:
            self.specific_text_color = color
            self.specific_secondary_text_color = secondary_color
