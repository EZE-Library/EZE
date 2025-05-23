"""
Components/RefreshLayout
========================

Example
-------

.. code-block:: python

    from kivy.clock import Clock
    from kivy.lang import Builder
    from kivy.factory import Factory
    from kivy.properties import StringProperty

    from eze.app import EZEApp
    from eze.uix.button import EZEIconButton
    from eze.icon_definitions import md_icons
    from eze.uix.list import ILeftBodyTouch, OneLineIconListItem
    from eze.theming import ThemeManager
    from eze.utils import asynckivy

    Builder.load_string('''
    <ItemForList>
        text: root.text

        IconLeftSampleWidget:
            icon: root.icon


    <Example@EZEFloatLayout>

        EZEBoxLayout:
            orientation: 'vertical'

            EZETopAppBar:
                title: app.title
                eze_bg_color: app.theme_cls.primary_color
                background_palette: 'Primary'
                elevation: 4
                left_action_items: [['menu', lambda x: x]]

            EZEScrollViewRefreshLayout:
                id: refresh_layout
                refresh_callback: app.refresh_callback
                root_layout: root
                spinner_color: "brown"
                circle_color: "white"

                EZEGridLayout:
                    id: box
                    adaptive_height: True
                    cols: 1
    ''')


    class IconLeftSampleWidget(ILeftBodyTouch, EZEIconButton):
        pass


    class ItemForList(OneLineIconListItem):
        icon = StringProperty()


    class Example(EZEApp):
        title = 'Example Refresh Layout'
        screen = None
        x = 0
        y = 15

        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            self.screen = Factory.Example()
            self.set_list()

            return self.screen

        def set_list(self):
            async def set_list():
                names_icons_list = list(md_icons.keys())[self.x:self.y]
                for name_icon in names_icons_list:
                    await asynckivy.sleep(0)
                    self.screen.ids.box.add_widget(
                        ItemForList(icon=name_icon, text=name_icon))
            asynckivy.start(set_list())

        def refresh_callback(self, *args):
            '''
            A method that updates the state of your application
            while the spinner remains on the screen.
            '''

            def refresh_callback(interval):
                self.screen.ids.box.clear_widgets()
                if self.x == 0:
                    self.x, self.y = 15, 30
                else:
                    self.x, self.y = 0, 15
                self.set_list()
                self.screen.ids.refresh_layout.refresh_done()
                self.tick = 0

            Clock.schedule_once(refresh_callback, 1)


    Example().run()
"""

__all__ = ("EZEScrollViewRefreshLayout",)

import os
from typing import Union

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.floatlayout import FloatLayout

from eze import uix_path
from eze.theming import ThemableBehavior
from eze.uix.scrollview import EZEScrollView

