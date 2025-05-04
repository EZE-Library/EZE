"""
Components/Menu
===============

.. seealso::

    `Material Design spec, Menus <https://m3.material.io/components/menus/overview>`_

.. rubric:: Menus display a list of choices on temporary surfaces.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-preview.png
    :align: center

- Menus should be easy to open, close, and interact with
- Menu content should be suited to user needs
- Menu items should be easy to scan

Usage
-----

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp

    from eze.app import EZEApp
    from eze.uix.menu import EZEDropdownMenu

    KV = '''
    EZEScreen:

        EZERaisedButton:
            id: button
            text: "Press me"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu_open()
    '''


    class Test(EZEApp):
        def menu_open(self):
            menu_items = [
                {
                    "text": f"Item {i}",
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            EZEDropdownMenu(
                caller=self.root.ids.button, items=menu_items
            ).open()

        def menu_callback(self, text_item):
            print(text_item)

        def build(self):
            self.theme_cls.primary_palette = "Orange"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-usage.gif
    :align: center

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-anatomy.png
    :align: center

You can combine the following parameters:
-----------------------------------------

- leading_icon
- text
- trailing_icon
- trailing_text

...to create the necessary types of menu items:

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
            "trailing_icon": "apple-keyboard-command",
            "trailing_text": "+Shift+X",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-leading-icon-trailing-icon-trailing-text.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "trailing_icon": "apple-keyboard-command",
            "trailing_text": "+Shift+X",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-trailing-icon-trailing-text.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "trailing_icon": "apple-keyboard-command",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-trailing-icon.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "trailing_text": "Shift+X",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-trailing-text.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
            "trailing_icon": "apple-keyboard-command",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-leading-icon-trailing-icon.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-leading-icon.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
            "trailing_text": "Shift+X",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-leading-icon-trailing-text.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-text.png
    :align: center

You can use the following parameters to customize the menu items:
-----------------------------------------------------------------

- text_color
- leading_icon_color
- trailing_icon_color
- trailing_text_color

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
            "trailing_icon": "apple-keyboard-command",
            "trailing_text": "+Shift+X",
            "leading_icon_color": "orange",
            "trailing_icon_color": "green",
            "trailing_text_color": "red",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-customize.png
    :align: center

.. Header:
Header
------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp

    from eze.app import EZEApp
    from eze.uix.menu import EZEDropdownMenu
    from eze.uix.boxlayout import EZEBoxLayout

    KV = '''
    <MenuHeader>
        spacing: "12dp"
        padding: "4dp"
        adaptive_height: True

        EZEIconButton:
            icon: "gesture-tap-button"
            pos_hint: {"center_y": .5}

        EZELabel:
            text: "Actions"
            adaptive_size: True
            pos_hint: {"center_y": .5}


    EZEScreen:

        EZERaisedButton:
            id: button
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu.open()
    '''


    class MenuHeader(EZEBoxLayout):
        '''An instance of the class that will be added to the menu header.'''


    class Test(EZEApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            self.menu = EZEDropdownMenu(
                header_cls=MenuHeader(),
                caller=self.screen.ids.button,
                items=menu_items,
            )

        def menu_callback(self, text_item):
            print(text_item)

        def build(self):
            self.theme_cls.primary_palette = "Orange"
            self.theme_cls.theme_style = "Dark"
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-header.png
    :align: center

Menu with EZETopAppBar
---------------------

The :class:`~EZEDropdownMenu` works well with the standard
:class:`~eze.uix.toolbar.EZETopAppBar`. Since the buttons on the Toolbar are created
by the EZETopAppBar component, it is necessary to pass the button as an argument to
the callback using `lambda x: app.callback(x)`. This example uses drop down menus
for both the righthand and lefthand menus.

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp

    from eze.app import EZEApp
    from eze.uix.menu import EZEDropdownMenu
    from eze.uix.snackbar import Snackbar

    KV = '''
    EZEBoxLayout:
        orientation: "vertical"

        EZETopAppBar:
            title: "EZETopAppBar"
            left_action_items: [["menu", lambda x: app.callback(x)]]
            right_action_items: [["dots-vertical", lambda x: app.callback(x)]]

        EZELabel:
            text: "Content"
            halign: "center"
    '''


    class Test(EZEApp):
        def build(self):
            self.theme_cls.primary_palette = "Orange"
            self.theme_cls.theme_style = "Dark"
            menu_items = [
                {
                    "text": f"Item {i}",
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            self.menu = EZEDropdownMenu(items=menu_items)
            return Builder.load_string(KV)

        def callback(self, button):
            self.menu.caller = button
            self.menu.open()

        def menu_callback(self, text_item):
            self.menu.dismiss()
            Snackbar(text=text_item).open()


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-menu.png
    :align: center

.. Position:
Position
========

Bottom position
---------------

.. seealso::

    :attr:`~EZEDropdownMenu.position`

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp

    from eze.app import EZEApp
    from eze.uix.menu import EZEDropdownMenu

    KV = '''
    EZEScreen:

        EZETextField:
            id: field
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: None
            width: "200dp"
            hint_text: "Password"
            on_focus: if self.focus: app.menu.open()
    '''


    class Test(EZEApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "on_release": lambda x=f"Item {i}": self.set_item(x),
                } for i in range(5)]
            self.menu = EZEDropdownMenu(
                caller=self.screen.ids.field,
                items=menu_items,
                position="bottom",
            )

        def set_item(self, text_item):
            self.screen.ids.field.text = text_item
            self.menu.dismiss()

        def build(self):
            self.theme_cls.primary_palette = "Orange"
            self.theme_cls.theme_style = "Dark"
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-position.png
    :align: center

Center position
---------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp

    from eze.app import EZEApp
    from eze.uix.menu import EZEDropdownMenu

    KV = '''
    EZEScreen:

        EZEDropDownItem:
            id: drop_item
            pos_hint: {'center_x': .5, 'center_y': .5}
            text: 'Item 0'
            on_release: app.menu.open()
    '''


    class Test(EZEApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "on_release": lambda x=f"Item {i}": self.set_item(x),
                } for i in range(5)
            ]
            self.menu = EZEDropdownMenu(
                caller=self.screen.ids.drop_item,
                items=menu_items,
                position="center",
            )
            self.menu.bind()

        def set_item(self, text_item):
            self.screen.ids.drop_item.set_item(text_item)
            self.menu.dismiss()

        def build(self):
            self.theme_cls.primary_palette = "Orange"
            self.theme_cls.theme_style = "Dark"
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-position-center.gif
    :align: center

API break
=========

1.1.1 version
-------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp
    from kivy.properties import StringProperty

    from eze.app import EZEApp
    from eze.uix.boxlayout import EZEBoxLayout
    from eze.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
    from eze.uix.menu import EZEDropdownMenu

    KV = '''
    <RightContentCls>
        disabled: True
        adaptive_size: True
        pos_hint: {"center_y": .5}

        EZEIconButton:
            icon: root.icon
            icon_size: "16sp"
            eze_bg_color_disabled: 0, 0, 0, 0

        EZELabel:
            text: root.text
            font_style: "Caption"
            adaptive_size: True
            pos_hint: {"center_y": .5}


    <Item>

        IconLeftWidget:
            icon: root.left_icon

        RightContentCls:
            id: container
            icon: root.right_icon
            text: root.right_text


    EZEScreen:

        EZERaisedButton:
            id: button
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu.open()
    '''


    class RightContentCls(IRightBodyTouch, EZEBoxLayout):
        icon = StringProperty()
        text = StringProperty()


    class Item(OneLineAvatarIconListItem):
        left_icon = StringProperty()
        right_icon = StringProperty()
        right_text = StringProperty()


    class Test(EZEApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "right_text": "+Shift+X",
                    "right_icon": "apple-keyboard-command",
                    "left_icon": "web",
                    "viewclass": "Item",
                    "height": dp(54),
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            self.menu = EZEDropdownMenu(
                caller=self.screen.ids.button,
                items=menu_items,
                bg_color="#bdc6b0",
                width_mult=4,
            )

        def menu_callback(self, text_item):
            print(text_item)

        def build(self):
            return self.screen


    Test().run()

1.2.0 version
-------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp

    from eze.app import EZEApp
    from eze.uix.menu import EZEDropdownMenu

    KV = '''
    EZEScreen:

        EZERaisedButton:
            id: button
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu.open()
    '''


    class Test(EZEApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "leading_icon": "web",
                    "trailing_icon": "apple-keyboard-command",
                    "trailing_text": "+Shift+X",
                    "trailing_icon_color": "grey",
                    "trailing_text_color": "grey",
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            self.menu = EZEDropdownMenu(
                md_bg_color="#bdc6b0",
                caller=self.screen.ids.button,
                items=menu_items,
            )

        def menu_callback(self, text_item):
            print(text_item)

        def build(self):
            return self.screen


    Test().run()
"""

