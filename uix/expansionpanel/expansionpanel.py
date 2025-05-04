"""
Components/ExpansionPanel
=========================

.. seealso::

    `Material Design spec, Expansion panel <https://material.io/archive/guidelines/components/expansion-panels.html#>`_

.. rubric:: Expansion panels contain creation flows and allow lightweight editing of an element.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/expansion-panel.png
    :align: center

Usage
-----

.. code-block:: python

    self.add_widget(
        EZEExpansionPanel(
            icon="logo.png",  # panel icon
            content=Content(),  # panel content
            panel_cls=EZEExpansionPanelOneLine(text="Secondary text"),  # panel class
        )
    )

To use :class:`~EZEExpansionPanel` you must pass one of the following classes
to the :attr:`~EZEExpansionPanel.panel_cls` parameter:

- :class:`~EZEExpansionPanelOneLine`
- :class:`~EZEExpansionPanelTwoLine`
- :class:`~EZEsExpansionPanelThreeLine`

These classes are inherited from the following classes:

- :class:`~eze.uix.list.OneLineAvatarIconListItem`
- :class:`~eze.uix.list.TwoLineAvatarIconListItem`
- :class:`~eze.uix.list.ThreeLineAvatarIconListItem`

.. code-block:: python

    self.root.ids.box.add_widget(
        EZEExpansionPanel(
            icon="logo.png",
            content=Content(),
            panel_cls=EZEExpansionPanelThreeLine(
                text="Text",
                secondary_text="Secondary text",
                tertiary_text="Tertiary text",
            )
        )
    )

Example
-------

.. code-block:: python

    import os

    from kivy.lang import Builder

    from eze.app import EZEApp
    from eze.uix.boxlayout import EZEBoxLayout
    from eze.uix.expansionpanel import EZEExpansionPanel, EZEExpansionPanelThreeLine
    from kivymd import images_path

    KV = '''
    <Content>
        adaptive_height: True

        TwoLineIconListItem:
            text: "(050)-123-45-67"
            secondary_text: "Mobile"

            IconLeftWidget:
                icon: 'phone'


    EZEScrollView:

        EZEGridLayout:
            id: box
            cols: 1
            adaptive_height: True
    '''


    class Content(EZEBoxLayout):
        '''Custom content.'''


    class Test(EZEApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for i in range(10):
                self.root.ids.box.add_widget(
                    EZEExpansionPanel(
                        icon=os.path.join(images_path, "logo", "eze-icon-128.png"),
                        content=Content(),
                        panel_cls=EZEExpansionPanelThreeLine(
                            text="Text",
                            secondary_text="Secondary text",
                            tertiary_text="Tertiary text",
                        )
                    )
                )


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/expansion-panel.gif
    :align: center

Two events are available for :class:`~EZEExpansionPanel`
-------------------------------------------------------

- :attr:`~EZEExpansionPanel.on_open`
- :attr:`~EZEExpansionPanel.on_close`

.. code-block:: kv

        EZEExpansionPanel:
            on_open: app.on_panel_open(args)
            on_close: app.on_panel_close(args)

The user function takes one argument - the object of the panel:

.. code-block:: python

    def on_panel_open(self, instance_panel):
        print(instance_panel)

.. seealso:: `See Expansion panel example <https://github.com/kivymd/KivyMD/wiki/Components-Expansion-Panel>`_

    `Expansion panel and MDCard <https://github.com/kivymd/KivyMD/wiki/Components-Expansion-Panel-and-MDCard>`_
"""

__all__ = (
    "EZEExpansionPanel",
    "EZEExpansionPanelOneLine",
    "EZEExpansionPanelTwoLine",
    "EZEExpansionPanelThreeLine",
    "EZEExpansionPanelLabel",
)

import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import WidgetException

import eze.material_resources as m_res
from eze import uix_path
from eze.icon_definitions import eze_icons
from eze.uix.button import EZEIconButton
from eze.uix.list import (
    IconLeftWidget,
    ImageLeftWidget,
    IRightBodyTouch,
    OneLineAvatarIconListItem,
    ThreeLineAvatarIconListItem,
    TwoLineAvatarIconListItem,
    TwoLineListItem,
)

