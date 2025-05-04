"""
Components/NavigationRail
=========================

.. versionadded:: 1.0.0

.. seealso::

    `Material Design spec, Navigation rail <https://m3.material.io/components/navigation-rail/specs>`_

.. rubric:: Navigation rails provide access to primary destinations in apps
    when using tablet and desktop screens.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail.png
    :align: center

Usage
-----

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from eze.app import EZEApp

            KV = '''
            EZEBoxLayout:

                EZENavigationRail:

                    EZENavigationRailItem:
                        text: "Python"
                        icon: "language-python"

                    EZENavigationRailItem:
                        text: "JavaScript"
                        icon: "language-javascript"

                    EZENavigationRailItem:
                        text: "CPP"
                        icon: "language-cpp"

                    EZENavigationRailItem:
                        text: "Git"
                        icon: "git"

                EZEScreen:
            '''


            class Example(vApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from eze.app import EZEApp
            from eze.uix.boxlayout import EZEBoxLayout
            from eze.uix.navigationrail import EZENavigationRail, EZENavigationRailItem


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        EZEBoxLayout(
                            EZENavigationRail(
                                EZENavigationRailItem(
                                    text="Python",
                                    icon="language-python",
                                ),
                                EZENavigationRailItem(
                                    text="JavaScript",
                                    icon="language-javascript",
                                ),
                                EZENavigationRailItem(
                                    text="CPP",
                                    icon="language-cpp",
                                ),
                                EZENavigationRailItem(
                                    text="Git",
                                    icon="git",
                                ),
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-usage.png
    :align: center

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-anatomy.png
    :align: center

1. Container
2. Label text (optional)
3. Icon
4. Active indicator
5. Badge (optional)
6. Large badge (optional)
7. Large badge label (optional)
8. Menu icon (optional)

Example
=======

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.lang import Builder

            from eze.app import EZEApp
            from eze.uix.behaviors import CommonElevationBehavior
            from eze.uix.boxlayout import EZEEZEBoxLayout
            from eze.uix.button import EZEFillRoundFlatIconButton
            from eze.uix.label import EZELabel
            from eze.uix.screen import EZEScreen

            KV = '''
            #:import FadeTransition kivy.uix.screenmanager.FadeTransition


            <ExtendedButton>
                elevation: 1
                shadow_radius: 12
                -height: "54dp"


            <DrawerClickableItem@MDNavigationDrawerItem>
                focus_color: "#e7e4c0"
                unfocus_color: "#fffcf4"


            EZEScreen:

                EZENavigationLayout:

                    ScreenManager:

                        EZEScreen:

                            EZEBoxLayout:
                                orientation: "vertical"

                                EZEBoxLayout:
                                    adaptive_height: True
                                    eze_bg_color: "#FEFDFBFF"
                                    padding: "12dp"

                                    EZELabel:
                                        text: "12:00"
                                        adaptive_height: True
                                        pos_hint: {"center_y": .5}

                                EZEBoxLayout:

                                    EZENavigationRail:
                                        id: navigation_rail
                                        eze_bg_color: "#fffcf4"
                                        selected_color_background: "#e7e4c0"
                                        ripple_color_item: "#e7e4c0"
                                        on_item_release: app.switch_screen(*args)

                                        EZENavigationRailMenuButton:
                                            on_release: nav_drawer.set_state("open")

                                        EZENavigationRailFabButton:
                                            eze_bg_color: "#b0f0d6"

                                        EZENavigationRailItem:
                                            text: "Python"
                                            icon: "language-python"

                                        EZENavigationRailItem:
                                            text: "JavaScript"
                                            icon: "language-javascript"

                                        EZENavigationRailItem:
                                            text: "CPP"
                                            icon: "language-cpp"

                                        EZENavigationRailItem:
                                            text: "Swift"
                                            icon: "language-swift"

                                    ScreenManager:
                                        id: screen_manager
                                        transition:
                                            FadeTransition(duration=.2, clearcolor=app.theme_cls.bg_dark)

                EZENavigationDrawer:
                    id: nav_drawer
                    radius: 0, 16, 16, 0
                    eze_bg_color: "#fffcf4"
                    elevation: 2
                    width: "240dp"

                    EZENavigationDrawerMenu:

                        EZEBoxLayout:
                            orientation: "vertical"
                            adaptive_height: True
                            spacing: "12dp"
                            padding: 0, 0, 0, "12dp"

                            EZEIconButton:
                                icon: "menu"

                            EZEBoxLayout:
                                adaptive_height: True
                                padding: "12dp", 0, 0, 0

                                ExtendedButton:
                                    text: "Compose"
                                    icon: "pencil"

                        DrawerClickableItem:
                            text: "Python"
                            icon: "language-python"

                        DrawerClickableItem:
                            text: "JavaScript"
                            icon: "language-javascript"

                        DrawerClickableItem:
                            text: "CPP"
                            icon: "language-cpp"

                        DrawerClickableItem:
                            text: "Swift"
                            icon: "language-swift"
            '''


            class ExtendedButton(MDFillRoundFlatIconButton, CommonElevationBehavior):
                '''
                Implements a button of type
                `Extended FAB <https://m3.material.io/components/extended-fab/overview>`_.

                .. rubric::
                    Extended FABs help people take primary actions.
                    They're wider than FABs to accommodate a text label and larger target
                    area.

                This type of buttons is not yet implemented in the standard widget set
                of the KivyMD library, so we will implement it ourselves in this class.
                '''

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.padding = "16dp"
                    Clock.schedule_once(self.set_spacing)

                def set_spacing(self, interval):
                    self.ids.box.spacing = "12dp"

                def set_radius(self, *args):
                    if self.rounded_button:
                        value = self.height / 4
                        self.radius = [value, value, value, value]
                        self._radius = value


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.material_style = "M3"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)

                def switch_screen(
                    self, instance_navigation_rail, instance_navigation_rail_item
                ):
                    '''
                    Called when tapping on rail menu items. Switches application screens.
                    '''

                    self.root.ids.screen_manager.current = (
                        instance_navigation_rail_item.icon.split("-")[1].lower()
                    )

                def on_start(self):
                    '''Creates application screens.'''

                    navigation_rail_items = self.root.ids.navigation_rail.get_items()[:]
                    navigation_rail_items.reverse()

                    for widget in navigation_rail_items:
                        name_screen = widget.icon.split("-")[1].lower()
                        screen = EZEScreen(
                            name=name_screen,
                            eze_bg_color="#edd769",
                            radius=[18, 0, 0, 0],
                        )
                        box = EZEBoxLayout(padding="12dp")
                        label = EZELabel(
                            text=name_screen.capitalize(),
                            font_style="H1",
                            halign="right",
                            adaptive_height=True,
                            shorten=True,
                        )
                        box.add_widget(label)
                        screen.add_widget(box)
                        self.root.ids.screen_manager.add_widget(screen)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.metrics import dp

            from eze.app import EZEApp
            from eze.uix.behaviors import CommonElevationBehavior
            from eze.uix.boxlayout import EZEBoxLayout
            from eze.uix.button import EZEFillRoundFlatIconButton, EZEIconButton
            from eze.uix.label import EZELabel
            from eze.uix.navigationdrawer import (
                EZENavigationDrawerItem,
                EZENavigationLayout,
                EZENavigationDrawer,
                EZENavigationDrawerMenu,
            )
            from eze.uix.navigationrail import (
                EZENavigationRail,
                EZENavigationRailMenuButton,
                EZENavigationRailFabButton,
                EZENavigationRailItem,
            )
            from eze.uix.screen import EZEScreen
            from eze.uix.screenmanager import EZEScreenManager


            class DrawerClickableItem(EZENavigationDrawerItem):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.focus_color = "#e7e4c0"
                    self.unfocus_color = self.theme_cls.bg_light
                    self.radius = 24


            class ExtendedButton(EZEFillRoundFlatIconButton, CommonElevationBehavior):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.padding = "16dp"
                    self.elevation = 1
                    self.shadow_radius = 12
                    self.height = dp(56)
                    Clock.schedule_once(self.set_spacing)

                def set_spacing(self, interval):
                    self.ids.box.spacing = "12dp"

                def set_radius(self, *args):
                    if self.rounded_button:
                        self._radius = self.radius = self.height / 4


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.material_style = "M3"
                    self.theme_cls.primary_palette = "Orange"
                    return EZEScreen(
                        EZENavigationLayout(
                            EZEScreenManager(
                                EZEScreen(
                                    EZEBoxLayout(
                                        EZEBoxLayout(
                                            EZELabel(
                                                text="12:00",
                                                adaptive_height=True,
                                                pos_hint={"center_y": 0.5},
                                            ),
                                            adaptive_height=True,
                                            EZE_bg_color="#fffcf4",
                                            padding="12dp",
                                        ),
                                        EZEBoxLayout(
                                            EZENavigationRail(
                                                EZENavigationRailMenuButton(
                                                    on_release=self.open_nav_drawer,
                                                ),
                                                EZENavigationRailFabButton(
                                                    eze_bg_color="#b0f0d6",
                                                ),
                                                EZENavigationRailItem(
                                                    text="Python",
                                                    icon="language-python",
                                                ),
                                                EZENavigationRailItem(
                                                    text="JavaScript",
                                                    icon="language-javascript",
                                                ),
                                                EZENavigationRailItem(
                                                    text="CPP",
                                                    icon="language-cpp",
                                                ),
                                                EZENavigationRailItem(
                                                    text="Swift",
                                                    icon="language-swift",
                                                ),
                                                id="navigation_rail",
                                                eze_bg_color="#fffcf4",
                                                selected_color_background="#e7e4c0",
                                                ripple_color_item="#e7e4c0",
                                            ),
                                            EZEScreenManager(
                                                id="screen_manager_content",
                                            ),
                                            id="root_box",
                                        ),
                                        id="box_rail",
                                        orientation="vertical",
                                    ),
                                    id="box",
                                ),
                                id="screen",
                            ),
                            id="screen_manager",
                        ),
                        EZENavigationDrawer(
                            EZENavigationDrawerMenu(
                                EZEBoxLayout(
                                    EZEIconButton(
                                        icon="menu",
                                    ),
                                    EZEBoxLayout(
                                        ExtendedButton(
                                            text="Compose",
                                            icon="pencil",
                                        ),
                                        adaptive_height=True,
                                        padding=["12dp", 0, 0, 0],
                                    ),
                                    orientation="vertical",
                                    adaptive_height=True,
                                    spacing="12dp",
                                    padding=("3dp", 0, 0, "12dp"),
                                ),
                                DrawerClickableItem(
                                    text="Python",
                                    icon="language-python",
                                ),
                                DrawerClickableItem(
                                    text="JavaScript",
                                    icon="language-javascript",
                                ),
                                DrawerClickableItem(
                                    text="CPP",
                                    icon="language-cpp",
                                ),
                                DrawerClickableItem(
                                    text="Swift",
                                    icon="language-swift",
                                ),
                            ),
                            id="nav_drawer",
                            radius=(0, 16, 16, 0),
                            elevation=4,
                            width="240dp",
                        ),
                    )

                def switch_screen(self, *args, screen_manager_content=None):
                    '''
                    Called when tapping on rail menu items. Switches application screens.
                    '''

                    instance_navigation_rail, instance_navigation_rail_item = args
                    screen_manager_content.current = (
                        instance_navigation_rail_item.icon.split("-")[1].lower()
                    )

                def open_nav_drawer(self, *args):
                    self.root.ids.nav_drawer.set_state("open")

                def on_start(self):
                    '''Creates application screens.'''

                    screen_manager = self.root.ids.screen_manager
                    root_box = screen_manager.ids.screen.ids.box.ids.box_rail.ids.root_box
                    navigation_rail = root_box.ids.navigation_rail
                    screen_manager_content = root_box.ids.screen_manager_content
                    navigation_rail_items = navigation_rail.get_items()[:]
                    navigation_rail_items.reverse()
                    navigation_rail.bind(
                        on_item_release=lambda *args: self.switch_screen(
                            *args, screen_manager_content=screen_manager_content
                        )
                    )

                    for widget in navigation_rail_items:
                        name_screen = widget.icon.split("-")[1].lower()
                        screen_manager_content.add_widget(
                            EZEScreen(
                                EZEBoxLayout(
                                    EZELabel(
                                        text=name_screen.capitalize(),
                                        font_style="H1",
                                        halign="right",
                                        adaptive_height=True,
                                        shorten=True,
                                    ),
                                    padding="12dp",
                                ),
                                name=name_screen,
                                eze_bg_color="#6B5F1FFF",
                                radius=[18, 0, 0, 0],
                            ),
                        )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-example.gif
    :align: center

"""

