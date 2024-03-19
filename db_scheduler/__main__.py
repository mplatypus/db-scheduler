"""CLI for db_scheduler."""

import os
import sys

import hikari

import db_scheduler

if sys.platform == "win32":
    import colorama

    colorama.init()


YELLOW = "\x1b[33m"
WHITE = "\x1b[37m"

if "--version" in sys.argv or "-v" in sys.argv:
    sys.stderr.write(f"{YELLOW}DB Scheduler version: {WHITE}{db_scheduler.__version__}")
    exit(1)

if "--about" in sys.argv or "-a" in sys.argv:
    sys.stderr.write(
        f"""{YELLOW}About DB Scheduler

{WHITE}------------
DB Scheduler is a basic library, to be able to store time based triggers, and have them sent out when needed.
"""
    )
    exit(1)

sys.stderr.write(
    f"""
{YELLOW}DB Scheduler - package information
{WHITE}--------------------------------
{YELLOW}DB Scheduler version: {WHITE}{db_scheduler.__version__}
{YELLOW}Hikari version: {WHITE}{hikari.__version__}
{YELLOW}Install path: {WHITE}{os.path.abspath(os.path.dirname(__file__))}\n\n"""
)


# MIT License

# Copyright (c) 2023 MPlatypus

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
