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

