"""
Components/NavigationDrawer
===========================

.. seealso::

    `Material Design 2 spec, Navigation drawer <https://material.io/components/navigation-drawer>`_ and
    `Material Design 3 spec, Navigation drawer <https://m3.material.io/components/navigation-drawer/overview>`_

.. rubric:: Navigation drawers provide access to destinations in your app.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer.png
    :align: center

When using the class :class:`~MDNavigationDrawer` skeleton of your `KV` markup
should look like this:

Anatomy
-------

.. code-block:: kv

    Root:

        EZENavigationLayout:

            EZEScreenManager:

                Screen_1:

                Screen_2:

            EZENavigationDrawer:

                # This custom rule should implement what will be appear in your
                # EZENavigationDrawer.
                ContentNavigationDrawer:

A simple example
----------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: python

            from kivy.lang import Builder

            from eze.uix.boxlayout import EZEBoxLayout
            from eze.app import EZEApp

            KV = '''
            EZEScreen:

                EZENavigationLayout:

                    EZEScreenManager:

                        EZEScreen:

                            EZETopAppBar:
                                title: "Navigation Drawer"
                                elevation: 5
                                pos_hint: {"top": 1}
                                eze_bg_color: "#e7e4c0"
                                specific_text_color: "#3A3A33FF"
                                left_action_items:
                                    [['menu', lambda x: nav_drawer.set_state("open")]]


                    EZENavigationDrawer:
                        id: nav_drawer
                        radius: (0, 1, 1, 0)

                        ContentNavigationDrawer:
            '''


            class ContentNavigationDrawer(EZEBoxLayout):
                pass


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from eze.app import EZEApp
            from eze.uix.boxlayout import EZEBoxLayout
            from eze.uix.navigationdrawer import EZENavigationLayout, EZENavigationDrawer
            from eze.uix.screen import EZEScreen
            from eze.uix.screenmanager import EZEScreenManager
            from eze.uix.toolbar import EZETopAppBar


            class ContentNavigationDrawer(EZEBoxLayout):
                pass


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return(
                        EZEScreen(
                            EZENavigationLayout(
                                EZEScreenManager(
                                    EZEScreen(
                                        EZETopAppBar(
                                            title="Navigation Drawer",
                                            elevation=4,
                                            pos_hint={"top": 1},
                                            eze_bg_color="#e7e4c0",
                                            specific_text_color="#3E3D33FF",
                                            left_action_items=[
                                                ['menu', lambda x: self.nav_drawer_open()]
                                            ],
                                        )

                                    )
                                ),
                                EZENavigationDrawer(
                                    ContentNavigationDrawer(),
                                    id="nav_drawer",
                                    radius=(0, 6, 6, 0),
                                ),
                            ),
                        ),
                    )

                def nav_drawer_open(self, *args):
                    nav_drawer = self.root.children[0].ids.nav_drawer
                    nav_drawer.set_state("open")


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer.gif
    :align: center

.. Note:: :class:`~MDNavigationDrawer` is an empty
    :class:`~eze.uix.card.EZECard` panel.

Standard content for the navigation bar
---------------------------------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: python

            from kivy.lang import Builder

            from eze.app import EZEApp

            KV = '''
            <DrawerClickableItem@EZENavigationDrawerItem>
                focus_color: "#e7e4c0"
                text_color: "#404037FF"
                icon_color: "#565437FF"
                ripple_color: "#c5bdd2"
                selected_color: "#0c6c4d"


            <DrawerLabelItem@EZENavigationDrawerItem>
                text_color: "#3C3A21FF"
                icon_color: "#4A6164FF"
                focus_behavior: False
                selected_color: "#B69949FF"
                _no_ripple_effect: True


            EZEScreen:

                EZENavigationLayout:

                    EZEScreenManager:

                        EZEScreen:

                            EZETopAppBar:
                                title: "Navigation Drawer"
                                elevation: 4
                                pos_hint: {"top": 1}
                                eze_bg_color: "#FCF9DCFF"
                                specific_text_color: "#8B8966FF"
                                left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                    EZENavigationDrawer:
                        id: nav_drawer
                        radius: (0, 16, 16, 0)

                        EZENavigationDrawerMenu:

                            EZENavigationDrawerHeader:
                                title: "Header title"
                                title_color: "#9F7E8FFF"
                                text: "Header text"
                                spacing: "4dp"
                                padding: "12dp", 0, 0, "56dp"

                            EZENavigationDrawerLabel:
                                text: "Mail"

                            DrawerClickableItem:
                                icon: "gmail"
                                right_text: "+99"
                                text_right_color: "#4a4939"
                                text: "Inbox"

                            DrawerClickableItem:
                                icon: "send"
                                text: "Outbox"

                            EZENavigationDrawerDivider:

                            EZENavigationDrawerLabel:
                                text: "Labels"

                            DrawerLabelItem:
                                icon: "information-outline"
                                text: "Label"

                            DrawerLabelItem:
                                icon: "information-outline"
                                text: "Label"
            '''


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from eze.app import EZEApp
            from eze.uix.navigationdrawer import (
                EZENavigationLayout,
                EZENavigationDrawer,
                EZENavigationDrawerMenu,
                EZENavigationDrawerHeader,
                EZENavigationDrawerLabel,
                EZENavigationDrawerDivider,
                EZENavigationDrawerItem,
            )
            from eze.uix.screen import EZEScreen
            from eze.uix.screenmanager import EZEScreenManager
            from eze.uix.toolbar import EZETopAppBar


            class BaseNavigationDrawerItem(EZENavigationDrawerItem):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.radius = 24
                    self.text_color = "#1E1D0EFF"
                    self.icon_color = "#3A3A38FF"
                    self.focus_color = "#e7e4c0"


            class DrawerLabelItem(BaseNavigationDrawerItem):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.focus_behavior = False
                    self._no_ripple_effect = True
                    self.selected_color = "#4a4939"


            class DrawerClickableItem(BaseNavigationDrawerItem):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.ripple_color = "#c5bdd2"
                    self.selected_color = "#0c6c4d"


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return(
                        EZEScreen(
                            EZENavigationLayout(
                                EZEScreenManager(
                                    EZEScreen(
                                        EZETopAppBar(
                                            title="Navigation Drawer",
                                            elevation=4,
                                            pos_hint={"top": 1},
                                            eze_bg_color="#e7e4c0",
                                            specific_text_color="#4a4939",
                                            left_action_items=[
                                                ['menu', lambda x: self.nav_drawer_open()]
                                            ],
                                        )

                                    )
                                ),
                                EZENavigationDrawer(
                                    EZENavigationDrawerMenu(
                                        EZENavigationDrawerHeader(
                                            title="Header title",
                                            title_color="#4a4939",
                                            text="Header text",
                                            spacing="4dp",
                                            padding=("12dp", 0, 0, "56dp"),
                                        ),
                                        EZENavigationDrawerLabel(
                                            text="Mail",
                                        ),
                                        DrawerClickableItem(
                                            icon="gmail",
                                            right_text="+99",
                                            text_right_color="#4E4A17FF",
                                            text="Inbox",
                                        ),
                                        DrawerClickableItem(
                                            icon="send",
                                            text="Outbox",
                                        ),
                                        EZENavigationDrawerDivider(),
                                        EZENavigationDrawerLabel(
                                            text="Labels",
                                        ),
                                        DrawerLabelItem(
                                            icon="information-outline",
                                            text="Label",
                                        ),
                                        DrawerLabelItem(
                                            icon="information-outline",
                                            text="Label",
                                        ),
                                    ),
                                    id="nav_drawer",
                                    radius=(0, 16, 16, 0),
                                )
                            )
                        )
                    )

                def nav_drawer_open(self, *args):
                    nav_drawer = self.root.children[0].ids.nav_drawer
                    nav_drawer.set_state("open")


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-standatd-content.gif
    :align: center

Switching screens in the ``ScreenManager`` and using the common ``MDTopAppBar``
-----------------------------------------------------------------------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import ObjectProperty

            from eze.app import EZEApp
            from eze.uix.scrollview import EZEScrollView

            KV = '''
            <ContentNavigationDrawer>

                EZEList:

                    OneLineListItem:
                        text: "Screen 1"
                        on_press:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "scr 1"

                    OneLineListItem:
                        text: "Screen 2"
                        on_press:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "scr 2"


            EZEScreen:

                EZETopAppBar:
                    pos_hint: {"top": 1}
                    elevation: 4
                    title: "EZENavigationDrawer"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                EZENavigationLayout:

                    EZEScreenManager:
                        id: screen_manager

                        EZEScreen:
                            name: "scr 1"

                            EZELabel:
                                text: "Screen 1"
                                halign: "center"

                        EZEScreen:
                            name: "scr 2"

                            EZELabel:
                                text: "Screen 2"
                                halign: "center"

                    EZENavigationDrawer:
                        id: nav_drawer
                        radius: (0, 16, 16, 0)

                        ContentNavigationDrawer:
                            screen_manager: screen_manager
                            nav_drawer: nav_drawer
            '''


            class ContentNavigationDrawer(EZEScrollView):
                screen_manager = ObjectProperty()
                nav_drawer = ObjectProperty()


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from eze.app import EZEApp
            from eze.uix.label import EZELabel
            from eze.uix.list import EZEList, OneLineListItem
            from eze.uix.navigationdrawer import EZENavigationLayout, EZENavigationDrawer
            from eze.uix.screen import EZEScreen
            from eze.uix.screenmanager import EZEScreenManager
            from eze.uix.scrollview import EZEScrollView
            from eze.uix.toolbar import EZETopAppBar


            class Example(EZEApp):
                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return (
                        EZEScreen(
                            EZETopAppBar(
                                pos_hint={"top": 1},
                                elevation=4,
                                title="EZENavigationDrawer",
                                left_action_items=[["menu", lambda x: self.nav_drawer_open()]],
                            ),
                            EZENavigationLayout(
                                EZEScreenManager(
                                    EZEScreen(
                                        EZELabel(
                                            text="Screen 1",
                                            halign="center",
                                        ),
                                        name="scr 1",
                                    ),
                                    EZEScreen(
                                        EZELabel(
                                            text="Screen 2",
                                            halign="center",
                                        ),
                                        name="scr 2",
                                    ),
                                    id="screen_manager",
                                ),
                                EZENavigationDrawer(
                                    EZEScrollView(
                                        EZEList(
                                            OneLineListItem(
                                                text="Screen 1",
                                                on_press=self.switch_screen,
                                            ),
                                            OneLineListItem(
                                                text="Screen 2",
                                                on_press=self.switch_screen,
                                            ),
                                        ),
                                    ),
                                    id="nav_drawer",
                                    radius=(0, 16, 16, 0),
                                ),
                                id="navigation_layout",
                            )
                        )
                    )

                def switch_screen(self, instance_list_item: OneLineListItem):
                    self.root.ids.navigation_layout.ids.screen_manager.current = {
                        "Screen 1": "scr 1", "Screen 2": "scr 2"
                    }[instance_list_item.text]
                    self.root.children[0].ids.nav_drawer.set_state("close")

                def nav_drawer_open(self):
                    nav_drawer = self.root.children[0].ids.nav_drawer
                    nav_drawer.set_state("open")


            Example().run()
"""