with open(
    os.path.join(uix_path, "refreshlayout", "refreshlayout.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class _RefreshScrollEffect(DampedScrollEffect):
    """
    This class is simply based on DampedScrollEffect.
    If you need any documentation please look at
    :class:`~kivy.effects.dampedscrolleffect`.
    """

    min_scroll_to_reload = NumericProperty("-100dp")
    """
    Minimum overscroll value to reload.

    :attr:`min_scroll_to_reload` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `'-100dp'`.
    """

    def on_overscroll(
        self, instance_refresh_scroll_effect, overscroll: Union[int, float]
    ) -> bool:
        if overscroll < self.min_scroll_to_reload:
            scroll_view = self.target_widget.parent
            scroll_view._did_overscroll = True
            return True
        else:
            return False


class EZEScrollViewRefreshLayout(ThemableBehavior, EZEScrollView):
    """
    Refresh layout class.

    For more information, see in the
    :class:`~eze.theming.ThemableBehavior` and
    :class:`~eze.uix.scrollview.EZEScrollView`
    class documentation.
    """

    root_layout = ObjectProperty()
    """
    The spinner will be attached to this layout.

    :attr:`root_layout` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    refresh_callback = ObjectProperty()
    """
    The method that will be called at the on_touch_up event,
    provided that the overscroll of the list has been registered.

    :attr:`refresh_callback` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    spinner_color = ColorProperty([1, 1, 1, 1])
    """
    Color of the spinner in (r, g, b, a) or string format.

    .. versionadded:: 1.2.0

    :attr:`spinner_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    circle_color = ColorProperty(None)
    """
    Color of the ellipse around the spinner in (r, g, b, a) or string format.

    .. versionadded:: 1.2.0

    :attr:`circle_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    show_transition = StringProperty("out_elastic")
    """
    Transition of the spinner's opening.

    .. versionadded:: 1.2.0

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_elastic'`.
    """

    show_duration = NumericProperty(0.8)
    """
    Duration of the spinner display.

    .. versionadded:: 1.2.0

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.8`.
    """

    hide_transition = StringProperty("out_elastic")
    """
    Transition of hiding the spinner.

    .. versionadded:: 1.2.0

    :attr:`hide_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_elastic'`.
    """

    hide_duration = NumericProperty(0.8)
    """
    Duration of hiding the spinner.

    .. versionadded:: 1.2.0

    :attr:`hide_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.8`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.circle_color:
            self.circle_color = self.theme_cls.primary_dark
        self.effect_cls = _RefreshScrollEffect
        self._work_spinner = False
        self._did_overscroll = False
        self.refresh_spinner = None

    def on_touch_up(self, *args):
        if self._did_overscroll and not self._work_spinner:
            if self.refresh_callback:
                self.refresh_callback()
            if not self.refresh_spinner:
                self.refresh_spinner = RefreshSpinner(
                    _refresh_layout=self,
                    spinner_color=self.spinner_color,
                    circle_color=self.circle_color,
                    show_transition=self.show_transition,
                    show_duration=self.show_duration,
                    hide_transition=self.hide_transition,
                    hide_duration=self.hide_duration,
                )
                self.root_layout.add_widget(self.refresh_spinner)
            self.refresh_spinner.start_anim_spinner()
            self._work_spinner = True
            self._did_overscroll = False
            return True

        return super().on_touch_up(*args)

    def refresh_done(self) -> None:
        if self.refresh_spinner:
            self.refresh_spinner.hide_anim_spinner()


class RefreshSpinner(ThemableBehavior, FloatLayout):
    # Color of the spinner in (r, g, b, a) or string format.
    spinner_color = ColorProperty([1, 1, 1, 1])
    # Color of the ellipse around the spinner in (r, g, b, a) or string format.
    circle_color = ColorProperty()
    # Transition of the spinner's opening.
    show_transition = StringProperty()
    # The duration of the spinner display.
    show_duration = NumericProperty(0.8)
    # Transition of hiding the spinner.
    hide_transition = StringProperty()
    # Duration of hiding the spinner.
    hide_duration = NumericProperty(0.8)

    # kivymd.refreshlayout.MDScrollViewRefreshLayout object
    _refresh_layout = ObjectProperty()

    def start_anim_spinner(self) -> None:
        spinner = self.ids.body_spinner
        Animation(
            y=spinner.y - self.theme_cls.standard_increment * 2 + dp(10),
            d=self.show_duration,
            t=self.show_transition,
        ).start(spinner)

    def hide_anim_spinner(self) -> None:
        spinner = self.ids.body_spinner
        anim = Animation(
            y=Window.height, d=self.hide_duration, t=self.hide_transition
        )
        anim.bind(on_complete=self.set_spinner)
        anim.start(spinner)

    def set_spinner(self, *args) -> None:
        body_spinner = self.ids.body_spinner
        body_spinner.size = (dp(46), dp(46))
        body_spinner.y = Window.height
        body_spinner.opacity = 1
        spinner = self.ids.spinner
        spinner.size = (dp(30), dp(30))
        spinner.opacity = 1
        self._refresh_layout._work_spinner = False
        self._refresh_layout._did_overscroll = False
