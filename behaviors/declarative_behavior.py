"""
Behaviors/Declarative
=====================

.. versionadded:: 1.0.0

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe
            src="https://www.youtube.com/embed/_kiaJacLz8o"
            frameborder="0"
            allowfullscreen
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
        </iframe>
    </div>

As you already know, the Kivy framework provides the best/simplest/modern
UI creation tool that allows you to separate the logic of your application
from the description of the properties of widgets/GUI components.
This tool is named `KV Language <https://kivy.org/doc/stable/guide/lang.html>`_.

But in addition to creating a user interface using the KV Language Kivy allows
you to create user interface elements directly in the Python code.
And if you've ever created a user interface in Python code, you know how ugly
it looks. Even in the simplest user interface design, which was created using
Python code it is impossible to trace the widget tree, because in Python code
you build the user interface in an imperative style.

Imperative style
----------------

.. code-block:: python

    from eze.app import EZEApp
    from eze.uix.bottomnavigation import EZEBottomNavigation, EZEBottomNavigationItem
    from eze.uix.label import EZELabel
    from eze.uix.screen import EZEScreen


    class Example(EZEApp):
        def build(self):
            screen = EZEScreen()
            bottom_navigation = EZEBottomNavigation(
                panel_color="#eeeaea",
                selected_color_background="#97ecf8",
                text_color_active="white",
            )

            data = {
                "screen 1": {"text": "Mail", "icon": "gmail"},
                "screen 2": {"text": "Discord", "icon": "discord"},
                "screen 3": {"text": "LinkedIN", "icon": "linkedin"},
            }
            for key in data.keys():
                text = data[key]["text"]
                navigation_item = EZEBottomNavigationItem(
                    name=key, text=text, icon=data[key]["icon"]
                )
                navigation_item.add_widget(EZELabel(text=text, halign="center"))
                bottom_navigation.add_widget(navigation_item)

            screen.add_widget(bottom_navigation)
            return screen


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation-styles-programming.png
    :align: center

Take a look at the above code example. This is a very simple UI. But looking
at this code, you will not be able to figure the widget tree and understand
which UI this code implements. This is named imperative programming style,
which is used in Kivy.

Now let's see how the same code is implemented using the KV language,
which uses a declarative style of describing widget properties.

Declarative style with KV language
----------------------------------

.. code-block:: python

    from kivy.lang import Builder

    from eze.app import EZEApp


    class Test(EZEApp):
        def build(self):
            return Builder.load_string(
                '''
    EZEScreen:

        EZEBottomNavigation:
            panel_color: "#eeeaea"
            selected_color_background: "#97ecf8"
            text_color_active: "white"

            EZEBottomNavigationItem:
                name: "screen 1"
                text: "Mail"
                icon: "gmail"

                EZELabel:
                    text: "Mail"
                    halign: "center"

            EZEBottomNavigationItem:
                name: "screen 2"
                text: "Discord"
                icon: "discord"

                EZELabel:
                    text: "Discord"
                    halign: "center"

            EZEBottomNavigationItem:
                name: "screen 3"
                text: "LinkedIN"
                icon: "linkedin"

                EZELabel:
                    text: "LinkedIN"
                    halign: "center"
    '''
            )


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation-styles-programming.png
    :align: center

Looking at this code, we can now clearly see the widget tree and their properties.
We can quickly navigate through the components of the screen and quickly
change/add new properties/widgets. This is named declarative UI creation style.

But now the KivyMD library allows you to write Python code in a declarative style.
Just as it is implemented in Flutter/Jetpack Compose/SwiftUI.

Declarative style with Python code
----------------------------------

.. code-block:: python

    from eze.app import EZEApp
    from eze.uix.bottomnavigation import EZEBottomNavigation, EZEBottomNavigationItem
    from eze.uix.label import EZELabel
    from eze.uix.screen import EZEScreen


    class Example(EZEApp):
        def build(self):
            return (
                EZEScreen(
                    EZEBottomNavigation(
                        EZEBottomNavigationItem(
                            EZELabel(
                                text="Mail",
                                halign="center",
                            ),
                            name="screen 1",
                            text="Mail",
                            icon="gmail",
                        ),
                        EZEBottomNavigationItem(
                            EZELabel(
                                text="Discord",
                                halign="center",
                            ),
                            name="screen 2",
                            text="Discord",
                            icon="discord",
                        ),
                        EZEBottomNavigationItem(
                            EZELabel(
                                text="LinkedIN",
                                halign="center",
                            ),
                            name="screen 3",
                            text="LinkedIN",
                            icon="linkedin",
                        ),
                        panel_color="#eeeaea",
                        selected_color_background="#97ecf8",
                        text_color_active="white",
                    )
                )
            )


    Example().run()

.. note:: The EZE library does not support creating Kivy widgets in Python
    code in a declarative style.

But you can still use the declarative style of creating Kivy widgets in Python code.
To do this, you need to create a new class that will be inherited from the Kivy
widget and the :class:`~DeclarativeBehavior` class:

.. code-block:: python

    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button

    from eze.app import EZEApp
    from eze.uix.behaviors import DeclarativeBehavior


    class DeclarativeStyleBoxLayout(DeclarativeBehavior, BoxLayout):
        pass


    class Example(EZEApp):
        def build(self):
            return (
                DeclarativeStyleBoxLayout(
                    Button(),
                    Button(),
                    orientation="vertical",
                )
            )


    Example().run()

Get objects by identifiers
--------------------------

In the declarative style in Python code, the ids parameter of the specified
widget will return only the id of the child widget/container, ignoring other ids.
Therefore, to get objects by identifiers in declarative style in Python code,
you must specify all the container ids in which the widget is nested until you
get to the desired id:

.. code-block::

    from eze.app import EZEApp
    from eze.uix.boxlayout import EZEBoxLayout
    from eze.uix.button import EZERaisedButton
    from eze.uix.floatlayout import EZEFloatLayout


    class Example(EZEApp):
        def build(self):
            return (
                EZEBoxLayout(
                    EZEFloatLayout(
                        EZERaisedButton(
                            id="button_1",
                            text="Button 1",
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                        ),
                        id="box_container_1",
                    ),
                    EZEBoxLayout(
                        EZEFloatLayout(
                            EZERaisedButton(
                                id="button_2",
                                text="Button 2",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            ),
                            id="float_container",
                        ),
                        id="box_container_2",
                    )
                )
            )

        def on_start(self):
            # {
            #     'box_container_1': <eze.uix.floatlayout.EZEFloatLayout>,
            #     'box_container_2': <eze.uix.boxlayout.EZEBoxLayout object>
            # }
            print(self.root.ids)

            # <eze.uix.button.button.EZERaisedButton>
            print(self.root.ids.box_container_2.ids.float_container.ids.button_2)


    Example().run()

Yes, this is not a very good solution, but I think it will be fixed soon.

.. warning:: Declarative programming style in Python code in the EZE library
    is an experimental feature. Therefore, if you receive errors, do not hesitate
    to create new issue in the EZE repository.
"""

from kivy.properties import StringProperty
from kivy.uix.widget import Widget


class DeclarativeBehavior:
    """
    Implements the creation and addition of child widgets as declarative
    programming style.
    """

    id = StringProperty()
    """
    Widget ID.

    :attr:`id` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        for child in args:
            if issubclass(child.__class__, Widget):
                self.add_widget(child)
                if hasattr(child, "id") and child.id:
                    self.ids[child.id] = child
