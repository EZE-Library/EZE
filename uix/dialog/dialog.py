"""
Components/Dialog
=================

.. seealso::

    `Material Design spec, Dialogs <https://material.io/components/dialogs>`_


.. rubric:: Dialogs inform users about a task and can contain critical
    information, require decisions, or involve multiple tasks.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialogs.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from eze.app import EZEApp
    from eze.uix.button import EZEFlatButton
    from eze.uix.dialog import EZEDialog

    KV = '''
    EZEFloatLayout:

        EZEFlatButton:
            text: "ALERT DIALOG"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_alert_dialog()
    '''


    class Example(EZEApp):
        dialog = None

        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)

        def show_alert_dialog(self):
            if not self.dialog:
                self.dialog = EZEDialog(
                    text="Discard draft?",
                    buttons=[
                        EZEFlatButton(
                            text="CANCEL",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                        ),
                        EZEFlatButton(
                            text="DISCARD",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                        ),
                    ],
                )
            self.dialog.open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/alert-dialog.png
    :align: center
"""

__all__ = ("EZEDialog", "BaseDialog")

import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.modalview import ModalView

from eze import uix_path
from eze.material_resources import DEVICE_TYPE
from eze.theming import ThemableBehavior
from eze.uix.behaviors import CommonElevationBehavior, MotionDialogBehavior
from eze.uix.button import BaseButton
from eze.uix.card import EZESeparator
from eze.uix.list import BaseListItem