__all__ = (
    "EZENavigationLayout",
    "EZENavigationDrawer",
    "EZENavigationDrawerItem",
    "EZENavigationDrawerMenu",
    "EZENavigationDrawerHeader",
    "EZENavigationDrawerLabel",
    "EZENavigationDrawerDivider",
)

import os
from typing import Union

from kivy.animation import Animation, AnimationTransition
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang import Builder
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.screenmanager import ScreenManager

from eze import uix_path
from eze.uix.behaviors.focus_behavior import FocusBehavior
from eze.uix.boxlayout import EZEBoxLayout
from eze.uix.card import EZECard
from eze.uix.floatlayout import EZEFloatLayout
from eze.uix.list import MDList, OneLineAvatarIconListItem
from eze.uix.scrollview import EZEScrollView
from eze.uix.toolbar import EZETopAppBar

with open(
    os.path.join(uix_path, "navigationdrawer", "navigationdrawer.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class NavigationDrawerContentError(Exception):
    pass


class EZENavigationLayout(EZEFloatLayout):
    """
    For more information, see in the
    :class:`~eze.uix.floatlayout.EZEFloatLayout` class documentation.
    """

    _scrim_color = ObjectProperty(None)
    _scrim_rectangle = ObjectProperty(None)
    _screen_manager = ObjectProperty(None)
    _navigation_drawer = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(width=self.update_pos)

    def update_pos(self, instance_navigation_drawer, pos_x: float) -> None:
        drawer = self._navigation_drawer
        manager = self._screen_manager
        if not drawer or not manager:
            return
        if drawer.type == "standard":
            manager.size_hint_x = None
            if drawer.anchor == "left":
                manager.x = drawer.width + drawer.x
                manager.width = self.width - manager.x
            else:
                manager.x = 0
                manager.width = drawer.x
        elif drawer.type == "modal":
            manager.size_hint_x = None
            manager.x = 0
            if drawer.anchor == "left":
                manager.width = self.width - manager.x
            else:
                manager.width = self.width

    def add_scrim(self, instance_manager: ScreenManager) -> None:
        with instance_manager.canvas.after:
            self._scrim_color = Color(rgba=[0, 0, 0, 0])
            self._scrim_rectangle = Rectangle(
                pos=instance_manager.pos, size=instance_manager.size
            )
            instance_manager.bind(
                pos=self.update_scrim_rectangle,
                size=self.update_scrim_rectangle,
            )

    def update_scrim_rectangle(
        self, instance_manager: ScreenManager, size: list
    ) -> None:
        self._scrim_rectangle.pos = self.pos
        self._scrim_rectangle.size = self.size

    def add_widget(self, widget, index=0, canvas=None):
        """
        Only two layouts are allowed:
        :class:`~kivy.uix.screenmanager.ScreenManager` and
        :class:`~EZENavigationDrawer`.
        """

        if not isinstance(
            widget, (EZENavigationDrawer, ScreenManager, EZETopAppBar)
        ):
            raise NavigationDrawerContentError(
                "The EZENavigationLayout must contain "
                "only `EZENavigationDrawer` and `ScreenManager`"
            )
        if isinstance(widget, ScreenManager):
            self._screen_manager = widget
            self.add_scrim(widget)
        if isinstance(widget, EZENavigationDrawer):
            self._navigation_drawer = widget
            widget.bind(
                x=self.update_pos, width=self.update_pos, anchor=self.update_pos
            )
        if len(self.children) > 3:
            raise NavigationDrawerContentError(
                "The EZENavigationLayout must contain "
                "only `EZENavigationDrawer` and `ScreenManager`"
            )
        return super().add_widget(widget)


class EZENavigationDrawerLabel(EZEBoxLayout):
    """
    Implements a label for a menu for :class:`~EZENavigationDrawer` class.

    For more information, see in the :class:`~eze.uix.boxlayout.EZEBoxLayout`
    class documentation.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZENavigationDrawer:

            EZENavigationDrawerMenu:

                EZENavigationDrawerLabel:
                    text: "Mail"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-label.png
        :align: center
    """

    text = StringProperty()
    """
    Text label.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    padding = VariableListProperty(["20dp", 0, 0, "8dp"])
    """
    Padding between layout box and children: [padding_left, padding_top,
    padding_right, padding_bottom].

    Padding also accepts a two argument form [padding_horizontal,
    padding_vertical] and a one argument form [padding].

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to `['20dp', 0, 0, '8dp']`.
    """


class EZENavigationDrawerDivider(EZEBoxLayout):
    """
    Implements a divider for a menu for :class:`~EZENavigationDrawer` class.

    For more information, see in the :class:`~eze.uix.boxlayout.EZEBoxLayout`
    class documentation.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZENavigationDrawer:

            EZENavigationDrawerMenu:

                EZENavigationDrawerLabel:
                    text: "Mail"

                EZENavigationDrawerDivider:

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-divider.png
        :align: center
    """

    padding = VariableListProperty(["20dp", "12dp", 0, "12dp"])
    """
    Padding between layout box and children: [padding_left, padding_top,
    padding_right, padding_bottom].

    Padding also accepts a two argument form [padding_horizontal,
    padding_vertical] and a one argument form [padding].

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to `['20dp', '12dp', 0, '12dp']`.
    """

    color = ColorProperty(None)
    """
    Divider color in (r, g, b, a) or string format.

    :attr:`color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class EZENavigationDrawerHeader(EZEBoxLayout):
    """
    Implements a header for a menu for :class:`~EZENavigationDrawer` class.

    For more information, see in the :class:`~eze.uix.boxlayout.MDBoxLayout`
    class documentation.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZENavigationDrawer:

            EZENavigationDrawerMenu:

                EZENavigationDrawerHeader:
                    title: "Header title"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-header.png
        :align: center
    """

    source = StringProperty()
    """
    Image logo path.

    .. code-block:: kv

        EZENavigationDrawer:

            EZENavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Header title"
                    text: "Header text"
                    source: "logo.png"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-header-source.png
        :align: center

    :attr:`source` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    title = StringProperty()
    """
    Title shown in the first line.

    :attr:`title` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    title_halign = StringProperty("left")
    """
    Title halign first line.

    :attr:`title_halign` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'left'`.
    """

    title_color = ColorProperty(None)
    """
    Title text color in (r, g, b, a) or string format.

    :attr:`title_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    title_font_style = StringProperty("H4")
    """
    Title shown in the first line.

    :attr:`title_font_style` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'H4'`.
    """

    title_font_size = StringProperty("34sp")
    """
    Title shown in the first line.

    :attr:`title_font_size` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'34sp'`.
    """

    text = StringProperty()
    """
    Text shown in the second line.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text_halign = StringProperty("left")
    """
    Text halign first line.

    :attr:`text_halign` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'left'`.
    """

    text_color = ColorProperty(None)
    """
    Title text color in (r, g, b, a) or string format.

    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_font_style = StringProperty("H6")
    """
    Title shown in the first line.

    :attr:`text_font_style` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'H6'`.
    """

    text_font_size = StringProperty("20sp")
    """
    Title shown in the first line.

    :attr:`text_font_size` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'20sp'`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.check_content)

    def check_content(self, interval: Union[int, float]) -> None:
        """Removes widgets that the user has not added to the container."""

        if not self.title:
            self.ids.label_box.remove_widget(self.ids.title)
        if not self.text:
            self.ids.label_box.remove_widget(self.ids.text)
        if not self.source:
            self.remove_widget(self.ids.logo)


class EZENavigationDrawerItem(OneLineAvatarIconListItem, FocusBehavior):
    """
    Implements an item for the :class:`~EZENavigationDrawer` menu list.

    For more information, see in the
    :class:`~eze.uix.list.OneLineAvatarIconListItem` and
    :class:`~eze.uix.behaviors.FocusBehavior`
    class documentation.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZENavigationDrawer:

            EZENavigationDrawerMenu:

                EZENavigationDrawerHeader:
                    title: "Header title"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                EZENavigationDrawerItem
                    icon: "gmail"
                    right_text: "+99"
                    text: "Inbox"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-item.png
        :align: center
    """

    selected = BooleanProperty(False)
    """
    Is the item selected.

    :attr:`selected` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    icon = StringProperty()
    """
    Icon item.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_color = ColorProperty(None)
    """
    Icon color in (r, g, b, a) or string format item.

    :attr:`icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    selected_color = ColorProperty([0, 0, 0, 1])
    """
    The color in (r, g, b, a) or string format of the icon and text of the
    selected item.

    :attr:`selected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 1]`.
    """

    right_text = StringProperty()
    """
    Right text item.

    :attr:`right_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text_right_color = ColorProperty(None)
    """
    Right text color item in (r, g, b, a) or string format.

    :attr:`text_right_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _text_color = None
    _text_right_color = None
    # eze.uix.navigationdrawer.navigationdrawer.EZENavigationDrawerMenu
    _drawer_menu = ObjectProperty()


class EZENavigationDrawerMenu(EZEScrollView):
    """
    Implements a scrollable list for menu items of the
    :class:` EZENavigationDrawer` class.

    For more information, see in the
    :class:`~eze.uix.scrollview.MDScrollView` class documentation.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        EZENavigationDrawer:

            EZENavigationDrawerMenu:

                # Your menu items.
                ...
    """

    spacing = NumericProperty(0)
    """
    Spacing between children, in pixels.

    :attr:`spacing` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, EZEList):
            return super().add_widget(widget, *args, **kwargs)
        else:
            if isinstance(widget, EZENavigationDrawerItem):
                widget._drawer_menu = self
            self.ids.menu.add_widget(widget)

    def reset_active_color(self, item: EZENavigationDrawerItem) -> None:
        for widget in self.ids.menu.children:
            if issubclass(widget.__class__, EZENavigationDrawerItem):
                if widget != item:
                    widget.selected = False
                else:
                    widget.selected = True

            if (
                issubclass(widget.__class__, EZENavigationDrawerItem)
                and widget != item
            ):
                if widget._text_color:
                    widget.text_color = widget._text_color


