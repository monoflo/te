#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Parsers module.

This module provides a parse_args function that parses the arguments supplied to
the application, in addition to a format_names function that converts the file
names on each line of the input file to the preferred format.
"""

import argparse as ap
from re import sub
from sys import stdin, stderr
from _io import TextIOWrapper

def parse_args():
    """Parses the command-line arguments.

    Returns:
        the populated namespace.
    """
    parser = ap.ArgumentParser(prog="te",
                               description="Creates an enumeration of files")

    parser.add_argument('input', nargs='?',
                        type=ap.FileType('r', encoding='UTF-8'), default=stdin,
                        help="the file containing the filenames to enumerate")

    parser.add_argument('-d', '--destdir', type=str, default=".",
                        help="the directory in which to create the files")

    parser.add_argument('-e', '--extension', type=str, default="txt",
                        help="the file extension to use")

    return parser.parse_args()

def format_names(file: TextIOWrapper):
    """Parses each line of the file to format file names.

    Args:
        the input file.

    Returns:
        the list of valid, formatted filenames.
    """
    names = []
    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.replace(' ', '_')
        line = sub("[^A-Za-z0-9_]+", '', line)

        if line.isprintable() and not line.isspace():
            names.append(line)

        else:
            print("\"{}\"  skipped".format(line), file=stderr)

    return names
