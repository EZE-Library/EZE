"""
Themes/Theming
==============

.. seealso::

   `EZE Design spec, Material theming <https://material.io/design/material-theming>`_

EZE App
------------

The main class of your application, which in `Kivy` inherits from the
:class:`~kivy.app.App` class, in `EZE` must inherit from the
:class:`~eze.app.EZEApp` class. The :class:`~eze.app.EZEApp` class has
properties that allow you to control application properties such as
:attr:`color/style/font` of interface elements and much more.

Control material properties
---------------------------

The main application class inherited from the :class:`~eze.app.EZEApp` class
has the :attr:`~eze.app.EZEApp.theme_cls` attribute, with which you control
the material properties of your application.

Changing the theme colors
-------------------------

The standard theme_cls is designed to provide the standard themes and colors as
defined by Material Design.

We do not recommend that you change this.

However, if you do need to change the standard colors, for instance to meet branding
guidelines, you can do this by overloading the `color_definitions.py` object.

Create a custom color defintion object. This should have the same format as
the colors object in `color_definitions.py` and contain definitions for at least the
primary color, the accent color and the Light and Dark backgrounds.

.. note:: Your custom colors *must* use the names of the
    `existing colors as defined in the palette `_
    e.g. You can have `Blue` but you cannot have `NavyBlue`.

Add the custom theme to the :class:`~eze.app.EZEApp` as shown in the
following snippet.

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import ObjectProperty

            from eze.app import EZEApp
            from eze.uix.floatlayout import EZEFloatLayout
            from eze.uix.tab import EZETabsBase
            from eze.icon_definitions import eze_icons

            colors = {
                "Teal": {
                    "200": "#212121",
                    "500": "#212121",
                    "700": "#212121",
                },
                "Red": {
                    "200": "#C25554",
                    "500": "#C25554",
                    "700": "#C25554",
                },
                "Light": {
                    "StatusBar": "E0E0E0",
                    "AppBar": "#202020",
                    "Background": "#2E3032",
                    "CardsDialogs": "#FFFFFF",
                    "FlatButtonDown": "#CCCCCC",
                },
            }


            KV = '''
            EZEBoxLayout:
                orientation: "vertical"

                EZETopAppBar:
                    title: "Custom theme"

                EZETabs:
                    id: tabs


            <Tab>

                EZEIconButton:
                    id: icon
                    icon: root.icon
                    icon_size: "48sp"
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    pos_hint: {"center_x": .5, "center_y": .5}
            '''


            class Tab(EZEFloatLayout, EZETabsBase):
                '''Class implementing content for a tab.'''

                icon = ObjectProperty()


            class Example(EZEApp):
                icons = list(eze_icons.keys())[15:30]

                def build(self):
                    self.theme_cls.colors = colors
                    self.theme_cls.primary_palette = "Teal"
                    self.theme_cls.accent_palette = "Red"
                    return Builder.load_string(KV)

                def on_start(self):
                    for name_tab in self.icons:
                        tab = Tab(title="This is " + name_tab, icon=name_tab)
                        self.root.ids.tabs.add_widget(tab)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.properties import ObjectProperty

            from eze.app import EZEApp
            from eze.uix.boxlayout import EZEBoxLayout
            from eze.uix.button import EZEIconButton
            from eze.uix.floatlayout import EZEFloatLayout
            from eze.uix.tab import EZETabsBase, EZETabs
            from eze.icon_definitions import eze_icons
            from eze.uix.toolbar import EZETopAppBar

            colors = {
                "Teal": {
                    "200": "#212121",
                    "500": "#212121",
                    "700": "#212121",
                },
                "Red": {
                    "200": "#C25554",
                    "500": "#C25554",
                    "700": "#C25554",
                },
                "Light": {
                    "StatusBar": "E0E0E0",
                    "AppBar": "#202020",
                    "Background": "#2E3032",
                    "CardsDialogs": "#FFFFFF",
                    "FlatButtonDown": "#CCCCCC",
                },
            }


            class Tab(EZEFloatLayout, EZETabsBase):
                '''Class implementing content for a tab.'''

                icon = ObjectProperty()


            class Example(EZEApp):
                icons = list(eze_icons.keys())[15:30]

                def build(self):
                    self.theme_cls.colors = colors
                    self.theme_cls.primary_palette = "Teal"
                    self.theme_cls.accent_palette = "Red"

                    return (
                        EZEBoxLayout(
                            EZETopAppBar(title="Custom theme"),
                            EZETabs(id="tabs"),
                            orientation="vertical",
                        )
                    )

                def on_start(self):
                    for name_tab in self.icons:
                        self.root.ids.tabs.add_widget(
                            Tab(
                                EZEIconButton(
                                    icon=name_tab,
                                    icon_size="48sp",
                                    theme_icon_color="Custom",
                                    icon_color="white",
                                    pos_hint={"center_x": .5, "center_y": .5},
                                ),
                                title="This is " + name_tab,
                                icon=name_tab,
                            )
                        )


            Example().run()


This will change the theme colors to your custom definition. In all other
respects, the theming stays as documented.

.. warning:: Please note that the key ``'Red'`` is a required key for the
    dictionary :attr:`eze.color_definition.colors`.
"""

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.metrics import dp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    DictProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.utils import get_color_from_hex