class EZENavigationDrawer(EZECard):
    type = OptionProperty("modal", options=("standard", "modal"))
    """
    Type of drawer. Modal type will be on top of screen. Standard type will be
    at left or right of screen. Also it automatically disables
    :attr:`close_on_click` and :attr:`enable_swiping` to prevent closing
    drawer for standard type.

    For more information, see in the :class:`~kivymd.uix.card.EZECard`
    class documentation.

    Standard
    --------

    .. code-block:: kv

        EZENavigationDrawer:
            type: "standard"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-standard.gif
        :align: center

    Modal
    -----

    .. code-block:: kv

        EZENavigationDrawer:
            type: "modal"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-modal.gif
        :align: center

    :attr:`type` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'modal'`.
    """

    anchor = OptionProperty("left", options=("left", "right"))
    """
    Anchoring screen edge for drawer. Set it to `'right'` for right-to-left
    languages. Available options are: `'left'`, `'right'`.

    Left
    ----

    .. code-block:: kv

        EZENavigationDrawer:
            anchor: "left"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-type-left.png
        :align: center

    Right
    -----

    .. code-block:: kv

        EZENavigationDrawer:
            anchor: "right"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-type-right.png
        :align: center

    :attr:`anchor` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'left'`.
    """

    # FIXME: Doesn't work in Kivy v2.1.0.
    scrim_color = ColorProperty([0, 0, 0, 0.6])
    """
    Color for scrim in (r, g, b, a) or string format. Alpha channel will be
    multiplied with :attr:`_scrim_alpha`. Set fourth channel to 0 if you want
    to disable scrim.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-scrim-color.png
        :align: center

    .. code-block:: kv

        EZENavigationDrawer:
            scrim_color: 0, 0, 0, .8
            # scrim_color: 0, 0, 0, .2

    :attr:`scrim_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.5]`.
    """

    padding = VariableListProperty([16, 16, 12, 16])
    """
    Padding between layout box and children: [padding_left, padding_top,
    padding_right, padding_bottom].

    Padding also accepts a two argument form [padding_horizontal,
    padding_vertical] and a one argument form [padding].

    .. versionchanged:: 1.0.0

    .. code-block:: kv

        EZENavigationDrawer:
            padding: 56, 56, 12, 16

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-padding.png
        :align: center

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty` and
    defaults to '[16, 16, 12, 16]'.
    """

    close_on_click = BooleanProperty(True)
    """
    Close when click on scrim or keyboard escape. It automatically sets to
    False for "standard" type.

    :attr:`close_on_click` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    state = OptionProperty("close", options=("close", "open"))
    """
    Indicates if panel closed or opened. Sets after :attr:`status` change.
    Available options are: `'close'`, `'open'`.

    :attr:`state` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'close'`.
    """

    status = OptionProperty(
        "closed",
        options=(
            "closed",
            "opening_with_swipe",
            "opening_with_animation",
            "opened",
            "closing_with_swipe",
            "closing_with_animation",
        ),
    )
    """
    Detailed state. Sets before :attr:`state`. Bind to :attr:`state` instead
    of :attr:`status`. Available options are: `'closed'`,
    `'opening_with_swipe'`, `'opening_with_animation'`, `'opened'`,
    `'closing_with_swipe'`, `'closing_with_animation'`.

    :attr:`status` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'closed'`.
    """

    open_progress = NumericProperty(0.0)
    """
    Percent of visible part of side panel. The percent is specified as a
    floating point number in the range 0-1. 0.0 if panel is closed and 1.0 if
    panel is opened.

    :attr:`open_progress` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    enable_swiping = BooleanProperty(True)
    """
    Allow to open or close navigation drawer with swipe. It automatically
    sets to False for "standard" type.

    :attr:`enable_swiping` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    swipe_distance = NumericProperty(10)
    """
    The distance of the swipe with which the movement of navigation drawer
    begins.

    :attr:`swipe_distance` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `10`.
    """

    swipe_edge_width = NumericProperty(20)
    """
    The size of the area in px inside which should start swipe to drag
    navigation drawer.

    :attr:`swipe_edge_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `20`.
    """

    def _get_scrim_alpha(self):
        _scrim_alpha = 0
        if self.type == "modal":
            _scrim_alpha = self._scrim_alpha_transition(self.open_progress)
        if (
            isinstance(self.parent, EZENavigationLayout)
            and self.parent._scrim_color
        ):
            self.parent._scrim_color.rgba = self.scrim_color[:3] + [
                self.scrim_color[3] * _scrim_alpha
            ]
        return _scrim_alpha

    _scrim_alpha = AliasProperty(
        _get_scrim_alpha,
        None,
        bind=("_scrim_alpha_transition", "open_progress", "scrim_color"),
    )
    """
    Multiplier for alpha channel of :attr:`scrim_color`. For internal
    usage only.
    """

    scrim_alpha_transition = StringProperty("linear")
    """
    The name of the animation transition type to use for changing
    :attr:`scrim_alpha`.

    :attr:`scrim_alpha_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    def _get_scrim_alpha_transition(self):
        return getattr(AnimationTransition, self.scrim_alpha_transition)

    _scrim_alpha_transition = AliasProperty(
        _get_scrim_alpha_transition,
        None,
        bind=("scrim_alpha_transition",),
        cache=True,
    )

    opening_transition = StringProperty("out_cubic")
    """
    The name of the animation transition type to use when animating to
    the :attr:`state` `'open'`.

    :attr:`opening_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    opening_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'open'`.

    :attr:`opening_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    closing_transition = StringProperty("out_sine")
    """The name of the animation transition type to use when animating to
    the :attr:`state` 'close'.

    :attr:`closing_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_sine'`.
    """

    closing_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'close'`.

    :attr:`closing_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(
            open_progress=self.update_status,
            status=self.update_status,
            state=self.update_status,
        )
        Window.bind(on_keyboard=self._handle_keyboard)

    def set_state(self, new_state="toggle", animation=True) -> None:
        """
        Change state of the side panel.
        New_state can be one of `"toggle"`, `"open"` or `"close"`.
        """

        if new_state == "toggle":
            new_state = "close" if self.state == "open" else "open"

        if new_state == "open":
            Animation.cancel_all(self, "open_progress")
            self.status = "opening_with_animation"
            if animation:
                Animation(
                    open_progress=1.0,
                    d=self.opening_time * (1 - self.open_progress),
                    t=self.opening_transition,
                ).start(self)
            else:
                self.open_progress = 1
        else:  # "close"
            Animation.cancel_all(self, "open_progress")
            self.status = "closing_with_animation"
            if animation:
                Animation(
                    open_progress=0.0,
                    d=self.closing_time * self.open_progress,
                    t=self.closing_transition,
                ).start(self)
            else:
                self.open_progress = 0

    def update_status(self, *_) -> None:
        status = self.status
        if status == "closed":
            self.state = "close"
        elif status == "opened":
            self.state = "open"
        elif self.open_progress == 1 and status == "opening_with_animation":
            self.status = "opened"
            self.state = "open"
        elif self.open_progress == 0 and status == "closing_with_animation":
            self.status = "closed"
            self.state = "close"
        elif status in (
            "opening_with_swipe",
            "opening_with_animation",
            "closing_with_swipe",
            "closing_with_animation",
        ):
            pass
        if self.status == "closed":
            self.opacity = 0
        else:
            self.opacity = 1

    def get_dist_from_side(self, x: float) -> float:
        if self.anchor == "left":
            return 0 if x < 0 else x
        return 0 if x > Window.width else Window.width - x

    def on_touch_down(self, touch):
        if self.status == "closed":
            return False
        elif self.status == "opened":
            for child in self.children[:]:
                if child.dispatch("on_touch_down", touch):
                    return True
        if self.type == "standard" and not self.collide_point(
            touch.ox, touch.oy
        ):
            return False
        return True

    def on_touch_move(self, touch):
        if self.enable_swiping:
            if self.status == "closed":
                if (
                    self.get_dist_from_side(touch.ox) <= self.swipe_edge_width
                    and abs(touch.x - touch.ox) > self.swipe_distance
                ):
                    self.status = "opening_with_swipe"
            elif self.status == "opened":
                if abs(touch.x - touch.ox) > self.swipe_distance:
                    self.status = "closing_with_swipe"

        if self.status in ("opening_with_swipe", "closing_with_swipe"):
            self.open_progress = max(
                min(
                    self.open_progress
                    + (touch.dx if self.anchor == "left" else -touch.dx)
                    / self.width,
                    1,
                ),
                0,
            )
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.status == "opening_with_swipe":
            if self.open_progress > 0.5:
                self.set_state("open", animation=True)
            else:
                self.set_state("close", animation=True)
        elif self.status == "closing_with_swipe":
            if self.open_progress < 0.5:
                self.set_state("close", animation=True)
            else:
                self.set_state("open", animation=True)
        elif self.status == "opened":
            if self.close_on_click and not self.collide_point(
                touch.ox, touch.oy
            ):
                self.set_state("close", animation=True)
            elif self.type == "standard" and not self.collide_point(
                touch.ox, touch.oy
            ):
                return False
        elif self.status == "closed":
            return False
        return True

    def on_radius(self, instance_navigation_drawer, radius_value: list) -> None:
        self._radius = radius_value

    def on_type(self, instance_navigation_drawer, drawer_type: str) -> None:
        if self.type == "standard":
            self.enable_swiping = False
            self.close_on_click = False
        else:
            self.enable_swiping = True
            self.close_on_click = True

    def _handle_keyboard(self, window, key, *largs):
        if key == 27 and self.status == "opened" and self.close_on_click:
            self.set_state("close")
            return True
