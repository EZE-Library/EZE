"""
EZE
======
Simplified and Easier KIVY Library
======

EZE is a powerful Python library built on top of KIVY and KIVYMD,
designed to provide a simplified and intuitive interface for 
building user-friendly applications. By combining the strengths 
of both KIVY and KIVYMD, EZE offers a seamless development experience.

it's a collection of Material Design compliant widgets for use with,
`Kivy cross-platform graphical framework <http://kivy.org/#home>`
a framework for cross-platform, touch-enabled graphical applications.
The project's goal is to approximate Google's `Material Design spec
<https://material.io/design/introduction>`_ as close as possible without
sacrificing ease of use.

This library is meant to make development with kivy easier.
I Martin Onyisi (Martony) found the strength of EZE and brought this
project to a new level.

"""

import os

import kivy
from kivy.logger import Logger

__version__ = "0.1.0"
"""EZE version."""

release = False
if "READTHEDOCS" not in os.environ:
    kivy.require("2.2.0")

try:
    from eze._version import __date__, __hash__, __short_hash__
except ImportError:
    __hash__ = __short_hash__ = __date__ = ""

path = os.path.dirname(__file__)
"""Path to EZE package directory."""

fonts_path = os.path.join(path, f"fonts{os.sep}")
"""Path to fonts directory."""

images_path = os.path.join(path, f"images{os.sep}")
"""Path to images directory."""

uix_path = os.path.join(path, "uix")
"""Path to uix directory."""

_log_message = (
    "EZE:"
    + (" Release" if release else "")
    + f" {__version__}"
    + (f", git-{__short_hash__}" if __short_hash__ else "")
    + (f", {__date__}" if __date__ else "")
    + f' (installed at "{__file__}")'
)
Logger.info(_log_message)
Logger.warning(
    "EZE: "
    "Version 0.0.1 is deprecated and is no longer supported. "
    "Use EZE version 0.1.0 from the master branch "
    "(pip install eze)"
)

import eze.factory_registers  # NOQA
import eze.font_definitions  # NOQA
from eze.tools.packaging.pyinstaller import hooks_path  # NOQA
