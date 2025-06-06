"""
Behaviors/ToggleButton
======================

This behavior must always be inherited after the button's Widget class since it
works with the inherited properties of the button class.

example:

.. code-block:: python

    class MyToggleButtonWidget(EZEFlatButton, EZEToggleButton):
        # [...]
        pass


.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from eze.app import EZEApp
            from eze.uix.behaviors.toggle_behavior import EZEToggleButton
            from eze.uix.button import EZEFlatButton

            KV = '''
            EZEScreen:

                EZEBoxLayout:
                    adaptive_size: True
                    spacing: "12dp"
                    pos_hint: {"center_x": .5, "center_y": .5}

                    MyToggleButton:
                        text: "Show ads"
                        group: "x"

                    MyToggleButton:
                        text: "Do not show ads"
                        group: "x"

                    MyToggleButton:
                        text: "Does not matter"
                        group: "x"
            '''


            class MyToggleButton(EZEFlatButton, EZEToggleButton):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.background_down = self.theme_cls.primary_color


            class Test(EZEApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Test().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from eze.app import EZEApp
            from eze.uix.behaviors.toggle_behavior import EZEToggleButton
            from eze.uix.boxlayout import EZEBoxLayout
            from eze.uix.button import EZEFlatButton
            from eze.uix.screen import EZEScreen


            class MyToggleButton(EZEFlatButton, EZEToggleButton):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.background_down = self.theme_cls.primary_color


            class Test(EZEApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        EZEScreen(
                            EZEBoxLayout(
                                MyToggleButton(
                                    text="Show ads",
                                    group="x",
                                ),
                                MyToggleButton(
                                    text="Do not show ads",
                                    group="x",
                                ),
                                MyToggleButton(
                                    text="Does not matter",
                                    group="x",
                                ),
                                adaptive_size=True,
                                spacing="12dp",
                                pos_hint={"center_x": .5, "center_y": .5},
                            ),
                        )
                    )


            Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toggle-button-1.gif
    :align: center

You can inherit the ``MyToggleButton`` class only from the following classes
----------------------------------------------------------------------------

- :class:`~eze.uix.button.EZERaisedButton`
- :class:`~eze.uix.button.EZEFlatButton`
- :class:`~eze.uix.button.EZERectangleFlatButton`
- :class:`~eze.uix.button.EZERectangleFlatIconButton`
- :class:`~eze.uix.button.EZERoundFlatButton`
- :class:`~eze.uix.button.EZERoundFlatIconButton`
- :class:`~eze.uix.button.EZEFillRoundFlatButton`
- :class:`~eze.uix.button.EZEFillRoundFlatIconButton`
"""

__all__ = ("EZEToggleButton",)

from kivy.properties import BooleanProperty, ColorProperty
from kivy.uix.behaviors import ToggleButtonBehavior

from eze.uix.button import (
    ButtonContentsIconText,
    EZEFillRoundFlatButton,
    EZEFillRoundFlatIconButton,
    EZEFlatButton,
    EZERaisedButton,
    EZERectangleFlatButton,
    EZERectangleFlatIconButton,
    EZERoundFlatButton,
    EZERoundFlatIconButton,
)


class MDToggleButton(ToggleButtonBehavior):
    background_normal = ColorProperty(None)
    """
    Color of the button in ``rgba`` format for the 'normal' state.

    :attr:`background_normal` is a :class:`~kivy.properties.ColorProperty`
    and is defaults to `None`.
    """

    background_down = ColorProperty(None)
    """
    Color of the button in ``rgba`` format for the 'down' state.

    :attr:`background_down` is a :class:`~kivy.properties.ColorProperty`
    and is defaults to `None`.
    """

    font_color_normal = ColorProperty(None)
    """
    Color of the font's button in ``rgba`` format for the 'normal' state.

    :attr:`font_color_normal` is a :class:`~kivy.properties.ColorProperty`
    and is defaults to `None`.
    """

    font_color_down = ColorProperty([1, 1, 1, 1])
    """
    Color of the font's button in ``rgba`` format for the 'down' state.

    :attr:`font_color_down` is a :class:`~kivy.properties.ColorProperty`
    and is defaults to `[1, 1, 1, 1]`.
    """

    __is_filled = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        classinfo = (
            EZERaisedButton,
            EZEFlatButton,
            EZERectangleFlatButton,
            EZERectangleFlatIconButton,
            EZERoundFlatButton,
            EZERoundFlatIconButton,
            EZEFillRoundFlatButton,
            EZEFillRoundFlatIconButton,
        )
        # Do the object inherited from the "supported" buttons?
        if not issubclass(self.__class__, classinfo):
            raise ValueError(
                f"Class {self.__class__} must be inherited from one of the "
                f"classes in the list {classinfo}"
            )
        if (
            not self.background_normal
        ):  # This means that if the value == [] or None will return True.
            # If the object inherits from buttons with background:
            if isinstance(
                self,
                (
                    EZERaisedButton,
                    EZEFillRoundFlatButton,
                    EZEFillRoundFlatIconButton,
                ),
            ):
                self.__is_filled = True
                self.background_normal = self.theme_cls.primary_color
            # If not background_normal must be the same as the inherited one.
            else:
                self.background_normal = (
                    self.eze_bg_color[:] if self.eze_bg_color else (0, 0, 0, 0)
                )
        # If no background_down is setter.
        if (
            not self.background_down
        ):  # This means that if the value == [] or None will return True.
            self.background_down = (
                self.theme_cls.primary_dark
            )  # get the primary_color dark from theme_cls
        if not self.font_color_normal:
            self.font_color_normal = self.theme_cls.primary_color
        # Alternative to bind the function to the property.
        # self.bind(state=self._update_bg)
        self.fbind("state", self._update_bg)

    def _update_bg(self, ins, val):
        """Updates the color of the background."""

        if val == "down":
            self.eze_bg_color = self.background_down
            if (
                self.__is_filled is False
            ):  # If the background is transparent, and the button it toggled,
                # the font color must be withe [1, 1, 1, 1].
                self.text_color = self.font_color_down
            if self.group:
                self._release_group(self)
        else:
            self.eze_bg_color = self.background_normal
            if (
                self.__is_filled is False
            ):  # If the background is transparent, the font color must be the
                # primary color.
                self.text_color = self.font_color_normal

        if issubclass(self.__class__, ButtonContentsIconText):
            self.icon_color = self.text_color
