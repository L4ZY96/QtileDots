#  ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ███████╗
# ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██╔════╝
# ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝███████╗
# ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ╚════██║
# ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ███████║
#  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝

# https://github.com/L4ZYP4CM4N/DOTFILES

from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from .keys import mod, keys

"""
groups = [Group(f"{i+1}", label=" ") for i in range(6)]   #      󰊠

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )
"""

__groups = {
    1: Group("󰈹 ", matches=[Match(wm_class=["firefox"])]),
    2: Group(" "), 
    3: Group("󰨞 ", matches=[Match(wm_class=["code-oss"])]),
    4: Group(" ", matches=[Match(wm_class=["Thunar"])]),
    5: Group(" "),
    6: Group(" ", matches=[Match(wm_class=["Spotify"])]),
}
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1+shift+letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
