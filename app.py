"""
Themes/Material App
===================

This module contains :class:`EZEApp` class that is inherited from
:class:`~kivy.app.App`. :class:`EZEApp` has some properties needed for ``EZE``
library (like :attr:`~EZEApp.theme_cls`). You can turn on the monitor displaying
the current ``FPS`` value in your application:

.. code-block:: python

    KV = '''
    EZEScreen:

        EZELabel:
            text: "Hello World!"
            halign: "center"
    '''

    from kivy.lang import Builder

    from eze.app import EZEApp


    class MainApp(EZEApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            self.fps_monitor_start()


    MainApp().run()


"""

__all__ = ("EZEApp",)

import os

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.core.window import Window
import watchdog 

from kivy.properties import ObjectProperty, StringProperty

from eze.theming import ThemeManager


Window.size = (320, 580)


class FpsMonitoring:
    """Implements a monitor to display the current FPS in the toolbar."""

    def fps_monitor_start(self, anchor: str = "top") -> None:
        """Adds a monitor to the main application window."""

        def add_monitor(*args):
            from kivy.core.window import Window

            from eze.utils.fpsmonitor import FpsMonitor

            monitor = FpsMonitor(anchor=anchor)
            monitor.start()
            Window.add_widget(monitor)

        Clock.schedule_once(add_monitor)


class EZEApp(App, FpsMonitoring):
    """
    Application class, see :class:`~kivy.app.App` class documentation for more
    information.
    """

    icon = StringProperty("eze/images/logo/eze-icon-512.png")
    """
    See :attr:`~kivy.app.App.icon` attribute for more information.

    .. versionadded:: 1.1.0

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    adn default to `eze/images/logo/eze-icon-512.png`.
    """

    theme_cls = ObjectProperty()
    """
    Instance of :class:`~ThemeManager` class.

    .. Warning:: The :attr:`~theme_cls` attribute is already available
        in a class that is inherited from the :class:`~EZEApp` class.
        The following code will result in an error!

    .. code-block:: python

        class MainApp(EZEApp):
            theme_cls = ThemeManager()
            theme_cls.primary_palette = "Teal"

    .. Note:: Correctly do as shown below!

    .. code-block:: python

        class MainApp(EZEApp):
            def build(self):
                self.theme_cls.primary_palette = "Teal"

    :attr:`theme_cls` is an :class:`~kivy.properties.ObjectProperty`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = ThemeManager()

    def load_all_kv_files(self, path_to_directory: str) -> None:
        """
        Recursively loads KV files from the selected directory.

        .. versionadded:: 1.0.0
        """

        for path_to_dir, dirs, files in os.walk(path_to_directory):
            # When using the `load_all_kv_files` method, all KV files
            # from the `EZE` library were loaded twice, which leads to
            # failures when using application built using `PyInstaller`.
            if "eze" in path_to_directory:
                Logger.critical(
                    "EZE: "
                    "Do not use the word 'eze' in the name of the directory "
                    "from where you download KV files"
                )
            if (
                "venv" in path_to_dir
                or ".buildozer" in path_to_dir
                or os.path.join("eze") in path_to_dir
            ):
                continue
            for name_file in files:
                if (
                    os.path.splitext(name_file)[1] == ".kv"
                    and name_file != "style.kv"  # if use PyInstaller
                    and "__MACOS" not in path_to_dir  # if use Mac OS
                ):
                    path_to_kv_file = os.path.join(path_to_dir, name_file)
                    Builder.load_file(path_to_kv_file)