with open(
    os.path.join(uix_path, "expansionpanel", "expansionpanel.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class EZExpansionChevronRight(IRightBodyTouch, EZEIconButton):
    """Chevron icon on the right panel."""

    _angle = NumericProperty(0)


class EZEExpansionPanelOneLine(OneLineAvatarIconListItem):
    """
    Single line panel.

    For more information, see in the
    :class:`~eze.uix.list.OneLineAvatarIconListItem` class documentation.
    """


class EZEExpansionPanelTwoLine(TwoLineAvatarIconListItem):
    """
    Two-line panel.

    For more information, see in the
    :class:`~eze.uix.list.TwoLineAvatarIconListItem` class documentation.
    """


class EZEExpansionPanelThreeLine(ThreeLineAvatarIconListItem):
    """
    Three-line panel.

    For more information, see in the
    :class:`~eze.uix.list.ThreeLineAvatarIconListItem` class documentation.
    """


class EZEExpansionPanelLabel(TwoLineListItem):
    """
    Label panel.

    For more information, see in the
    :class:`~eze.uix.list.TwoLineListItem` class documentation.

    ..warning:: This class is created for use in the
        :class:`~eze.uix.stepper.EZEStepperVertical` and
        :class:`~eze.uix.stepper.EZEStepper` classes, and has not
        been tested for use outside of these classes.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_paddings)

    def set_paddings(self, interval: Union[int, float]) -> None:
        self._txt_bot_pad = dp(36)
        self._txt_left_pad = dp(0)


class EZEExpansionPanel(RelativeLayout):
    """
    Expansion panel class.

    For more information, see in the
    :class:`~kivy.uix.relativelayout.RelativeLayout` classes documentation.

    :Events:
        :attr:`on_open`
            Called when a panel is opened.
        :attr:`on_close`
            Called when a panel is closed.
    """

    content = ObjectProperty()
    """
    Content of panel. Must be `Kivy` widget.

    :attr:`content` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    icon = StringProperty()
    """
    Icon of panel.

    Icon Should be either be a path to an image or
    a logo name in :class:`~kivymd.icon_definitions.md_icons`

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

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
    """
    The name of the animation transition type to use when animating to
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

    panel_cls = ObjectProperty()
    """
    Panel object. The object must be one of the classes
    :class:`~EZEExpansionPanelOneLine`, :class:`~EZEExpansionPanelTwoLine` or
    :class:`~EZEExpansionPanelThreeLine`.

    :attr:`panel_cls` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    _state = StringProperty("close")
    _anim_playing = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_close")

        if self.panel_cls and isinstance(
            self.panel_cls,
            (
                EZEExpansionPanelOneLine,
                EZEExpansionPanelTwoLine,
                EZEExpansionPanelThreeLine,
                EZEExpansionPanelLabel,
            ),
        ):
            self.panel_cls.pos_hint = {"top": 1}
            self.panel_cls._no_ripple_effect = True
            self.panel_cls.bind(
                on_release=lambda x: self.check_open_panel(self.panel_cls)
            )
            if not isinstance(self.panel_cls, EZEExpansionPanelLabel):
                self.chevron = EZEExpansionChevronRight()
                self.panel_cls.add_widget(self.chevron)
                if self.icon:
                    if self.icon in eze_icons.keys():
                        self.panel_cls.add_widget(
                            IconLeftWidget(
                                icon=self.icon,
                                pos_hint={"center_y": 0.5},
                            )
                        )
                    else:
                        self.panel_cls.add_widget(
                            ImageLeftWidget(
                                source=self.icon, pos_hint={"center_y": 0.5}
                            )
                        )
                else:
                    self.panel_cls.remove_widget(
                        self.panel_cls.ids._left_container
                    )
                    self.panel_cls._txt_left_pad = 0
            else:
                # if no icon
                self.panel_cls._txt_left_pad = m_res.HORIZ_MARGINS
            self.add_widget(self.panel_cls)
        else:
            raise ValueError(
                "EZE: `panel_cls` object must be must be one of the "
                "objects from the list\n"
                "[EZEExpansionPanelOneLine, EZEExpansionPanelTwoLine, "
                "EZEExpansionPanelThreeLine]"
            )

    def on_open(self, *args):
        """Called when a panel is opened."""

    def on_close(self, *args):
        """Called when a panel is closed."""

    def check_open_panel(
        self,
        instance_panel: [
            EZEExpansionPanelThreeLine,
            EZEExpansionPanelTwoLine,
            EZEExpansionPanelThreeLine,
            EZEExpansionPanelLabel,
        ],
    ) -> None:
        """
        Called when you click on the panel. Called methods to open or close
        a panel.
        """

        press_current_panel = False
        for panel in self.parent.children:
            if isinstance(panel, EZEExpansionPanel):
                if len(panel.children) == 2:
                    if instance_panel is panel.children[1]:
                        press_current_panel = True
                    panel.remove_widget(panel.children[0])
                    if not isinstance(self.panel_cls, EZEExpansionPanelLabel):
                        chevron = panel.children[0].children[0].children[0]
                        self.set_chevron_up(chevron)
                    self.close_panel(panel, press_current_panel)
                    self.dispatch("on_close")
                    break
        if not press_current_panel:
            self.set_chevron_down()

    def set_chevron_down(self) -> None:
        """Sets the chevron down."""
        
        if not isinstance(self.panel_cls, EZEExpansionPanelLabel):
            Animation(_angle=-90, d=self.opening_time).start(self.chevron)
        self.open_panel()
        self.dispatch("on_open")
    def set_chevron_up(self, instance_chevron: EZEExpansionChevronRight) -> None:
        """Sets the chevron up."""

        if not isinstance(self.panel_cls, EZEExpansionPanelLabel):
            Animation(_angle=0, d=self.closing_time).start(instance_chevron)

    def close_panel(
        self, instance_expansion_panel, press_current_panel: bool
    ) -> None:
        """Method closes the panel."""

        if self._anim_playing:
            return

        if press_current_panel:
            self._anim_playing = True

        self._state = "close"

        anim = Animation(
            height=self.panel_cls.height,
            d=self.closing_time,
            t=self.closing_transition,
        )
        anim.bind(on_complete=self._disable_anim)
        anim.start(instance_expansion_panel)

    def open_panel(self, *args) -> None:
        """Method opens a panel."""

        if self._anim_playing:
            return

        self._anim_playing = True
        self._state = "open"

        anim = Animation(
            height=self.content.height + self.height,
            d=self.opening_time,
            t=self.opening_transition,
        )
        anim.bind(on_complete=self._add_content)
        anim.bind(on_complete=self._disable_anim)
        anim.start(self)

    def get_state(self) -> str:
        """Returns the state of panel. Can be `close` or `open` ."""

        return self._state

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(
            widget,
            (
                EZEExpansionPanelOneLine,
                EZEExpansionPanelTwoLine,
                EZEExpansionPanelThreeLine,
                EZEExpansionPanelLabel,
            ),
        ):
            self.height = widget.height
        return super().add_widget(widget)

    def _disable_anim(self, *args):
        self._anim_playing = False

    def _add_content(self, *args):
        if self.content:
            try:
                if isinstance(self.panel_cls, EZEExpansionPanelLabel):
                    self.content.y = dp(36)
                self.add_widget(self.content)
            except WidgetException:
                pass
