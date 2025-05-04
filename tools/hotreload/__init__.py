__all__ = ("HotReload", )
from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from eze.uix.behaviors import SpecificBackgroundColorBehavior
from eze.tools.hotreload import app