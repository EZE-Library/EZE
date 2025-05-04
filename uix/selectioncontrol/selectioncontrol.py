"""
Components/SelectionControls
============================

.. seealso::

    `Material Design spec, Checkbox <https://m3.material.io/components/checkbox/overview>`_

    `Material Design spec, Switch <https://m3.material.io/components/switch/overview>`_

.. rubric:: Selection controls allow the user to select options.

`EZE` provides the following selection controls classes for use:

- EZECheckbox_
- EZESwitch_

.. EZECheckbox:
EZECheckbox
----------

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from eze.app import EZEApp


    KV = '''
    EZEFloatLayout:

        EZECheckbox:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Example(EZEApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()


.. Note:: Be sure to specify the size of the checkbox. By default, it is
    `(dp(48), dp(48))`, but the ripple effect takes up all the available
    space.

Control state
-------------

.. code-block:: kv

    EZECheckbox:
        on_active: app.on_checkbox_active(*args)

.. code-block:: python

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')

EZECheckbox with group
---------------------

.. code-block:: python

    from kivy.lang import Builder

    from eze.app import EZEApp

    KV = '''
    <Check@EZECheckbox>:
        group: 'group'
        size_hint: None, None
        size: dp(48), dp(48)


    EZEFloatLayout:

        Check:
            active: True
            pos_hint: {'center_x': .4, 'center_y': .5}

        Check:
            pos_hint: {'center_x': .6, 'center_y': .5}
    '''


    class Example(EZEApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()


Parent and child checkboxes
---------------------------

Checkboxes can have a parent-child relationship with other checkboxes. When
the parent checkbox is checked, all child checkboxes are checked. If a parent
checkbox is unchecked, all child checkboxes are unchecked. If some, but not all,
child checkboxes are checked, the parent checkbox becomes an indeterminate
checkbox.

Usage
-----

.. code-block:: kv

    EZECheckbox:
        group: "root"  # this is a required name for the parent checkbox group

    EZECheckbox:
        group: "child"  # this is a required name for a group of child checkboxes

    EZECheckbox:
        group: "child"  # this is a required name for a group of child checkboxes

Example
-------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from eze.app import EZEApp
    from eze.uix.boxlayout import EZEBoxLayout

    KV = '''
    <CheckItem>
        adaptive_height: True

        EZECheckbox:
            size_hint: None, None
            size: "48dp", "48dp"
            group: root.group

        EZELabel:
            text: root.text
            adaptive_height: True
            theme_text_color: "Custom"
            text_color: "#B2B6AE"
            pos_hint: {"center_y": .5}


    EZEBoxLayout:
        orientation: "vertical"
        eze_bg_color: "#141612"

        EZETopAppBar:
            eze_bg_color: "#374134FF"
            specific_text_color: "#B2B6AE"
            elevation: 0
            title: "Meal options"
            left_action_items: [["arrow-left", lambda x: x]]
            anchor_title: "left"

        EZEBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: "12dp", "36dp", 0, 0

            CheckItem:
                text: "Recieve emails"
                group: "root"

            EZEBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "24dp", 0, 0, 0

                CheckItem:
                    text: "Daily"
                    group: "child"

                CheckItem:
                    text: "Weekly"
                    group: "child"

                CheckItem:
                    text: "Monthly"
                    group: "child"

        EZEWidget:
    '''


    class CheckItem(EZEBoxLayout):
        text = StringProperty()
        group = StringProperty()


    class Example(EZEApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Teal"
            return Builder.load_string(KV)


    Example().run()


.. EZESwitch:
EZESwitch
--------

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from eze.app import EZEApp

    KV = '''
    EZEFloatLayout:

        EZESwitch:
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Example(EZEApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()


.. Note:: Control state of :class:`~EZESwitch` same way as in
    :class:`~EZECheckbox`.
"""

__all__ = ("EZECheckbox", "EZESwitch")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    StringProperty,
)
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.floatlayout import FloatLayout

from eze import uix_path
from eze.theming import ThemableBehavior
from eze.uix.behaviors import (
    CircularRippleBehavior,
    CommonElevationBehavior,
    ScaleBehavior,
)
from eze.uix.floatlayout import EZEFloatLayout
from eze.uix.label import EZEIcon
from eze.utils import asynckivy