from eze.color_definitions import colors, hue, palette
from eze.font_definitions import theme_font_styles
from eze.material_resources import DEVICE_IOS, DEVICE_TYPE


class ThemeManager(EventDispatcher):
    primary_palette = OptionProperty("Blue", options=palette)
    """
    The name of the color scheme that the application will use.
    All major `material` components will have the color
    of the specified color theme.

    Available options are: `'Red'`, `'Pink'`, `'Purple'`, `'DeepPurple'`,
    `'Indigo'`, `'Blue'`, `'LightBlue'`, `'Cyan'`, `'Teal'`, `'Green'`,
    `'LightGreen'`, `'Lime'`, `'Yellow'`, `'Amber'`, `'Orange'`, `'DeepOrange'`,
    `'Brown'`, `'Gray'`, `'BlueGray'`.

    To change the color scheme of an application:

    .. tabs::

        .. tab:: Imperative python style with KV

            .. code-block:: python

                from kivy.lang import Builder

                from eze.app import EZEApp

                KV = '''
                EZEScreen:

                    EZERectangleFlatButton:
                        text: "Hello World!"
                        pos_hint: {"center_x": .5, "center_y": .5}
                '''


                class Example(EZEApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Red"  # "Purple", "Red"

                        return Builder.load_string(KV)


                Example().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from eze.app import EZEApp
                from eze.uix.button import EZERectangleFlatButton
                from eze.uix.screen import EZEScreen


                class Example(EZEApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Orange"  # "Purple", "Red"

                        return (
                            EZEScreen(
                                EZERectangleFlatButton(
                                    text="Hello, World",
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                )
                            )
                        )


                Example().run()


    :attr:`primary_palette` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Blue'`.
    """

    primary_hue = OptionProperty("500", options=hue)
    """
    The color hue of the application.

    Available options are: `'50'`, `'100'`, `'200'`, `'300'`, `'400'`, `'500'`,
    `'600'`, `'700'`, `'800'`, `'900'`, `'A100'`, `'A200'`, `'A400'`, `'A700'`.

    To change the hue color scheme of an application:

    .. tabs::

        .. tab:: Imperative python style with KV

            .. code-block:: python

                from eze.app import EZEApp
                from eze.uix.screen import EZEScreen
                from eze.uix.button import EZERectangleFlatButton


                class MainApp(EZEApp):
                    def build(self):
                        self.theme_cls.primary_palette = "Orange"
                        self.theme_cls.primary_hue = "200"  # "500"
                        screen = EZEScreen()
                        screen.add_widget(
                            EZERectangleFlatButton(
                                text="Hello World!",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            )
                        )
                        return screen


                MainApp().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from eze.app import EZEApp
                from eze.uix.button import EZERectangleFlatButton
                from eze.uix.screen import EZEScreen


                class Example(EZEApp):
                    def build(self):
                        self.theme_cls.primary_palette = "Orange"
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_hue = "200"  # "500"

                        return (
                            EZEScreen(
                                EZERectangleFlatButton(
                                    text="Hello World!",
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                )
                            )
                        )


                Example().run()

    With a value of ``self.theme_cls.primary_hue = "200"`` and ``self.theme_cls.primary_hue = "500"``:
    

    :attr:`primary_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'500'`.
    """

    primary_light_hue = OptionProperty("200", options=hue)
    """
    Hue value for :attr:`primary_light`.

    :attr:`primary_light_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'200'`.
    """

    primary_dark_hue = OptionProperty("700", options=hue)
    """
    Hue value for :attr:`primary_dark`.

    :attr:`primary_light_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'700'`.
    """

    def _get_primary_color(self) -> list:
        return get_color_from_hex(
            self.colors[self.primary_palette][self.primary_hue]
        )

    primary_color = AliasProperty(
        _get_primary_color, bind=("primary_palette", "primary_hue")
    )
    """
    The color of the current application theme.

    :attr:`primary_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value of the current application theme, property is readonly.
    """

    def _get_primary_light(self) -> list:
        return get_color_from_hex(
            self.colors[self.primary_palette][self.primary_light_hue]
        )

    primary_light = AliasProperty(
        _get_primary_light, bind=("primary_palette", "primary_light_hue")
    )
    """
    Colors of the current application color theme (in lighter color).

    .. tabs::

        .. tab:: Declarative style with KV

            .. code-block:: python

                from kivy.lang import Builder

                from eze.app import EZEApp


                KV = '''
                EZEScreen:

                    EZERaisedButton:
                        text: "primary_light"
                        pos_hint: {"center_x": 0.5, "center_y": 0.7}
                        eze_bg_color: app.theme_cls.primary_light

                    EZERaisedButton:
                        text: "primary_color"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    EZERaisedButton:
                        text: "primary_dark"
                        pos_hint: {"center_x": 0.5, "center_y": 0.3}
                        eze_bg_color: app.theme_cls.primary_dark
                '''


                class MainApp(EZEApp):
                    def build(self):
                        self.theme_cls.primary_palette = "Orange"
                        self.theme_cls.theme_style = "Dark"
                        return Builder.load_string(KV)


                MainApp().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from eze.app import EZEApp
                from eze.uix.button import EZERaisedButton
                from eze.uix.screen import EZEScreen


                class Example(EZEApp):
                    def build(self):
                        self.theme_cls.primary_palette = "Orange"
                        self.theme_cls.theme_style = "Dark"

                        return (
                            EZEScreen(
                                EZERaisedButton(
                                    text="Primary light",
                                    pos_hint={"center_x": 0.5, "center_y": 0.7},
                                    eze_bg_color=self.theme_cls.primary_light,
                                ),
                                EZERaisedButton(
                                    text="Primary color",
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                ),
                                EZERaisedButton(
                                    text="Primary dark",
                                    pos_hint={"center_x": 0.5, "center_y": 0.3},
                                    eze_bg_color=self.theme_cls.primary_dark,
                                ),
                            )
                        )


                Example().run()

    :attr:`primary_light` is an :class:`~kivy.properties.AliasProperty` that
    returns the value of the current application theme (in lighter color),
    property is readonly.
    """

    def _get_primary_dark(self) -> list:
        return get_color_from_hex(
            self.colors[self.primary_palette][self.primary_dark_hue]
        )

    primary_dark = AliasProperty(
        _get_primary_dark, bind=("primary_palette", "primary_dark_hue")
    )
    """
    Colors of the current application color theme (in darker color).

    :attr:`primary_dark` is an :class:`~kivy.properties.AliasProperty` that
    returns the value of the current application theme (in darker color),
    property is readonly.
    """

    accent_palette = OptionProperty("Amber", options=palette)
    """
    The application color palette used for items such as the tab indicator
    in the :class:`~eze.uix.tab.EZETabsBar` class and so on.
    See :attr:`eze.uix.tab.EZETabsBar.indicator_color` attribute.

    :attr:`accent_palette` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Amber'`.
    """

    accent_hue = OptionProperty("500", options=hue)
    """
    Similar to :attr:`primary_hue`, but returns a value for :attr:`accent_palette`.

    :attr:`accent_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'500'`.
    """

    accent_light_hue = OptionProperty("200", options=hue)
    """
    Hue value for :attr:`accent_light`.

    :attr:`accent_light_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'200'`.
    """

    accent_dark_hue = OptionProperty("700", options=hue)
    """
    Hue value for :attr:`accent_dark`.

    :attr:`accent_dark_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'700'`.
    """

    def _get_accent_color(self) -> list:
        return get_color_from_hex(
            self.colors[self.accent_palette][self.accent_hue]
        )

    accent_color = AliasProperty(
        _get_accent_color, bind=["accent_palette", "accent_hue"]
    )
    """
    Similar to :attr:`primary_color`, but returns a value for :attr:`accent_color`.

    :attr:`accent_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`accent_color`, property is
    readonly.
    """

    def _get_accent_light(self) -> list:
        return get_color_from_hex(
            self.colors[self.accent_palette][self.accent_light_hue]
        )

    accent_light = AliasProperty(
        _get_accent_light, bind=["accent_palette", "accent_light_hue"]
    )
    """
    Similar to :attr:`primary_light`, but returns a value for :attr:`accent_light`.

    :attr:`accent_light` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`accent_light`, property is
    readonly.
    """

    def _get_accent_dark(self) -> list:
        return get_color_from_hex(
            self.colors[self.accent_palette][self.accent_dark_hue]
        )

    accent_dark = AliasProperty(
        _get_accent_dark, bind=["accent_palette", "accent_dark_hue"]
    )
    """
    Similar to :attr:`primary_dark`, but returns a value for :attr:`accent_dark`.

    :attr:`accent_dark` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`accent_dark`, property is
    readonly.
    """

    material_style = OptionProperty("M3", options=["M2", "M3"])
    """
    Material design style.
    Available options are: 'M2', 'M3'.

    .. versionadded:: 1.0.0

    .. versionchanged:: 1.2.0
        By default now `'M3'`.

    .. seealso::

       `Material Design 2 <https://material.io/>`_ and
       `Material Design 3 <https://m3.material.io>`_


    :attr:`material_style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'M3'`.
    """

    theme_style_switch_animation = BooleanProperty(False)
    """
    Animate app colors when switching app color scheme ('Dark/light').

    .. versionadded:: 1.1.0

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: python

                from kivy.lang import Builder

                from eze.app import EZEApp

                KV = '''
                EZEScreen:

                    EZECard:
                        orientation: "vertical"
                        padding: 0, 0, 0 , "36dp"
                        size_hint: .5, .5
                        pos_hint: {"center_x": .5, "center_y": .5}
                        elevation: 2
                        shadow_offset: 0, -2

                        EZELabel:
                            text: "Theme style - {}".format(app.theme_cls.theme_style)
                            halign: "center"
                            valign: "center"
                            bold: True
                            font_style: "H5"

                        EZERaisedButton:
                            text: "Set theme"
                            on_release: app.switch_theme_style()
                            pos_hint: {"center_x": .5}
                '''


                class Example(EZEApp):
                    def build(self):
                        self.theme_cls.theme_style_switch_animation = True
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Orange"
                        return Builder.load_string(KV)

                    def switch_theme_style(self):
                        self.theme_cls.primary_palette = (
                            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
                        )
                        self.theme_cls.theme_style = (
                            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
                        )


                Example().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from eze.app import EZEApp
                from eze.uix.button import EZERaisedButton
                from eze.uix.card import EZECard
                from eze.uix.label import EZELabel
                from eze.uix.screen import EZEScreen


                class Example(EZEApp):
                    def build(self):
                        self.theme_cls.theme_style_switch_animation = True
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Orange"
                        return (
                            EZEScreen(
                                EZECard(
                                    EZELabel(
                                        id="label",
                                        text="Theme style - {}".format(self.theme_cls.theme_style),
                                        halign="center",
                                        valign="center",
                                        bold=True,
                                        font_style="H5",
                                    ),
                                    EZERaisedButton(
                                        text="Set theme",
                                        on_release=self.switch_theme_style,
                                        pos_hint={"center_x": 0.5},
                                    ),
                                    id="card",
                                    orientation="vertical",
                                    padding=(0, 0, 0, "36dp"),
                                    size_hint=(0.5, 0.5),
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    elevation=2,
                                    shadow_offset=(0, -2),
                                )
                            )
                        )

                    def switch_theme_style(self, *args):
                        self.theme_cls.primary_palette = (
                            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
                        )
                        self.theme_cls.theme_style = (
                            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
                        )
                        self.root.ids.card.ids.label.text = (
                            "Theme style - {}".format(self.theme_cls.theme_style)
                        )


                Example().run()


    :attr:`theme_style_switch_animation` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    theme_style_switch_animation_duration = NumericProperty(0.2)
    """
    Duration of the animation of switching the color scheme of the application
    ("Dark/light").

    .. versionadded:: 1.1.0

    .. code-block:: python

        class Example(EZEApp):
            def build(self):
                self.theme_cls.theme_style_switch_animation = True
                self.theme_cls.theme_style_switch_animation_duration = 0.8


    :attr:`theme_style_switch_animation_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    theme_style = OptionProperty("Light", options=["Light", "Dark"])
    """
    App theme style.

    .. tabs::

        .. tab:: Imperative python style

            .. code-block:: python

                from eze.app import EZEApp
                from eze.uix.screen import EZEScreen
                from eze.uix.button import EZERectangleFlatButton


                class MainApp(EZEApp):
                    def build(self):
                        self.theme_cls.primary_palette = "Orange"
                        self.theme_cls.theme_style = "Dark"  # "Light"
                        screen = EZEScreen()
                        screen.add_widget(
                            EZERectangleFlatButton(
                                text="Hello World!",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            )
                        )
                        return screen


                MainApp().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from eze.app import EZEApp
                from eze.uix.button import EZERectangleFlatButton
                from eze.uix.screen import EZEScreen


                class Example(EZEApp):
                    def build(self):
                        self.theme_cls.primary_palette = "Orange"
                        self.theme_cls.theme_style = "Dark"  # "Light"

                        return (
                            EZEScreen(
                                EZERectangleFlatButton(
                                    text="Hello World!",
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                ),
                            )
                        )


                Example().run()


    :attr:`theme_style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Light'`.
    """

    def _get_theme_style(self, opposite: bool) -> str:
        if opposite:
            return "Light" if self.theme_style == "Dark" else "Dark"
        else:
            return self.theme_style

    def _get_bg_darkest(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(self.colors["Light"]["StatusBar"])
        elif theme_style == "Dark":
            return get_color_from_hex(self.colors["Dark"]["StatusBar"])

    bg_darkest = AliasProperty(_get_bg_darkest, bind=["theme_style"])
    """
    Similar to :attr:`bg_dark`,
    but the color values are a tone lower (darker) than :attr:`bg_dark`.

    .. tabs::

        .. tab:: Declarative style with KV

            .. code-block:: python

                from kivy.lang import Builder

                from eze.app import EZEApp

                KV = '''
                EZEBoxLayout:

                    EZEWidget:
                        eze_bg_color: app.theme_cls.bg_light

                    EZEBoxLayout:
                        eze_bg_color: app.theme_cls.bg_normal

                    EZEBoxLayout:
                        eze_bg_color: app.theme_cls.bg_dark

                    EZEBoxLayout:
                        eze_bg_color: app.theme_cls.bg_darkest
                '''


                class MainApp(EZEApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"  # "Light"
                        return Builder.load_string(KV)


                MainApp().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from eze.app import EZEApp
                from eze.uix.boxlayout import EZEBoxLayout
                from eze.uix.widget import EZEWidget


                class Example(EZEApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"  # "Light"

                        return (
                            EZEBoxLayout(
                                EZEWidget(
                                    eze_bg_color=self.theme_cls.bg_light,
                                ),
                                EZEWidget(
                                    eze_bg_color=self.theme_cls.bg_normal,
                                ),
                                EZEWidget(
                                    eze_bg_color=self.theme_cls.bg_dark,
                                ),
                                EZEWidget(
                                    eze_bg_color=self.theme_cls.bg_darkest,
                                ),
                            )
                        )


                Example().run()

    :attr:`bg_darkest` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`bg_darkest`,
    property is readonly.
    """

    def _get_op_bg_darkest(self) -> list:
        return self._get_bg_darkest(True)

    opposite_bg_darkest = AliasProperty(
        _get_op_bg_darkest, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`bg_darkest`.

    :attr:`opposite_bg_darkest` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_bg_darkest`,
    property is readonly.
    """

    def _get_bg_dark(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(self.colors["Light"]["AppBar"])
        elif theme_style == "Dark":
            return get_color_from_hex(self.colors["Dark"]["AppBar"])

    bg_dark = AliasProperty(_get_bg_dark, bind=["theme_style"])
    """
    Similar to :attr:`bg_normal`,
    but the color values are one tone lower (darker) than :attr:`bg_normal`.

    :attr:`bg_dark` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`bg_dark`,
    property is readonly.
    """

    def _get_op_bg_dark(self) -> list:
        return self._get_bg_dark(True)

    opposite_bg_dark = AliasProperty(_get_op_bg_dark, bind=["theme_style"])
    """
    The opposite value of color in the :attr:`bg_dark`.

    :attr:`opposite_bg_dark` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`opposite_bg_dark`,
    property is readonly.
    """

    def _get_bg_normal(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(self.colors["Light"]["Background"])
        elif theme_style == "Dark":
            return get_color_from_hex(self.colors["Dark"]["Background"])

    bg_normal = AliasProperty(_get_bg_normal, bind=["theme_style"])
    """
    Similar to :attr:`bg_light`,
    but the color values are one tone lower (darker) than :attr:`bg_light`.

    :attr:`bg_normal` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`bg_normal`,
    property is readonly.
    """

    def _get_op_bg_normal(self) -> list:
        return self._get_bg_normal(True)

    opposite_bg_normal = AliasProperty(_get_op_bg_normal, bind=["theme_style"])
    """
    The opposite value of color in the :attr:`bg_normal`.

    :attr:`opposite_bg_normal` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_bg_normal`,
    property is readonly.
    """

    def _get_bg_light(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(self.colors["Light"]["CardsDialogs"])
        elif theme_style == "Dark":
            return get_color_from_hex(self.colors["Dark"]["CardsDialogs"])

    bg_light = AliasProperty(_get_bg_light, bind=["theme_style"])
    """"
    Depending on the style of the theme (`'Dark'` or `'Light`')
    that the application uses, :attr:`bg_light` contains the color value
    in ``rgba`` format for the widgets background.

    :attr:`bg_light` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`bg_light`,
    property is readonly.
    """

    def _get_op_bg_light(self) -> list:
        return self._get_bg_light(True)

    opposite_bg_light = AliasProperty(_get_op_bg_light, bind=["theme_style"])
    """
    The opposite value of color in the :attr:`bg_light`.

    :attr:`opposite_bg_light` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_bg_light`,
    property is readonly.
    """

    def _get_divider_color(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
        color[3] = 0.12
        return color

    divider_color = AliasProperty(_get_divider_color, bind=["theme_style"])
    """
    Color for dividing lines such as  :class:`~eze.uix.card.EZESeparator`.

    :attr:`divider_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`divider_color`,
    property is readonly.
    """

    def _get_op_divider_color(self) -> list:
        return self._get_divider_color(True)

    opposite_divider_color = AliasProperty(
        _get_op_divider_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`divider_color`.

    :attr:`opposite_divider_color` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_divider_color`,
    property is readonly.
    """

    def _get_disabled_primary_color(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        lum = sum(self.primary_color[0:3]) / 3.0
        if theme_style == "Light":
            a = 0.38
        elif theme_style == "Dark":
            a = 0.50
        return [lum, lum, lum, a]

    disabled_primary_color = AliasProperty(
        _get_disabled_primary_color, bind=["theme_style"]
    )
    """
    The greyscale disabled version of the current application theme color
    in ``rgba`` format.

    .. versionadded:: 1.0.0

    :attr:`disabled_primary_color`
    is an :class:`~kivy.properties.AliasProperty` that returns the value
    in ``rgba`` format for :attr:`disabled_primary_color`,
    property is readonly.
    """

    def _get_op_disabled_primary_color(self) -> list:
        return self._get_disabled_primary_color(True)

    opposite_disabled_primary_color = AliasProperty(
        _get_op_disabled_primary_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`disabled_primary_color`.

    .. versionadded:: 1.0.0

    :attr:`opposite_disabled_primary_color` is an
    :class:`~kivy.properties.AliasProperty` that returns the value
    in ``rgba`` format for :attr:`opposite_disabled_primary_color`,
    property is readonly.
    """

    def _get_text_color(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.87
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
        return color

    text_color = AliasProperty(_get_text_color, bind=["theme_style"])
    """
    Color of the text used in the :class:`~eze.uix.label.EZELabel`.

    :attr:`text_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`text_color`,
    property is readonly.
    """

    def _get_op_text_color(self) -> list:
        return self._get_text_color(True)

    opposite_text_color = AliasProperty(
        _get_op_text_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`text_color`.

    :attr:`opposite_text_color` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_text_color`,
    property is readonly.
    """

    def _get_secondary_text_color(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.54
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
            color[3] = 0.70
        return color

    secondary_text_color = AliasProperty(
        _get_secondary_text_color, bind=["theme_style"]
    )
    """
    The color for the secondary text that is used in classes
    from the module :class:`~eze/uix/list.TwoLineListItem`.

    :attr:`secondary_text_color` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`secondary_text_color`,
    property is readonly.
    """

    def _get_op_secondary_text_color(self) -> list:
        return self._get_secondary_text_color(True)

    opposite_secondary_text_color = AliasProperty(
        _get_op_secondary_text_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`secondary_text_color`.

    :attr:`opposite_secondary_text_color`
    is an :class:`~kivy.properties.AliasProperty` that returns the value
    in ``rgba`` format for :attr:`opposite_secondary_text_color`,
    property is readonly.
    """

    def _get_icon_color(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.54
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
        return color

    icon_color = AliasProperty(_get_icon_color, bind=["theme_style"])
    """
    Color of the icon used in the :class:`~eze.uix.button.EZEIconButton`.

    :attr:`icon_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`icon_color`,
    property is readonly.
    """

    def _get_op_icon_color(self) -> list:
        return self._get_icon_color(True)

    opposite_icon_color = AliasProperty(
        _get_op_icon_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`icon_color`.

    :attr:`opposite_icon_color` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_icon_color`,
    property is readonly.
    """

    def _get_disabled_hint_text_color(self, opposite: bool = False) -> list:
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.38
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
            color[3] = 0.50
        return color

    disabled_hint_text_color = AliasProperty(
        _get_disabled_hint_text_color, bind=["theme_style"]
    )
    """
    Color of the disabled text used in the :class:`~eze.uix.textfield.EZETextField`.

    :attr:`disabled_hint_text_color`
    is an :class:`~kivy.properties.AliasProperty` that returns the value
    in ``rgba`` format for :attr:`disabled_hint_text_color`,
    property is readonly.
    """

    def _get_op_disabled_hint_text_color(self) -> list:
        return self._get_disabled_hint_text_color(True)

    opposite_disabled_hint_text_color = AliasProperty(
        _get_op_disabled_hint_text_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`disabled_hint_text_color`.

    :attr:`opposite_disabled_hint_text_color`
    is an :class:`~kivy.properties.AliasProperty` that returns the value
    in ``rgba`` format for :attr:`opposite_disabled_hint_text_color`,
    property is readonly.
    """

    # Hardcoded because muh standard
    def _get_error_color(self) -> list:
        return get_color_from_hex(self.colors["Red"]["A700"])

    error_color = AliasProperty(_get_error_color, bind=["theme_style"])
    """
    Color of the error text used
    in the :class:`~eze.uix.textfield.EZETextField`.

    :attr:`error_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`error_color`,
    property is readonly.
    """

    def _get_ripple_color(self) -> list:
        return self._ripple_color

    def _set_ripple_color(self, value) -> None:
        self._ripple_color = value

    _ripple_color = ColorProperty(colors["Gray"]["400"])
    """Private value."""

    ripple_color = AliasProperty(
        _get_ripple_color, _set_ripple_color, bind=["_ripple_color"]
    )
    """
    Color of ripple effects.

    :attr:`ripple_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`ripple_color`,
    property is readonly.
    """

    def _determine_device_orientation(self, _, window_size) -> None:
        if window_size[0] > window_size[1]:
            self.device_orientation = "landscape"
        elif window_size[1] >= window_size[0]:
            self.device_orientation = "portrait"

    device_orientation = StringProperty("")
    """
    Device orientation.

    :attr:`device_orientation` is an :class:`~kivy.properties.StringProperty`.
    """

    def _get_standard_increment(self) -> float:
        if DEVICE_TYPE == "mobile":
            if self.device_orientation == "landscape":
                return dp(48)
            else:
                return dp(56)
        else:
            return dp(60)

    standard_increment = AliasProperty(
        _get_standard_increment, bind=["device_orientation"]
    )
    """
    Value of standard increment.

    :attr:`standard_increment` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`standard_increment`,
    property is readonly.
    """

    def _get_horizontal_margins(self) -> float:
        if DEVICE_TYPE == "mobile":
            return dp(16)
        else:
            return dp(24)

    horizontal_margins = AliasProperty(_get_horizontal_margins)
    """
    Value of horizontal margins.

    :attr:`horizontal_margins` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`horizontal_margins`,
    property is readonly.
    """

    def on_theme_style(self, interval: int, theme_style: str) -> None:
        if (
            hasattr(App.get_running_app(), "theme_cls")
            and App.get_running_app().theme_cls == self
        ):
            self.set_clearcolor_by_theme_style(theme_style)

    _set_clearcolor = False

    def set_clearcolor_by_theme_style(self, theme_style):
        if self.theme_style_switch_animation and self._set_clearcolor:
            Animation(
                clearcolor=get_color_from_hex(
                    self.colors[theme_style]["Background"]
                ),
                d=self.theme_style_switch_animation_duration,
                t="linear",
            ).start(Window)
        else:
            Window.clearcolor = get_color_from_hex(
                self.colors[theme_style]["Background"]
            )
            self._set_clearcolor = True

    # Font name, size (sp), always caps, letter spacing (sp).
    font_styles = DictProperty(
        {
            "H1": ["RobotoLight", 96, False, -1.5],
            "H2": ["RobotoLight", 60, False, -0.5],
            "H3": ["Roboto", 48, False, 0],
            "H4": ["Roboto", 34, False, 0.25],
            "H5": ["Roboto", 24, False, 0],
            "H6": ["RobotoMedium", 20, False, 0.15],
            "Subtitle1": ["Roboto", 16, False, 0.15],
            "Subtitle2": ["RobotoMedium", 14, False, 0.1],
            "Body1": ["Roboto", 16, False, 0.5],
            "Body2": ["Roboto", 14, False, 0.25],
            "Button": ["RobotoMedium", 14, True, 1.25],
            "Caption": ["RubikWetPaint-Regular", 12, False, 0.4],
            "Overline": ["Roboto", 10, True, 1.5],
            "Icon": ["Icons", 24, False, 0],
        }
    )
    """
    Data of default font styles.

    Add custom font
    ---------------

    .. tabs::

        .. tab:: Declarative style with KV

            .. code-block:: python

                from kivy.core.text import LabelBase
                from kivy.lang import Builder

                from eze.app import EZEApp
                from eze.font_definitions import theme_font_styles

                KV = '''
                EZEScreen:

                    EZELabel:
                        text: "JetBrainsMono"
                        halign: "center"
                        font_style: "JetBrainsMono"
                '''


                class MainApp(EZEApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"

                        LabelBase.register(
                            name="JetBrainsMono",
                            fn_regular="JetBrainsMono-Regular.ttf")

                        theme_font_styles.append('JetBrainsMono')
                        self.theme_cls.font_styles["JetBrainsMono"] = [
                            "JetBrainsMono",
                            16,
                            False,
                            0.15,
                        ]
                        return Builder.load_string(KV)


                MainApp().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from kivy.core.text import LabelBase

                from eze.app import EZEApp
                from eze.uix.screen import EZEScreen
                from eze.uix.label import EZELabel
                from eze.font_definitions import theme_font_styles


                class MainApp(EZEApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"

                        LabelBase.register(
                            name="JetBrainsMono",
                            fn_regular="JetBrainsMono-Regular.ttf")

                        theme_font_styles.append('JetBrainsMono')
                        self.theme_cls.font_styles["JetBrainsMono"] = [
                            "JetBrainsMono",
                            16,
                            False,
                            0.15,
                        ]
                        return (
                            EZEScreen(
                                EZELabel(
                                    text="JetBrainsMono",
                                    halign="center",
                                    font_style="JetBrainsMono",
                                )
                            )
                        )


                MainApp().run()


    :attr:`font_styles` is an :class:`~kivy.properties.DictProperty`.
    """

    def set_colors(
        self,
        primary_palette: str,
        primary_hue: str,
        primary_light_hue: str,
        primary_dark_hue: str,
        accent_palette: str,
        accent_hue: str,
        accent_light_hue: str,
        accent_dark_hue: str,
    ) -> None:
        """
        Courtesy method to allow all of the theme color attributes to be set in one call.

        :attr:`set_colors` allows all of the following to be set in one method call:

        * primary palette color,
        * primary hue,
        * primary light hue,
        * primary dark hue,
        * accent palette color,
        * accent hue,
        * accent ligth hue, and
        * accent dark hue.

        Note that all values *must* be provided. If you only want to set one or two values
        use the appropriate method call for that.

        .. tabs::

            .. tab:: Imperative python style

                .. code-block:: python

                    from eze.app import EZEApp
                    from eze.uix.screen import EZEScreen
                    from eze.uix.button import EZERectangleFlatButton

                    class MainApp(EZEApp):
                        def build(self):
                            self.theme_cls.set_colors(
                                "Blue", "600", "50", "800", "Teal", "600", "100", "800"
                            )
                            screen = EZEScreen()
                            screen.add_widget(
                                EZERectangleFlatButton(
                                    text="Hello World!",
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                )
                            )
                            return screen


                    MainApp().run()

            .. tab:: Declarative python style

                .. code-block:: python

                    from eze.app import EZEApp
                    from eze.uix.screen import EZEScreen
                    from eze.uix.button import EZERectangleFlatButton

                    class MainApp(EZEApp):
                        def build(self):
                            self.theme_cls.set_colors(
                                "Blue", "600", "50", "800", "Teal", "600", "100", "800"
                            )
                            return (
                                EZEScreen(
                                    EZERectangleFlatButton(
                                        text="Hello World!",
                                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    )
                                )
                            )


                    MainApp().run()
        """

        self.primary_palette = primary_palette
        self.primary_hue = primary_hue
        self.primary_light_hue = primary_light_hue
        self.primary_dark_hue = primary_dark_hue
        self.accent_palette = accent_palette
        self.accent_hue = accent_hue
        self.accent_light_hue = accent_light_hue
        self.accent_dark_hue = accent_dark_hue

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda x: self.on_theme_style(0, self.theme_style))
        self._determine_device_orientation(None, Window.size)
        Window.bind(size=self._determine_device_orientation)
        self.bind(font_styles=self.sync_theme_styles)
        self.colors = colors
        Clock.schedule_once(self.sync_theme_styles)

    def sync_theme_styles(self, *args) -> None:
        # Syncs the values from self.font_styles to theme_font_styles
        # this will ensure continuity when someone registers a new font_style.
        for num, style in enumerate(theme_font_styles):
            if style not in self.font_styles:
                theme_font_styles.pop(num)
        for style in self.font_styles.keys():
            theme_font_styles.append(style)


class ThemableBehavior(EventDispatcher):
    theme_cls = ObjectProperty()
    """
    Instance of :class:`~ThemeManager` class.

    :attr:`theme_cls` is an :class:`~kivy.properties.ObjectProperty`.
    """

    device_ios = BooleanProperty(DEVICE_IOS)
    """
    ``True`` if device is ``iOS``.

    :attr:`device_ios` is an :class:`~kivy.properties.BooleanProperty`.
    """

    widget_style = OptionProperty(
        "android", options=["android", "ios", "desktop"]
    )
    """
    Allows to set one of the three style properties for the widget:
    `'android'`, `'ios'`, `'desktop'`.

    For example, for the class :class:`~eze.uix.selectioncontrol.EZESwitch`
    has two styles - `'android'` and `'ios'`:

    .. code-block:: kv

        EZESwitch:
            widget_style: "ios"

    .. code-block:: kv

        EZESwitch:
            widget_style: "android"

    :attr:`widget_style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'android'`.
    """

    opposite_colors = BooleanProperty(False)
    """
    For some widgets, for example, for a widget
    :class:`~eze.uix.toolbar.EZETopAppBar` changes the color of the label to
    the color opposite to the main theme.

    .. code-block:: kv

        EZETopAppBar:
            title: "EZETopAppBar"
            opposite_colors: True


    .. code-block:: kv

        EZETopAppBar:
            title: "EZETopAppBar"
            opposite_colors: True

    """

    def __init__(self, **kwargs):
        self.unbind_properties = [
            "theme_style",
            "material_style",
            "device_orientation",
            "primary_color",
            "primary_palette",
            "accent_palette",
            "text_color",
        ]

        if self.theme_cls is not None:
            pass
        else:
            try:
                if not isinstance(
                    App.get_running_app().property("theme_cls", True),
                    ObjectProperty,
                ):
                    raise ValueError(
                        "EZE: App object must be inherited from "
                        "`eze.app.EZEApp`"
                    )
            except AttributeError:
                raise ValueError(
                    "EZE: App object must be initialized before loading "
                    "root widget. See "
                )
            self.theme_cls = App.get_running_app().theme_cls

        super().__init__(**kwargs)

        # Fix circular imports.
        from eze.uix.behaviors import CommonElevationBehavior
        from eze.uix.label import EZELabel
        from eze.uix.textfield import EZETextField

        self.common_elevation_behavior = CommonElevationBehavior
        self.eze_label = EZELabel
        self.eze_textfield = EZETextField

    def remove_widget(self, widget) -> None:
        if not hasattr(widget, "theme_cls"):
            super().remove_widget(widget)
            return

        callbacks = widget.theme_cls.get_property_observers("theme_style")

        for callback in callbacks:
            try:
                if hasattr(callback, "proxy") and hasattr(
                    callback.proxy, "theme_cls"
                ):
                    if issubclass(widget.__class__, self.eze_textfield):
                        widget.theme_cls.unbind(
                            **{
                                "theme_style": getattr(
                                    callback.proxy, callback.method_name
                                )
                            }
                        )
                    for property_name in self.unbind_properties:
                        if widget == callback.proxy:
                            widget.theme_cls.unbind(
                                **{
                                    property_name: getattr(
                                        callback.proxy, callback.method_name
                                    )
                                }
                            )
                            # EZE widgets may contain other EZE widgets.
                            for children in widget.children:
                                if hasattr(children, "theme_cls"):
                                    self.remove_widget(children)
            except ReferenceError:
                pass

        # Canceling a scheduled method call on_window_touch for EZELabel
        # objects.
        if (
            issubclass(widget.__class__, self.eze_label)
            and self.eze_label.allow_selection
        ):
            Window.unbind(on_touch_down=widget.on_window_touch)

        super().remove_widget(widget)