with open(
    os.path.join(uix_path, "dialog", "dialog.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class BaseDialog(
    ThemableBehavior, MotionDialogBehavior, ModalView, CommonElevationBehavior
):
    elevation = NumericProperty(3)
    """
    See :attr:`eze.uix.behaviors.elevation.CommonElevationBehavior.elevation`
    attribute for more information.

    .. versionadded:: 1.1.0

    :attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `3`.
    """

    shadow_softness = NumericProperty(24)
    """
    See :attr:`eze.uix.behaviors.elevation.CommonElevationBehavior.shadow_softness`
    attribute for more information.

    .. versionadded:: 1.1.0

    :attr:`shadow_softness` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `24`.
    """

    shadow_offset = ListProperty((0, 4))
    """
    See :attr:`eze.uix.behaviors.elevation.CommonElevationBehavior.shadow_offset`
    attribute for more information.

    .. versionadded:: 1.1.0

    :attr:`shadow_offset` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 4]`.
    """

    radius = ListProperty([dp(7), dp(7), dp(7), dp(7)])
    """
    Dialog corners rounding value.

    .. code-block:: python

        [...]
            self.dialog = EZEDialog(
                text="Oops! Something seems to have gone wrong!",
                radius=[20, 7, 20, 7],
            )
            [...]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[7, 7, 7, 7]`.
    """

    _scale_x = NumericProperty(1)
    _scale_y = NumericProperty(1)


class EZEDialog(BaseDialog):
    """
    Dialog class.

    For more information, see in the
    :class:`~eze.theming.ThemableBehavior` and
    :class:`~kivy.uix.modalview.ModalView` and
    :class:`~eze.uix.behaviors.CommonElevationBehavior`
    classes documentation.
    """

    title = StringProperty()
    """
    Title dialog.

    .. code-block:: python

        [...]
            self.dialog = EZEDialog(
                title="Reset settings?",
                buttons=[
                    EZEFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    EZEFlatButton(
                        text="ACCEPT",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
            [...]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-title.png
        :align: center

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text = StringProperty()
    """
    Text dialog.

    .. code-block:: python

        [...]
            self.dialog = EZEDialog(
                title="Reset settings?",
                text="This will reset your device to its default factory settings.",
                buttons=[
                    EZEFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    EZEFlatButton(
                        text="ACCEPT",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
            [...]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-text.png
        :align: center

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    buttons = ListProperty()
    """
    List of button objects for dialog.
    Objects must be inherited from :class:`~eze.uix.button.BaseButton` class.

    .. code-block:: python

        [...]
            self.dialog = EZEDialog(
                text="Discard draft?",
                buttons=[
                    EZEFlatButton(text="CANCEL"), EZERaisedButton(text="DISCARD"),
                ],
            )
            [...]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-buttons.png
        :align: center

    :attr:`buttons` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    items = ListProperty()
    """
    List of items objects for dialog.
    Objects must be inherited from :class:`~eze.uix.list.BaseListItem` class.

    With type 'simple'
    ~~~~~~~~~~~~~~~~~~

    .. code-block:: python

        from kivy.lang import Builder
        from kivy.properties import StringProperty

        from eze.app import EZEApp
        from eze.uix.dialog import EZEDialog
        from eze.uix.list import OneLineAvatarListItem

        KV = '''
        <Item>

            ImageLeftWidget:
                source: root.source


        EZEFloatLayout:

            EZEFlatButton:
                text: "ALERT DIALOG"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_simple_dialog()
        '''


        class Item(OneLineAvatarListItem):
            divider = None
            source = StringProperty()


        class Example(EZEApp):
            dialog = None

            def build(self):
                self.theme_cls.theme_style = "Dark"
                self.theme_cls.primary_palette = "Orange"
                return Builder.load_string(KV)

            def show_simple_dialog(self):
                if not self.dialog:
                    self.dialog = EZEDialog(
                        title="Set backup account",
                        type="simple",
                        items=[
                            Item(text="user01@gmail.com", source="eze/images/logo/eze-icon-128.png"),
                            Item(text="user02@gmail.com", source="data/logo/kivy-icon-128.png"),
                        ],
                    )
                self.dialog.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-items.png
        :align: center

    With type 'confirmation'
    ~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: python

        from kivy.lang import Builder

        from eze.app import EZEApp
        from eze.uix.button import EZEFlatButton
        from eze.uix.dialog import EZEDialog
        from eze.uix.list import OneLineAvatarIconListItem

        KV = '''
        <ItemConfirm>
            on_release: root.set_icon(check)

            CheckboxLeftWidget:
                id: check
                group: "check"


        EZEFloatLayout:

            EZEFlatButton:
                text: "ALERT DIALOG"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_confirmation_dialog()
        '''


        class ItemConfirm(OneLineAvatarIconListItem):
            divider = None

            def set_icon(self, instance_check):
                instance_check.active = True
                check_list = instance_check.get_widgets(instance_check.group)
                for check in check_list:
                    if check != instance_check:
                        check.active = False


        class Example(EZEApp):
            dialog = None

            def build(self):
                self.theme_cls.theme_style = "Dark"
                self.theme_cls.primary_palette = "Orange"
                return Builder.load_string(KV)

            def show_confirmation_dialog(self):
                if not self.dialog:
                    self.dialog = EZEDialog(
                        title="Phone ringtone",
                        type="confirmation",
                        items=[
                            ItemConfirm(text="Callisto"),
                            ItemConfirm(text="Luna"),
                            ItemConfirm(text="Night"),
                            ItemConfirm(text="Solo"),
                            ItemConfirm(text="Phobos"),
                            ItemConfirm(text="Diamond"),
                            ItemConfirm(text="Sirena"),
                            ItemConfirm(text="Red music"),
                            ItemConfirm(text="Allergio"),
                            ItemConfirm(text="Magic"),
                            ItemConfirm(text="Tic-tac"),
                        ],
                        buttons=[
                            EZEFlatButton(
                                text="CANCEL",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                            ),
                            EZEFlatButton(
                                text="OK",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                            ),
                        ],
                    )
                self.dialog.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-confirmation.png
        :align: center

    :attr:`items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    width_offset = NumericProperty(dp(48))
    """
    Dialog offset from device width.

    :attr:`width_offset` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(48)`.
    """

    type = OptionProperty(
        "alert", options=["alert", "simple", "confirmation", "custom"]
    )
    """
    Dialog type.
    Available option are `'alert'`, `'simple'`, `'confirmation'`, `'custom'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'alert'`.
    """

    content_cls = ObjectProperty()
    """
    Custom content class. This attribute is only available when :attr:`type` is
    set to `'custom'`.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: python

                from kivy.lang import Builder
                from kivy.uix.boxlayout import BoxLayout

                from eze.app import EZEApp
                from eze.uix.button import EZEFlatButton
                from eze.uix.dialog import EZEDialog

                KV = '''
                <Content>
                    orientation: "vertical"
                    spacing: "12dp"
                    size_hint_y: None
                    height: "120dp"

                    EZETextField:
                        hint_text: "City"

                    EZETextField:
                        hint_text: "Street"


                EZEFloatLayout:

                    EZEFlatButton:
                        text: "ALERT DIALOG"
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        on_release: app.show_confirmation_dialog()
                '''


                class Content(BoxLayout):
                    pass


                class Example(EZEApp):
                    dialog = None

                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Orange"
                        return Builder.load_string(KV)

                    def show_confirmation_dialog(self):
                        if not self.dialog:
                            self.dialog = EZEDialog(
                                title="Address:",
                                type="custom",
                                content_cls=Content(),
                                buttons=[
                                    EZEFlatButton(
                                        text="CANCEL",
                                        theme_text_color="Custom",
                                        text_color=self.theme_cls.primary_color,
                                    ),
                                    EZEFlatButton(
                                        text="OK",
                                        theme_text_color="Custom",
                                        text_color=self.theme_cls.primary_color,
                                    ),
                                ],
                            )
                        self.dialog.open()


                Example().run()

        .. tab:: Declarative Python style

            .. code-block:: python

                from eze.app import EZEApp
                from eze.uix.boxlayout import EZEBoxLayout
                from eze.uix.button import EZEFlatButton
                from eze.uix.dialog import EZEDialog
                from eze.uix.floatlayout import EZEFloatLayout
                from eze.uix.textfield import EZETextField


                class Example(EZEApp):
                    dialog = None

                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Orange"
                        return (
                            EZEFloatLayout(
                                EZEFlatButton(
                                    text="ALERT DIALOG",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                    on_release=self.show_confirmation_dialog,
                                )
                            )
                        )

                    def show_confirmation_dialog(self, *args):
                        if not self.dialog:
                            self.dialog = EZEDialog(
                                title="Address:",
                                type="custom",
                                content_cls=EZEBoxLayout(
                                    EZETextField(
                                        hint_text="City",
                                    ),
                                    EZETextField(
                                        hint_text="Street",
                                    ),
                                    orientation="vertical",
                                    spacing="12dp",
                                    size_hint_y=None,
                                    height="120dp",
                                ),
                                buttons=[
                                    EZEFlatButton(
                                        text="CANCEL",
                                        theme_text_color="Custom",
                                        text_color=self.theme_cls.primary_color,
                                    ),
                                    EZEFlatButton(
                                        text="OK",
                                        theme_text_color="Custom",
                                        text_color=self.theme_cls.primary_color,
                                    ),
                                ],
                            )
                        self.dialog.open()


                Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-custom.png
        :align: center

    :attr:`content_cls` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `'None'`.
    """

    eze_bg_color = ColorProperty(None)
    """
    Background color in the (r, g, b, a) or string format.

    :attr:`eze_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _scroll_height = NumericProperty("28dp")
    _spacer_top = NumericProperty("24dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.update_width)

        if self.size_hint == [1, 1] and (
            DEVICE_TYPE == "desktop" or DEVICE_TYPE == "tablet"
        ):
            self.size_hint = (None, None)
            self.width = min(dp(560), Window.width - self.width_offset)
        elif self.size_hint == [1, 1] and DEVICE_TYPE == "mobile":
            self.size_hint = (None, None)
            self.width = min(dp(280), Window.width - self.width_offset)

        if not self.title:
            self._spacer_top = 0

        if not self.buttons:
            self.ids.root_button_box.height = 0
        else:
            self.create_buttons()

        update_height = False
        if self.type in ("simple", "confirmation"):
            if self.type == "confirmation":
                self.ids.spacer_top_box.add_widget(EZESeparator())
                self.ids.spacer_bottom_box.add_widget(EZESeparator())
            self.create_items()
        if self.type == "custom":
            if self.content_cls:
                self.ids.container.remove_widget(self.ids.scroll)
                self.ids.container.remove_widget(self.ids.text)
                self.ids.spacer_top_box.add_widget(self.content_cls)
                self.ids.spacer_top_box.padding = (0, "24dp", "16dp", 0)
                update_height = True
        if self.type == "alert":
            self.ids.scroll.bar_width = 0

        if update_height:
            Clock.schedule_once(self.update_height)

    def update_width(self, *args) -> None:
        self.width = max(
            self.height + self.width_offset,
            min(
                dp(560) if DEVICE_TYPE != "mobile" else dp(280),
                Window.width - self.width_offset,
            ),
        )

    def update_height(self, *args) -> None:
        self._spacer_top = self.content_cls.height + dp(24)

    def update_items(self, items: list) -> None:
        self.ids.box_items.clear_widgets()
        self.items = items
        self.create_items()

    def on_open(self) -> None:
        # TODO: Add scrolling text.
        self.height = self.ids.container.height
        super().on_open()

    def get_normal_height(self) -> float:
        return (
            (Window.height * 80 / 100)
            - self._spacer_top
            - dp(52)
            - self.ids.container.padding[1]
            - self.ids.container.padding[-1]
            - 100
        )

    def edit_padding_for_item(self, instance_item) -> None:
        instance_item.ids._left_container.x = 0
        instance_item._txt_left_pad = "56dp"

    def create_items(self) -> None:
        if not self.text:
            self.ids.container.remove_widget(self.ids.text)
            height = 0
        else:
            height = self.ids.text.height

        for item in self.items:
            if issubclass(item.__class__, BaseListItem):
                height += item.height  # calculate height contents
                self.edit_padding_for_item(item)
                self.ids.box_items.add_widget(item)

        if height > Window.height:
            self.ids.scroll.height = self.get_normal_height()
        else:
            self.ids.scroll.height = height

    def create_buttons(self) -> None:
        for button in self.buttons:
            if issubclass(button.__class__, BaseButton):
                self.ids.button_box.add_widget(button)