from __future__ import annotations

__all__ = (
    "BaseDropdownItem",
    "EZEDropdownMenu",
    "EZEDropdownTextItem",
    "EZEDropdownLeadingIconItem",
    "EZEDropdownTrailingIconItem",
    "EZEDropdownTrailingIconTextItem",
    "EZEDropdownTrailingTextItem",
    "EZEDropdownLeadingTrailingIconTextItem",
    "EZEDropdownLeadingIconTrailingTextItem",
)

import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    VariableListProperty,
    StringProperty,
)
from kivy.uix.recycleview import RecycleView

import eze.material_resources as m_res
from eze import uix_path
from eze.uix.behaviors import StencilBehavior, RectangularRippleBehavior
from eze.uix.behaviors.motion_behavior import MotionDropDownMenuBehavior
from eze.uix.boxlayout import EZEBoxLayout
from eze.uix.card import EZECard
from eze.uix.label import EZELabel
from eze.uix.list import IRightBody

with open(
    os.path.join(uix_path, "menu", "menu.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class EZEMenu(RecycleView):
    width_mult = NumericProperty(1)
    """
    See :attr:`~EZEDropdownMenu.width_mult`.

    .. deprecated:: 1.2.0
    """

    drop_cls = ObjectProperty()
    """
    See :class:`~EZEDropdownMenu` class.
    """


class BaseDropdownItem(RectangularRippleBehavior, ButtonBehavior, EZEBoxLayout):
    """
    Base class for menu items.

    .. versionadded:: 1.2.0

    For more information, see in the
    :class:`~eze.uix.behaviors.RectangularRippleBehavior` and
    :class:`~eze.uix.boxlayout.EZEBoxLayout` classes.
    """

    text = StringProperty()
    """
    The text of the menu item.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    leading_icon = StringProperty()
    """
    The leading icon of the menu item.

    :attr:`leading_icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    trailing_icon = StringProperty()
    """
    The trailing icon of the menu item.

    :attr:`trailing_icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    trailing_text = StringProperty()
    """
    The trailing text of the menu item.

    :attr:`trailing_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text_color = ColorProperty(None)
    """
    The color of the text in (r, g, b, a) or string format for the text of the
    menu item.

    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    leading_icon_color = ColorProperty(None)
    """
    The color of the text in (r, g, b, a) or string format for the leading icon
    of the menu item.

    :attr:`leading_icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    trailing_icon_color = ColorProperty(None)
    """
    The color of the text in (r, g, b, a) or string format for the trailing
    icon of the menu item.

    :attr:`leading_icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    trailing_text_color = ColorProperty(None)
    """
    The color of the text in (r, g, b, a) or string format for the trailing
    text of the menu item.

    :attr:`leading_icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    divider = OptionProperty("Full", options=["Full", None], allownone=True)
    """
    Divider mode. Available options are: `'Full'`, `None`
    and default to `'Full'`.

    :attr:`divider` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'Full'`.
    """

    divider_color = ColorProperty(None)
    """
    Divider color in (r, g, b, a) or string format.

    :attr:`divider_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class EZETrailingTextContainer(BaseDropdownItem, IRightBody, EZELabel):
    """
    Implements a container for trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the
    :class:`~BaseDropdownItem` and
    :class:`~eze.uix.list.IRightBody` and
    :class:`~eze.uix.label.EZELabel` classes.
    """


class EZETrailingIconTextContainer(BaseDropdownItem, IRightBody, EZEBoxLayout):
    """
    Implements a container for trailing icons and trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the
    :class:`~BaseDropdownItem` and
    :class:`~eze.uix.list.IRightBody` and
    :class:`~eze.uix.boxlayout.MDBoxLayout` classes.
    """


class EZEDropdownTextItem(BaseDropdownItem):
    """
    Implements a menu item with text without leading and trailing icons.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class EZEDropdownLeadingIconItem(BaseDropdownItem):
    """
    Implements a menu item with text, leading icon and without trailing icon.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class EZEDropdownTrailingIconItem(BaseDropdownItem):
    """
    Implements a menu item with text, without leading icon and with trailing
    icon.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class EZEDropdownTrailingIconTextItem(BaseDropdownItem):
    """
    Implements a menu item with text, without leading icon, with trailing
    icon and with trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class EZEDropdownTrailingTextItem(BaseDropdownItem):
    """
    Implements a menu item with text, without leading icon, without trailing
    icon and with trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class EZEDropdownLeadingIconTrailingTextItem(BaseDropdownItem):
    """
    Implements a menu item with text, leading icon and with trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class EZEDropdownLeadingTrailingIconTextItem(BaseDropdownItem):
    """
    Implements a menu item with text, with leading icon, with trailing
    icon and with trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class EZEDropdownLeadingTrailingIconItem(BaseDropdownItem):
    """
    Implements a menu item with text, with leading icon, with trailing icon.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class EZEDropdownMenu(MotionDropDownMenuBehavior, StencilBehavior, EZECard):
    """
    Dropdown menu class.

    For more information, see in the
    :class:`~eze.uix.behaviors.MotionDropDownMenuBehavior` and
    :class:`~eze.uix.behaviors.StencilBehavior` and
    :class:`~eze.uix.card.EZECard`
    classes documentation.

    :Events:
        `on_release`
            The method that will be called when you click menu items.
    """

    header_cls = ObjectProperty()
    """
    An instance of the class (`Kivy`, `KivyMD` or 'EZE' widget) that will be added
    to the menu header.

    .. versionadded:: 0.104.2

    See Header_ for more information.

    :attr:`header_cls` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    items = ListProperty()
    """
    List of dictionaries with properties for menu items.

    :attr:`items` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    width_mult = NumericProperty(1, deprecated=True)
    """
    This number multiplied by the standard increment ('56dp' on mobile, '64dp'
    on desktop), determines the width of the menu items.

    If the resulting number were to be too big for the application Window,
    the multiplier will be adjusted for the biggest possible one.

    .. deprecated:: 1.2.0

        Use `width` instead.

        .. code-block:: python

            self.menu = EZEDropdownMenu(
                width=dp(240),
                ...,
            )

    :attr:`width_mult` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    min_height = NumericProperty(dp(48))

    max_height = NumericProperty()
    """
    The menu will grow no bigger than this number. Set to 0 for no limit.

    :attr:`max_height` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    border_margin = NumericProperty("4dp")
    """
    Margin between Window border and menu.

    .. code-block:: python

        self.menu = EZEDropdownMenu(
            border_margin=dp(24),
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-border-margin-24.png
        :align: center

    :attr:`border_margin` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `4dp`.
    """

    ver_growth = OptionProperty(None, allownone=True, options=["up", "down"])
    """
    Where the menu will grow vertically to when opening. Set to `None` to let
    the widget pick for you. Available options are: `'up'`, `'down'`.

    .. code-block:: python

        self.menu = EZEDropdownMenu(
            ver_growth="up",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-ver-growth-up.png
        :align: center

    .. code-block:: python

        self.menu = EZEDropdownMenu(
            ver_growth="down",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-ver-growth-down.png
        :align: center

    :attr:`ver_growth` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    hor_growth = OptionProperty(None, allownone=True, options=["left", "right"])
    """
    Where the menu will grow horizontally to when opening. Set to `None` to let
    the widget pick for you. Available options are: `'left'`, `'right'`.

    .. code-block:: python

        self.menu = EZEDropdownMenu(
            hor_growth="left",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-hor-growth-left.png
        :align: center

    .. code-block:: python

        self.menu = EZEDropdownMenu(
            hor_growth="right",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-hor-growth-right.png
        :align: center

    :attr:`hor_growth` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    background_color = ColorProperty(None, deprecated=True)
    """
    Color in (r, g, b, a) or string format of the background of the menu.

    .. deprecated:: 1.2.0

        Use `eze_bg_color` instead.

    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    caller = ObjectProperty()
    """
    The widget object that calls the menu window.

    :attr:`caller` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    position = OptionProperty(
        "auto", options=["top", "auto", "center", "bottom"]
    )
    """
    Menu window position relative to parent element.
    Available options are: `'auto'`, `'top'`, `'center'`, `'bottom'`.

    See Position_ for more information.

    :attr:`position` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'auto'`.
    """

    radius = VariableListProperty([dp(7)])
    """
    Menu radius.

    :attr:`radius` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to `'[dp(7)]'`.
    """

    elevation = NumericProperty(m_res.DROP_DOWN_MENU_ELEVATION)
    """
    See :attr:`eze.uix.behaviors.elevation.CommonElevationBehavior.elevation`
    attribute.

    :attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2`.
    """

    shadow_radius = VariableListProperty([6], length=4)
    """
    See :attr:`eze.uix.behaviors.elevation.CommonElevationBehavior.shadow_radius`
    attribute.

    :attr:`shadow_radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[6]`.
    """

    shadow_softness = NumericProperty(m_res.DROP_DOWN_MENU_SOFTNESS)
    """
    See :attr:`eze.uix.behaviors.elevation.CommonElevationBehavior.shadow_softness`
    attribute.

    :attr:`shadow_softness` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `6`.
    """

    shadow_offset = ListProperty(m_res.DROP_DOWN_MENU_OFFSET)
    """
    See :attr:`eze.uix.behaviors.elevation.CommonElevationBehavior.shadow_offset`
    attribute.

    :attr:`shadow_offset` is an :class:`~kivy.properties.ListProperty`
    and defaults to `(0, -2)`.
    """

    _items = []
    _start_coords = []
    _tar_x = 0
    _tar_y = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(
            on_resize=self._remove_menu,
            on_maximize=self._remove_menu,
            on_restore=self._remove_menu,
        )
        self.register_event_type("on_dismiss")
        self.menu = self.ids.md_menu
        self.target_height = 0

    def adjust_width(self) -> None:
        """
        Adjust the width of the menu if the width of the menu goes beyond
        the boundaries of the parent window from  starting point.
        """

        if self._start_coords[0] >= Window.width / 2:
            if self.width > self._start_coords[0]:
                self.width = (
                    self._start_coords[0]
                    - self.border_margin
                    - (
                        (self.caller.width / 2 + self.border_margin)
                        if self.position in ["right", "left"]
                        else 0
                    )
                )
        else:
            if Window.width - self._start_coords[0] < self.width:
                self.width = (
                    Window.width - self._start_coords[0] - self.border_margin
                )

    def check_ver_growth(self) -> None:
        """
        Checks whether the height of the lower/upper borders of the menu
        exceeds the limits borders of the parent window.
        """

        if self.target_height > self._start_coords[1] - self.border_margin:
            self.ver_growth = "up"
        else:
            if self._start_coords[1] > Window.height - self._start_coords[1]:
                self.ver_growth = "down"

    def check_hor_growth(self) -> None:
        """
        Checks whether the width of the left/right menu borders exceeds the
        boundaries of the parent window.
        """

        if (
            Window.width - (self._start_coords[0] + self.border_margin)
            <= self.width
        ):
            self.hor_growth = "left"
        elif self.width >= self._start_coords[0] + self.border_margin:
            self.hor_growth = "right"

    def get_target_pos(self) -> [float, float]:
        self._tar_x, self._tar_y = self._start_coords

        if self.ver_growth == "up":
            self._tar_y = self._start_coords[1] + self.height
        else:
            self._tar_y = self._start_coords[1]

        if self.hor_growth == "left":
            self._tar_x = self._start_coords[0] - self.width
        else:
            self._tar_x = self._start_coords[0]

        return self._tar_x, self._tar_y

    def set_target_height(self) -> None:
        """
        Set the target height of the menu depending on the size of each item.
        """

        self.target_height = 0
        for item in self.menu.data:
            self.target_height += item.get("height", self.min_height)

        if 0 < self.max_height < self.target_height:
            self.target_height = self.max_height

        if self._start_coords[1] >= Window.height / 2:
            if self.target_height > self._start_coords[1]:
                self.target_height = (
                    self._start_coords[1]
                    - self.border_margin
                    - (
                        (self.caller.height / 2 + self.border_margin)
                        if self.position in ["top", "bottom"]
                        else 0
                    )
                )
        else:
            if Window.height - self._start_coords[1] < self.target_height:
                self.target_height = (
                    Window.height - self._start_coords[1] - self.border_margin
                )

    def set_menu_properties(self, *args) -> None:
        """Sets the size and position for the menu window."""

        if self.caller:
            self.menu.data = self._items
            # We need to pick a starting point, see how big we need to be,
            # and where to grow to.
            self._start_coords = self.caller.to_window(*self.caller.center)

            self.adjust_width()
            self.set_target_height()
            self.check_ver_growth()
            self.check_hor_growth()

    def set_menu_pos(self, *args) -> None:
        if self.position == "auto":
            self.menu.x = self._tar_x
            self.menu.y = self._tar_y - (
                self.header_cls.height if self.header_cls else 0
            )
        else:
            if self.position == "center":
                self.pos = (
                    self._start_coords[0] - self.width / 2,
                    self._start_coords[1] - self.height / 2,
                )
            elif self.position == "bottom":
                self.pos = (
                    (self._start_coords[0] - self.width / 2)
                    if not self.hor_growth
                    else (
                        (self._start_coords[0] - self.width)
                        if self.hor_growth == "left"
                        else (self._start_coords[0])
                    ),
                    self._start_coords[1]
                    - (
                        self.height
                        + self.border_margin
                        + self.caller.height / 2
                    ),
                )
            elif self.position == "top":
                self.pos = (
                    (self._start_coords[0] - self.width / 2)
                    if not self.hor_growth
                    else (
                        (self._start_coords[0] - self.width)
                        if self.hor_growth == "left"
                        else (self._start_coords[0])
                    ),
                    self._start_coords[1]
                    + self.caller.height / 2
                    + self.border_margin,
                )

    def adjust_position(self) -> str:
        """
        Return value 'auto' for the menu position if the menu position is out
        of screen.
        """

        position = self.position

        if position == "bottom":
            if (
                self._start_coords[1]
                - (self.height + self.border_margin + self.caller.height / 2)
                < 0
            ):
                position = "auto"
        elif position == "top":
            if (
                self._start_coords[1]
                + self.caller.height / 2
                + self.border_margin
                > Window.height
            ):
                position = "auto"
        elif position == "center":
            if (
                (
                    self._start_coords[1] + self.height / 2 > Window.height
                    or self._start_coords[1] - self.height / 2 < 0
                )
                or Window.width - (self._start_coords[0] + self.border_margin)
                < self.width / 2
                or self._start_coords[0] + self.border_margin < self.width / 2
            ):
                position = "auto"

        return position

    def open(self) -> None:
        """Animate the opening of a menu window."""

        self.set_menu_properties()
        Window.add_widget(self)
        self.position = self.adjust_position()

        if self.width <= 100:
            self.width = dp(240)

        self.height = self.target_height
        self._tar_x, self._tar_y = self.get_target_pos()
        self.x = self._tar_x
        self.y = self._tar_y - self.target_height
        self.scale_value_center = self.caller.center
        self.set_menu_pos()
        self.on_open()

    def on_items(self, instance, value: list) -> None:
        """
        The method sets the class that will be used to create the menu item.
        """

        items = []
        viewclass = "EZEDropdownTextItem"

        for data in value:
            if "viewclass" not in data:
                if (
                    "leading_icon" not in data
                    and "trailing_icon" not in data
                    and "trailing_text" not in data
                ):
                    viewclass = "EZEDropdownTextItem"
                elif (
                    "leading_icon" in data
                    and "trailing_icon" not in data
                    and "trailing_text" not in data
                ):
                    viewclass = "EZEDropdownLeadingIconItem"
                elif (
                    "leading_icon" not in data
                    and "trailing_icon" in data
                    and "trailing_text" not in data
                ):
                    viewclass = "EZEDropdownTrailingIconItem"
                elif (
                    "leading_icon" not in data
                    and "trailing_icon" in data
                    and "trailing_text" in data
                ):
                    viewclass = "EZEDropdownTrailingIconTextItem"
                elif (
                    "leading_icon" in data
                    and "trailing_icon" in data
                    and "trailing_text" in data
                ):
                    viewclass = "EZEDropdownLeadingTrailingIconTextItem"
                elif (
                    "leading_icon" in data
                    and "trailing_icon" in data
                    and "trailing_text" not in data
                ):
                    viewclass = "EZEDropdownLeadingTrailingIconItem"
                elif (
                    "leading_icon" not in data
                    and "trailing_icon" not in data
                    and "trailing_text" in data
                ):
                    viewclass = "MDDropdownTrailingTextItem"
                elif (
                    "leading_icon" in data
                    and "trailing_icon" not in data
                    and "trailing_text" in data
                ):
                    viewclass = "EZEDropdownLeadingIconTrailingTextItem"

                data["viewclass"] = viewclass

            if "height" not in data:
                data["height"] = dp(48)

            items.append(data)

        self._items = items

    def on_header_cls(
        self, instance_dropdown_menu, instance_user_menu_header
    ) -> None:
        """Called when a value is set to the :attr:`header_cls` parameter."""

        def add_content_header_cls(interval):
            self.ids.content_header.clear_widgets()
            self.ids.content_header.add_widget(instance_user_menu_header)

        Clock.schedule_once(add_content_header_cls, 1)

    def on_touch_down(self, touch):
        if not self.menu.collide_point(*touch.pos):
            self.dispatch("on_dismiss")
            return True
        super().on_touch_down(touch)
        return True

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        return True

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        return True

    def dismiss(self, *args) -> None:
        """Closes the menu."""

        self.on_dismiss()

    def _remove_menu(self, *args):
        Window.remove_widget(self)
        self.set_scale()


if __name__ == "__main__":
    # To test the correct menu position.
    from kivy.lang import Builder
    from kivy.metrics import dp

    from eze.app import EZEApp
    from eze.uix.button import EZERaisedButton
    from eze.uix.screen import EZEScreen

    class Test(EZEApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = EZEScreen()
            menu_items = [{"text": f"Item {i}"} for i in range(55)]
            self.menu = EZEDropdownMenu(items=menu_items, width_mult=4)

        def open_menu(self, caller):
            self.menu.caller = caller
            self.menu.open()

        def on_start(self):
            pos_hints = [
                {"top": 1, "left": 0.1},
                {"top": 1, "center_x": 0.5},
                {"top": 1, "right": 1},
                {"center_y": 0.5, "left": 1},
                {"bottom": 1, "left": 1},
                {"bottom": 1, "center_x": 0.5},
                {"bottom": 1, "right": 1},
                {"center_y": 0.5, "right": 1},
                {"center_y": 0.5, "center_x": 0.5},
            ]
            for pos_hint in pos_hints:
                self.screen.add_widget(
                    EZERaisedButton(pos_hint=pos_hint, on_release=self.open_menu)
                )

        def build(self):
            return self.screen

    Test().run()
