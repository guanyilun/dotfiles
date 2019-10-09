"""Build recipes for my dotfiles"""

import os

HOME = os.environ["HOME"]

def install_dep(recipe):
    return [
        'sudo pip install py3status',
    ]

def install(recipe):
    # check whether .config/i3 exists
    cmds = []
    if os.path.exists(os.path.join(HOME, ".config/i3")):
        # make a backup
        cmds.append("mv ~/.config/i3 ~/.config/i3.bak")
    # make symbolic link
    cmds.append("mkdir -vp ~/.config")
    cmds.append("ln -s ~/dotfiles/i3 ~/.config/i3")
    return cmds
