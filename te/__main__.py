#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Main module.

This module provides the main function of the module.
"""

from os.path import isdir, join
from sys import stderr
from te.parsers import parse_args, format_names
from te.touch import touch

def main():
    """The main function of the module."""
    args = parse_args()

    if not isdir(args.destdir):
        print("\"{}\" is not a directory".format(args.destdir), file=stderr)
        exit(-1)

    names = format_names(args.input)

    num_digits = str(len(str(len(names))))
    fmt_str = '{:0' + num_digits + 'd}_{}.' + args.extension

    for count, name in enumerate(names):
        touch(join(args.destdir, fmt_str.format(count, name)))

main()