__all__ = (
    "EZENavigationRail",
    "EZENavigationRailItem",
    "EZENavigationRailFabButton",
    "EZENavigationRailMenuButton",
)

import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior

from eze import uix_path
from eze.uix.behaviors import ScaleBehavior
from eze.uix.boxlayout import EZEBoxLayout
from eze.uix.button import EZEFloatingActionButton, EZEIconButton
from eze.uix.card import EZECard
from eze.uix.floatlayout import EZEFloatLayout
from eze.uix.widget import EZEWidget

with open(
    os.path.join(uix_path, "navigationrail", "navigationrail.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class PanelRoot(EZEFloatLayout):
    """
    Contains
    :class:`~EZENavigationRailFabButton`, :class:`~EZENavigationRailMenuButton`
    buttons and a :class:`~Paneltems` container with menu items.
    """


class PanelItems(EZEBoxLayout):
    """Box for menu items."""


class RippleWidget(EZEWidget, ScaleBehavior):
    """
    Implements a background color for a menu item -
    (:class:`~EZENavigationRailItem`).
    """


class EZENavigationRailFabButton(EZEFloatingActionButton):
    """
    Implements an optional floating action button (FAB).

    For more information, see in the
    :class:`~eze.uix.button.EZEFloatingActionButton` class documentation.
    """

    icon = StringProperty("pencil")
    """
    Button icon name.

    .. code-block:: kv

        EZENavigationRail:

            EZENavigationRailFabButton:
                icon: "home"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-fab-button-icon.png
        :align: center

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'pencil'`.
    """


class EZENavigationRailMenuButton(EZEIconButton):
    """
    Implements a menu button.

    For more information, see in the
    :class:`~eze.uix.button.EZEIconButton` classes documentation.
    """

    icon = StringProperty("menu")
    """
    Button icon name.

    .. code-block:: kv

        EZENavigationRail:

            EZENavigationRailMenuButton:
                icon: "home"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-menu-button-icon.png
        :align: center

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'menu'`.
    """


class EZENavigationRailItem(ButtonBehavior, EZEBoxLayout):
    """
    Implements a menu item with an icon and text.

    For more information, see in the
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~eze.uix.boxlayout.EZEBoxLayout`
    classes documentation.
    """

    navigation_rail = ObjectProperty()
    """
    :class:`~EZENavigationRail` object.

    :attr:`navigation_rail` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    icon = StringProperty("checkbox-blank-circle")
    """
    Icon item.

    .. code-block:: kv

        EZENavigationRail:

            EZENavigationRailItem:
                icon: "language-python"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-icon.png
        :align: center

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank'`.
    """

    text = StringProperty()
    """
    Text item.

    .. code-block:: kv

        EZENavigationRail:

            EZENavigationRailItem:
                text: "Python"
                icon: "language-python"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-text.png
        :align: center

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    badge_icon = StringProperty()
    """
    Badge icon name.

    .. code-block:: kv

        EZENavigationRail:

            EZENavigationRailItem:
                text: "Python"
                icon: "language-python"
                badge_icon: "plus"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-badge-icon.png
        :align: center

    :attr:`badge_icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    badge_icon_color = ColorProperty(None)
    """
    Badge icon color in (r, g, b, a) format.

    .. code-block:: kv

        EZENavigationRail:

            EZENavigationRailItem:
                text: "Python"
                icon: "language-python"
                badge_icon: "plus"
                badge_icon_color: 0, 0, 1, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-badge-icon-color.png
        :align: center

    :attr:`badge_icon_color` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    badge_bg_color = ColorProperty(None)
    """
    Badge icon background color in (r, g, b, a) format.

    .. code-block:: kv

        EZENavigationRail:

            EZENavigationRailItem:
                text: "Python"
                icon: "language-python"
                badge_icon: "plus"
                badge_bg_color: "#b0f0d6"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-badge-bg-color.png
        :align: center

    :attr:`badge_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    badge_font_size = NumericProperty(0)
    """
    Badge icon font size.

    .. code-block:: kv

        EZENavigationRail:

            EZENavigationRailItem:
                text: "Python"
                icon: "language-python"
                badge_icon: "plus"
                badge_font_size: "24sp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-badge-font-size.png
        :align: center

    :attr:`badge_font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    active = BooleanProperty(False)
    """
    Is the element active.

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _selected_region_width = NumericProperty("56dp")
    _ripple_size = ListProperty([0, 0])
    _release = BooleanProperty(False)

    def on_active(
        self, instance_navigation_rail_item, value_active: bool
    ) -> None:
        """Called when the value of `active` changes."""

        self.animation_size_ripple_area(1 if value_active else 0)

    def animation_size_ripple_area(self, value: int) -> None:
        """Animates the size/fade of the ripple area."""

        Animation(
            scale_value_x=value,
            scale_value_y=value,
            scale_value_z=value,
            opacity=value,
            d=0.25,
            t=self.navigation_rail.ripple_transition,
        ).start(self.ids.ripple_widget)

    def on_press(self) -> None:
        """Called when pressed on a panel element."""

        self._release = False
        self.active = True
        self.navigation_rail.deselect_item(self)
        self.navigation_rail.dispatch("on_item_press", self)

    def on_release(self) -> None:
        """Called when released on a panel element."""

        self._release = True
        self.animation_size_ripple_area(0)
        self.navigation_rail.dispatch("on_item_release", self)


class EZENavigationRail(EZECard):
    """
    Navigation rail class.

    For more information, see in the
    :class:`~eze.uix.card.EZECard` class documentation.

    :Events:
        :attr:`on_item_press`
            Called on the `on_press` event of menu item -
            :class:`~EZENavigationRailItem`.

        :attr:`on_item_release`
            Called on the `on_release` event of menu item -
            :class:`~EZENavigationRailItem`.
    """

    radius = VariableListProperty(0, length=4)
    """
    Rail radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    padding = VariableListProperty([0, "36dp", 0, "36dp"], length=4)
    """
    Padding between layout box and children:
    [padding_left, padding_top, padding_right, padding_bottom].

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, '36dp', 0, '36dp']`.
    """

    anchor = OptionProperty("top", options=["top", "bottom", "center"])
    """
    The position of the panel with menu items.
    Available options are: `'top'`, `'bottom'`, `'center'`.

    .. rubric:: Top

    .. code-block:: kv

        EZENavigationRail:
            anchor: "top"

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-anchor-top.png
        :align: center

    .. rubric:: Center

    .. code-block:: kv

        EZENavigationRail:
            anchor: "center"

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-center.png
        :align: center

    .. rubric:: Bottom

    .. code-block:: kv

        EZENavigationRail:
            anchor: "bottom"

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-bottom.png
        :align: center

    :attr:`anchor` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'top'`.
    """

    type = OptionProperty(
        "labeled", options=["labeled", "selected", "unselected"]
    )
    """
    Type of switching menu items.
    Available options are: `'labeled'`, `'selected'`, `'unselected'`.

    .. rubric:: Labeled

    .. code-block:: kv

        EZENavigationRail:
            type: "labeled"

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-labeled.png
        :align: center

    .. rubric:: Selected

    .. code-block:: kv

        EZENavigationRail:
            type: "selected"

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-selected.gif
        :align: center

    .. rubric:: Unselected

    .. code-block:: kv

        EZENavigationRail:
            type: "unselected"

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-unselected.gif
        :align: center

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'labeled'`.
    """

    text_color_item_normal = ColorProperty(None)
    """
    The text color in (r, g, b, a) or string format of the normal menu item
    (:class:`~EZENavigationRailItem`).

    .. code-block:: kv

        EZENavigationRail:
            text_color_item_normal: app.theme_cls.primary_color

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-text-color-item-normal.png
        :align: center

    :attr:`text_color_item_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color_item_active = ColorProperty(None)
    """
    The text color in (r, g, b, a) or string format of the active menu item
    (:class:`~EZENavigationRailItem`).

    .. code-block:: kv

        EZENavigationRail:
            text_color_item_active: app.theme_cls.primary_color

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-text-color-item-active.png
        :align: center

    :attr:`text_color_item_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color_item_normal = ColorProperty(None)
    """
    The icon color in (r, g, b, a) or string format of the normal menu item
    (:class:`~EZENavigationRailItem`).

    .. code-block:: kv

        EZENavigationRail:
            icon_color_item_normal: app.theme_cls.primary_color

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-icon-color-item-normal.png
        :align: center

    :attr:`icon_color_item_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color_item_active = ColorProperty(None)
    """
    The icon color in (r, g, b, a) or string format of the active menu item
    (:class:`~EZENavigationRailItem`).

    .. code-block:: kv

        EZENavigationRail:
            icon_color_item_active: app.theme_cls.primary_color

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-icon-color-item-active.png
        :align: center

    :attr:`icon_color_item_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    selected_color_background = ColorProperty(None)
    """
    Background color which will highlight the icon of the active menu item -
    :class:`~EZENavigationRailItem` - in (r, g, b, a) format.

    .. code-block:: kv

        EZENavigationRail:
            selected_color_background: "#e7e4c0"

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-selected-color-background.png
        :align: center

    :attr:`selected_color_background` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    ripple_color_item = ColorProperty(None)
    """
    Ripple effect color of menu items (:class:`~EZENavigationRailItem`)
    in (r, g, b, a) format.

    .. code-block:: kv

        EZENavigationRail:
            ripple_color_item: "#e7e4c0"

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-ripple-color-item.png
        :align: center

    :attr:`ripple_color_item` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    ripple_transition = StringProperty("out_cubic")
    """
    Type of animation of the ripple effect when a menu item is selected.

    :attr:`ripple_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'ripple_transition'`.
    """

    current_selected_item = NumericProperty(0)
    """
    Index of the menu list item (:class:`~EZENavigationRailItem`) that will be
    active by default

    .. code-block:: kv

        EZENavigationRail:
            current_selected_item: 1

            EZENavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-current-selected-item.png
        :align: center

    :attr:`current_selected_item` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    font_name = StringProperty("Roboto")
    """
    Font path for menu item (:class:`~EZENavigationRailItem`) text.

    .. code-block:: kv

        EZENavigationRail:

            EZENavigationRailItem:
                text: "Python"
                icon: "language-python"
                font_name: "nasalization-rg.ttf"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-font-name.png
        :align: center

    :attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Roboto'`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_pos_menu_fab_buttons)
        Clock.schedule_once(self.set_current_selected_item)
        self.register_event_type("on_item_press")
        self.register_event_type("on_item_release")

    def on_size(self, *args):
        Clock.schedule_once(self.set_pos_menu_fab_buttons)

    def on_item_press(self, *args) -> None:
        """
        Called on the `on_press` event of menu item -
        :class:`~EZENavigationRailItem`.
        """

    def on_item_release(self, *args) -> None:
        """
        Called on the `on_release` event of menu item -
        :class:`~EZENavigationRailItem`.
        """

    def deselect_item(
        self, selected_navigation_rail_item: EZENavigationRailItem
    ) -> None:
        """
        Sets the `active` value to `False` for all menu items
        (:class:`~EZENavigationRailItem`) except the selected item.
        Called when a menu item is touched.
        """

        for navigation_rail_item in self.ids.box_items.children:
            if selected_navigation_rail_item is not navigation_rail_item:
                navigation_rail_item.active = False

    def get_items(self) -> list:
        """Returns a list of :class:`~EZENavigationRailItem` objects"""

        return self.ids.box_items.children

    def set_pos_panel_items(
        self,
        instance_fab_button: Union[None, EZENavigationRailFabButton],
        instance_menu_button: Union[None, EZENavigationRailFabButton],
    ) -> None:
        """Set :class:`~Paneltems` panel position with menu items."""

        if self.anchor == "top":
            if instance_fab_button:
                self.ids.box_items.y = instance_fab_button.y - (
                    len(self.ids.box_items.children) * dp(56)
                    + self.padding[1] * 2
                    + dp(24)
                )
            else:
                if not instance_menu_button:
                    self.ids.box_items.pos_hint = {"top": 1}
                else:
                    self.ids.box_items.y = instance_menu_button.y - (
                        len(self.ids.box_items.children) * dp(56)
                        + self.padding[1] * 2
                    )
        elif self.anchor == "center":
            self.ids.box_items.pos_hint = {"center_y": 0.5}
        elif self.anchor == "bottom":
            self.ids.box_items.y = dp(12)

    def set_current_selected_item(self, interval: Union[int, float]) -> None:
        """Sets the active menu list item (:class:`~EZENavigationRailItem`)."""

        if self.ids.box_items.children:
            items = self.ids.box_items.children[:]
            items.reverse()

            if len(items) <= self.current_selected_item:
                Logger.error(
                    f"EZENavigationRail:You have "
                    f"{len(self.ids.box_items.children)} menu items, but you "
                    f"set {self.current_selected_item} as the active item. "
                    f"The very first menu item will be set active."
                )
                index = 0
            else:
                index = self.current_selected_item

            items[index].dispatch("on_press")
            items[index].dispatch("on_release")

    def set_pos_menu_fab_buttons(self, *args) -> None:
        """
        Sets the position of the :class:`~EZENavigationRailFabButton` and
        :class:`~EZENavigationRailMenuButton` buttons on the panel.
        """

        fab_button = None  # EZENavigationRailFabButton
        menu_button = None  # EZENavigationRailMenuButton

        for widget in self.ids.box_buttons.children:
            if isinstance(widget, EZENavigationRailFabButton):
                fab_button = widget
            if isinstance(widget, EZENavigationRailMenuButton):
                menu_button = widget

        if fab_button and menu_button:

            def set_fab_button_y(interval):
                fab_button.y = self.parent.height - (
                    menu_button.height
                    + fab_button.height
                    + self.padding[1]
                    + dp(18)
                )
                self.set_pos_panel_items(fab_button, menu_button)

            Clock.schedule_once(set_fab_button_y)
        elif fab_button and not menu_button:

            def set_fab_button_y(interval):
                fab_button.y = self.parent.height - (
                    self.padding[1] + fab_button.height
                )
                self.set_pos_panel_items(fab_button, menu_button)

            Clock.schedule_once(set_fab_button_y)
        else:
            Clock.schedule_once(
                lambda x: self.set_pos_panel_items(fab_button, menu_button)
            )

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, EZENavigationRailFabButton):
            self.ids.box_buttons.add_widget(widget)
        elif isinstance(widget, EZENavigationRailMenuButton):
            self.ids.box_buttons.add_widget(widget)
        elif isinstance(widget, EZENavigationRailItem):
            widget.navigation_rail = self
            self.ids.box_items.add_widget(widget)
        elif isinstance(widget, (PanelRoot, PanelItems)):
            return super().add_widget(widget)
