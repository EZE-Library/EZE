"""
PyInstaller hook for EZE
===========================

Adds fonts, images and KV files to package.

All modules from uix directory are added by Kivy hook.
"""

import os
from pathlib import Path

import eze

datas = [
    # Add `.ttf` files from the `eze/fonts` directory.
    (
        eze.fonts_path,
        str(Path("eze").joinpath(Path(eze.fonts_path).name)),
    ),
    # Add files from the `eze/images` directory.
    (
        eze.images_path,
        str(Path("eze").joinpath(Path(eze.images_path).name)),
    ),
]

# Add `.kv. files from the `eze/uix` directory.
for path_to_kv_file in Path(eze.uix_path).glob("**/*.kv"):
    datas.append(
        (
            str(Path(path_to_kv_file).parent.joinpath("*.kv")),
            str(
                Path("eze").joinpath(
                    "uix",
                    str(Path(path_to_kv_file).parent).split(
                        str(Path("eze").joinpath("uix")) + os.sep
                    )[1],
                )
            ),
        )
    )
