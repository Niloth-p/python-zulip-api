#!/usr/bin/env python
import os
import zulip

import argparse

def main():
    usage = """zulip-api-examples [script_name]

Prints the path to the Zulip API example scripts."""
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('script_name',
                        nargs='?',
                        default='',
                        help='print path to the script <script_name>')
    args = parser.parse_args()
    zulip_path = os.path.abspath(os.path.dirname(zulip.__file__))
    examples_path = os.path.abspath(os.path.join(zulip_path, 'examples', args.script_name))
    if os.path.isdir(examples_path) or (args.script_name and os.path.isfile(examples_path)):
        print(examples_path)
    else:
        raise OSError("Examples cannot be accessed at {}: {} does not exist!"
                      .format(examples_path,
                              "File" if args.script_name else "Directory"))

if __name__ == '__main__':
    main()