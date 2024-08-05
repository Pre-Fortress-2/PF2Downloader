"""
Hashes the running binary with SHA-512.
Compares against remote hash which should always correspond with the latest stable release.
If it doesn't match, prompt to update the game.
"""

from sys import argv
from subprocess import run
from platform import system
from gettext import gettext as _
import hashlib
import httpx
import os
import sys
import gui
import vars

def hash_script():
    h = hashlib.sha512()
    with open(argv[0], 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def check_downloader_update():
    try:
        if system() == 'Windows':
            remote_hash = httpx.get( vars.SOURCE_URL + "/pf2cd_sha512sum_windows" )
        else:
            remote_hash = httpx.get( vars.SOURCE_URL + "/pf2cd_sha512sum_windows")
    except httpx.RequestError:
        gui.message(_("WARNING: downloader failed to check itself for updates, potentially out-of-date."))
        return

    remote_hash_string = remote_hash.text
    remote_hash_string = remote_hash_string.rstrip('\n')

    if remote_hash_string == hash_script():
        gui.message(_("PF2Downloader appears to be up-to-date."))
    elif gui.message_yes_no(_("PF2Downloader has an update available. Your current version may not work properly. Do you want to install it?")) and not vars.SCRIPT_MODE:
        gui.message_end(_('Delete PF2Downloader, then redownload and relaunch it from https://prefortress.com/download'), 0)
    elif vars.SCRIPT_MODE:
        gui.message(_("PF2Downloader out-of-date."))
    else:
        gui.message(_("User chose to skip update. Things may be broken."))