with open(
    os.path.join(uix_path, "selectioncontrol", "selectioncontrol.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class EZECheckbox(
    CircularRippleBehavior, ScaleBehavior, ToggleButtonBehavior, EZEIcon
):
    """
    Checkbox class.

    For more information, see in the
    :class:`~eze.uix.behaviors.CircularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ToggleButtonBehavior` and
    :class:`~eze.uix.label.EZEIcon`
    classes documentation.
    """

    __allow_child_checkboxes_active = True
    __allow_root_checkbox_active = True

    active = BooleanProperty(False)
    """
    Indicates if the checkbox is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    checkbox_icon_normal = StringProperty("checkbox-blank-outline")
    """
    Background icon of the checkbox used for the default graphical
    representation when the checkbox is not pressed.

    :attr:`checkbox_icon_normal` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-outline'`.
    """

    checkbox_icon_down = StringProperty("checkbox-marked")
    """
    Background icon of the checkbox used for the default graphical
    representation when the checkbox is pressed.

    :attr:`checkbox_icon_down` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-marked'`.
    """

    radio_icon_normal = StringProperty("checkbox-blank-circle-outline")
    """
    Background icon (when using the `group` option) of the checkbox used for
    the default graphical representation when the checkbox is not pressed.

    :attr:`radio_icon_normal` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle-outline'`.
    """

    radio_icon_down = StringProperty("checkbox-marked-circle")
    """
    Background icon (when using the `group` option) of the checkbox used for
    the default graphical representation when the checkbox is pressed.

    :attr:`radio_icon_down` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-marked-circle'`.
    """

    color_active = ColorProperty(None)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the active state.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZECheckbox:
            color_active: "red"


    :attr:`color_active` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_inactive = ColorProperty(None)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the inactive state.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZECheckbox:
            color_inactive: "blue"

    :attr:`color_inactive` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    disabled_color = ColorProperty(None)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the disabled state.

    .. code-block:: kv

        EZECheckbox:
            disabled_color: "lightgrey"
            disabled: True
            active: True

    :attr:`disabled_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Deprecated property.

    selected_color = ColorProperty(None, deprecated=True)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the active state.

    .. deprecated:: 1.0.0
        Use :attr:`color_active` instead.

    :attr:`selected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    unselected_color = ColorProperty(None, deprecated=True)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the inactive state.

    .. deprecated:: 1.0.0
        Use :attr:`color_inactive` instead.

    :attr:`unselected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _current_color = ColorProperty([0.0, 0.0, 0.0, 0.0])

    def __init__(self, **kwargs):
        self.check_anim_out = Animation(
            scale_value_x=0, scale_value_y=0, duration=0.1, t="out_quad"
        )
        self.check_anim_in = Animation(
            scale_value_x=1, scale_value_y=1, duration=0.1, t="out_quad"
        )
        super().__init__(**kwargs)
        self.color_active = self.theme_cls.primary_color
        self.color_inactive = self.theme_cls.secondary_text_color
        self.disabled_color = self.theme_cls.divider_color
        self._current_color = self.color_inactive
        self.check_anim_out.bind(
            on_complete=lambda *x: self.check_anim_in.start(self)
        )
        self.bind(
            checkbox_icon_normal=self.update_icon,
            checkbox_icon_down=self.update_icon,
            radio_icon_normal=self.update_icon,
            radio_icon_down=self.update_icon,
            group=self.update_icon,
            color_active=self.update_color,
            color_inactive=self.update_color,
            disabled_color=self.update_color,
            disabled=self.update_color,
            state=self.update_color,
        )
        self.theme_cls.bind(
            theme_style=self.update_primary_color,
            primary_color=self.update_primary_color,
        )
        self.update_icon()
        self.update_color()

    def update_primary_color(self, instance, value) -> None:
        """
        Called when the values of
        :attr:`eze.theming.ThemableBehavior.theme_cls.theme_style` and
        :attr:`eze.theming.ThemableBehavior.theme_cls.primary_color`
        change.
        """

        if value in ("Dark", "Light"):
            if not self.disabled:
                self.color = self.theme_cls.primary_color
            else:
                self.color = self.disabled_color
        else:
            self.color_active = value

    def update_icon(self, *args) -> None:
        """
        Called when the values of
        :attr:`checkbox_icon_normal` and
        :attr:`checkbox_icon_down` and
        :attr:`radio_icon_normal` and
        :attr:`group`
        change.
        """

        if self.state == "down":
            self.icon = (
                self.radio_icon_down
                if self.group and self.group not in ["root", "child"]
                else self.checkbox_icon_down
                if self.group != "root"
                else "minus-box"
            )
        else:
            self.icon = (
                self.radio_icon_normal
                if self.group and self.group not in ["root", "child"]
                else self.checkbox_icon_normal
            )

    def update_color(self, *args) -> None:
        """
        Called when the values of
        :attr:`color_active` and
        :attr:`color_inactive` and
        :attr:`disabled_color` and
        :attr:`disabled` and
        :attr:`state`
        change.
        """

        if self.disabled:
            self._current_color = self.disabled_color
        elif self.state == "down":
            self._current_color = self.color_active
        else:
            self._current_color = self.color_inactive

    def on_state(self, *args) -> None:
        """Called when the values of :attr:`state` change."""

        if self.state == "down":
            self.check_anim_in.cancel(self)
            self.check_anim_out.start(self)
            self.update_icon()
            if self.group:
                self._release_group(self)
            self.active = True
        else:
            self.check_anim_in.cancel(self)
            if not self.group:
                self.check_anim_out.start(self)
            self.update_icon()
            self.active = False

    def on_active(self, *args) -> None:
        """Called when the values of :attr:`active` change."""

        self.state = "down" if self.active else "normal"

        if (
            self.group
            and self.group == "root"
            and EZECheckbox.__allow_root_checkbox_active
        ):
            self.set_child_active(self.active)
        elif self.group and self.group == "child":
            if EZECheckbox.__allow_child_checkboxes_active:
                self.set_root_active()

    def set_root_active(self) -> None:
        root_checkbox = self.get_widgets("root")
        if root_checkbox:
            EZECheckbox.__allow_root_checkbox_active = False
            root_checkbox[0].active = True in [
                child.active for child in self.get_widgets("child")
            ]
            EZECheckbox.__allow_root_checkbox_active = True

    def set_child_active(self, active: bool):
        for child in self.get_widgets("child"):
            child.active = active
        EZECheckbox.__allow_child_checkboxes_active = True

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            if self.group and self.group == "root":
                EZECheckbox.__allow_child_checkboxes_active = False
        return super().on_touch_down(touch)

    def _release_group(self, current):
        if self.group and self.group in ["root", "child"]:
            return
        super()._release_group(current)


class EZEThumbIcon(EZEIcon):
    """
    Implements icon for the :class:`~EZEThumb` widget.

    .. versionadded:: 1.0.0
    """


class EZEThumb(CommonElevationBehavior, CircularRippleBehavior, EZEFloatLayout):
    """Implements a thumb for the :class:`~EZESwitch` widget."""

    def _set_ellipse(self, instance, value):
        self.ellipse.size = (self._ripple_rad, self._ripple_rad)
        if self.ellipse.size[0] > self.width * 1.5 and not self._fading_out:
            self.fade_out()
        self.ellipse.pos = (
            self.center_x - self._ripple_rad / 2.0,
            self.center_y - self._ripple_rad / 2.0,
        )
        self.stencil.pos = (
            self.center_x - (self.width * self.ripple_scale) / 2,
            self.center_y - (self.height * self.ripple_scale) / 2,
        )


class EZESwitch(ThemableBehavior, FloatLayout):
    """
    Switch class.

    For more information, see in the
    :class:`~eze.theming.ThemableBehavior` and
    :class:`~kivy.uix.floatlayout.FloatLayout` classes documentation.
    """

    active = BooleanProperty(False)
    """
    Indicates if the switch is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    icon_active = StringProperty()
    """
    Thumb icon when the switch is in the active state (only M3 style).

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZESwitch:
            active: True
            icon_active: "check"


    :attr:`icon_active` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_inactive = StringProperty()
    """
    EZEThumb icon when the switch is in an inactive state (only M3 style).

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZESwitch:
            icon_inactive: "close"


    :attr:`icon_inactive` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_active_color = ColorProperty(None)
    """
    EZEThumb icon color in (r, g, b, a) or string format when the switch is in the
    active state (only M3 style).

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZESwitch:
            active: True
            icon_active: "check"
            icon_active_color: "white"



    :attr:`icon_active_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_inactive_color = ColorProperty(None)
    """
    Thumb icon color in (r, g, b, a) or string format when the switch is in an
    inactive state (only M3 style).

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZESwitch:
            icon_inactive: "close"
            icon_inactive_color: "grey"


    :attr:`icon_inactive_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    eze_thumb_color_active = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the ezethumb when the switch is active.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZESwitch:
            active: True
            eze_thumb_color_active: "brown"


    :attr:`eze_thumb_color_active` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    eze_thumb_color_inactive = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the thumb when the switch is inactive.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZESwitch:
            eze_thumb_color_inactive: "brown"


    :attr:`eze_thumb_color_inactive` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    eze_thumb_color_disabled = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the thumb when the switch is
    in the disabled state.

    .. code-block:: kv

        EZESwitch:
            active: True
            eze_thumb_color_disabled: "brown"
            disabled: True


    :attr:`eze_thumb_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    track_color_active = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the track when the switch is active.

    .. code-block:: kv

        EZESwitch:
            active: True
            track_color_active: "red"


    :attr:`track_color_active` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    track_color_inactive = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the track when the switch is inactive.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZESwitch:
            track_color_inactive: "red"


    :attr:`track_color_inactive` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    track_color_disabled = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the track when the switch is
    in the disabled state.

    .. code-block:: kv

        EZESwitch:
            track_color_disabled: "lightgrey"
            disabled: True

    :attr:`track_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    eze_thumb_pos = ListProperty([0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(icon_active=self.set_icon, icon_inactive=self.set_icon)
        self.size_hint = (None, None)
        self.size = (dp(36), dp(48))
        Clock.schedule_once(self._check_style)
        Clock.schedule_once(lambda x: self._update_eze_thumb_pos(animation=False))
        Clock.schedule_once(lambda x: self.on_active(self, self.active))

    def set_icon(self, instance_switch, icon_value: str) -> None:
        """
        Called when the values of
        :attr:`icon_active` and :attr:`icon_inactive` change.
        """

        def set_icon(*args):
            icon = icon_value if icon_value else "blank"
            self.ids.eze_thumb.ids.icon.icon = icon

        Clock.schedule_once(set_icon, 0.2)

    def on_active(self, instance_switch, active_value: bool) -> None:
        """Called when the values of :attr:`active` change."""

        if self.theme_cls.material_style == "M3" and self.widget_style != "ios":
            size = (
                (
                    (dp(16), dp(16))
                    if not self.icon_inactive
                    else (dp(24), dp(24))
                )
                if not active_value
                else (dp(24), dp(24))
            )
            icon = "blank"
            color = (0, 0, 0, 0)

            if self.icon_active and active_value:
                icon = self.icon_active
                color = (
                    self.icon_active_color
                    if self.icon_active_color
                    else self.theme_cls.text_color
                )
            elif self.icon_inactive and not active_value:
                icon = self.icon_inactive
                color = (
                    self.icon_inactive_color
                    if self.icon_inactive_color
                    else self.theme_cls.text_color
                )

            Animation(size=size, t="out_quad", d=0.2).start(self.ids.eze_thumb)
            Animation(color=color, t="out_quad", d=0.2).start(
                self.ids.eze_thumb.ids.icon
            )
            self.set_icon(self, icon)

        self._update_eze_thumb_pos()

    # FIXME: If you move the cursor from the switch during the
    #  `on_touch_down` event, the animation of returning the thumb to
    #  the previous size does not work. The following code fixes this.
    def on_eze_thumb_down(self) -> None:
        """
        Called at the on_touch_down event of the :class:`~EZEThumb` object.
        Indicates the state of the switch "on/off" by an animation of
        increasing the size of the thumb.
        """

        if self.widget_style != "ios" and self.theme_cls.material_style == "M3":
            if self.active:
                size = (dp(28), dp(28))
                pos = (
                    self.ids.eze_thumb.pos[0] - dp(2),
                    self.ids.eze_thumb.pos[1] - dp(1.8),
                )
            else:
                size = (dp(27), dp(27))
                pos = (
                    (
                        self.ids.eze_thumb.pos[0] - dp(5),
                        self.ids.eze_thumb.pos[1] - dp(5),
                    )
                    if not self.icon_inactive
                    else (
                        self.ids.eze_thumb.pos[0] + dp(1),
                        self.ids.eze_thumb.pos[1] - dp(1),
                    )
                )
            Animation(size=size, pos=pos, t="out_quad", d=0.2).start(
                self.ids.eze_thumb
            )

    def _update_eze_thumb_pos(self, *args, animation=True):
        if self.active:
            eze_thumb_pos = (
                self.width
                - (
                    dp(15)
                    if self.widget_style == "ios"
                    or self.theme_cls.material_style == "M2"
                    else dp(28)
                ),
                self.height / 2
                - (
                    dp(12)
                    if self.widget_style == "ios"
                    or self.theme_cls.material_style == "M2"
                    else dp(16)
                ),
            )
        else:
            eze_thumb_pos = (
                0 if not self.icon_inactive else dp(-14),
                self.height / 2
                - (
                    dp(12)
                    if self.widget_style == "ios"
                    or self.theme_cls.material_style == "M2"
                    else dp(17)
                ),
            )
        Animation.cancel_all(self, "eze_thumb_pos")

        if animation:
            Animation(eze_thumb_pos= eze_thumb_pos, duration=0.2, t="out_quad").start(
                self
            )
        else:
            self.eze_thumb_pos = eze_thumb_pos

    def _check_style(self, *args):
        if self.widget_style == "ios" or self.theme_cls.material_style == "M2":
            self.set_icon(self, "")
