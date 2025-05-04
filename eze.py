"""
EZE: Simplified and Easier KIVY Library
=======================

.. seealso::
EZE is a powerful Python library built on top 
of KIVY and KIVYMD, designed to provide a simplified and 
intuitive interface for building user-friendly applications. 

By combining the strengths of both KIVY and 
KIVYMD, EZE offers a seamless development experience.
"""

from eze.app import EZEApp
from eze.uix.label import EZELabel

class MainApp(EZEApp):
    def build(self):
        return EZELabel(text="Hello World!", halign="center")
MainApp().run()
