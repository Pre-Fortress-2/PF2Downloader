"""
Tiny module that currently just establishes
the temp paths and some variables for other
modules to use.
"""
from platform import system
import sys
import tempfile

DEBUG = True

if system() == 'Windows':
    TEMP_PATH = tempfile.gettempdir()
else:
    TEMP_PATH = '/var/tmp/'

# For determining whether we're installing or updating/repairing the game
INSTALLED = False

ARIA2C_BINARY = None
BUTLER_BINARY = None
INSTALL_PATH = None
PF2_PATH = None

SCRIPT_MODE = len(sys.argv) > 1

SOURCE_URL = 'https://archive.prefortress.com/' # store the actual files here
CONTENT_URL = "https://prefortress.com/" # store version info here

if DEBUG:
    CONTENT_URL = "https://localhost:4000/"

# Only on Linux
TO_SYMLINK = [
    ["/pf2/bin/server.so", "/pf2/bin/server_srv.so"]
]

HELP_MENU = '''Usage: PF2Downloader [COMMAND] [PATH]
Installation utility for Pre-Fortress 2

If no arguments are provided, the downloader will be ran in setup mode, in
which a series of questions will be asked to install the game for a regular
user. This is what's used when opening the downloader from the desktop.

Valid commands:
  --install           installs Pre-Fortress 2 into a new folder inside PATH
  --update            updates the pre-existing Pre-Fortress 2 installation in its
                      folder inside PATH
  --help              shows this

PATH is the folder containing Pre-Fortress 2's folder. This is usually the
sourcemods folder for clients, or the Source dedicated server folder for
servers.

If PATH isn't provided, then it'll be replaced with the detected path to the
sourcemods folder in the Steam directory. If it couldn't be detected, then the
path will be the current work directory.'''