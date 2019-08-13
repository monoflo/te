#!/usr/bin/env python3
# -*- coding: utf-8 -*-`

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Touch module.

This module provides a touch function which is used to create empty files.
"""

def touch(filepath: str):
    """Creates a file by opening it in append mode.

    Args:
        the path of the file to create.
    """
    with open(filepath, 'a'):
        pass
