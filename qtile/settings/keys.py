# ██╗  ██╗███████╗██╗   ██╗███████╗
# ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝
# █████╔╝ █████╗   ╚████╔╝ ███████╗
# ██╔═██╗ ██╔══╝    ╚██╔╝  ╚════██║
# ██║  ██╗███████╗   ██║   ███████║
# ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝

# https://github.com/L4ZYP4CM4N/DOTFILES

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    

    # System #

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),
    
    # power menu
    ([mod], "q", lazy.spawn("sh .config/qtile/scripts/rofi/powermenu.sh")),

    #Exit Qtile
    ([mod, "control"], "q", lazy.shutdown()),
    

    # Aplications

    # Menu rofi
    #([mod, "shift"], "Space", lazy.spawn("rofi -show run")),
    ([mod], "Space", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "Space", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "f", lazy.spawn("firefox")),

    # File Explorer
    ([mod], "t", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Code
    ([mod], "c", lazy.spawn("code-oss")),

    # Spotify
    ([mod], "s", lazy.spawn("spotify")),

    # Screenshot
    ([mod], "p", lazy.spawn("sh .config/qtile/scripts/ScreenShoTer --active")),
    ([mod, "shift"], "p", lazy.spawn("sh .config/qtile/scripts/ScreenShoTer --sel")),
    ([mod, "control"], "p", lazy.spawn("sh .config/qtile/scripts/ScreenShoTer --now")),


    # Custom scripts

    #Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "sh .config/qtile/scripts/Volume --dec"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "sh .config/qtile/scripts/Volume --inc"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "sh .config/qtile/scripts/Volume --toggle"
    )),

    #MediaKeys
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")), 

    #Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("sh .config/qtile/scripts/Brightness up")),
    ([], "XF86MonBrightnessDown", lazy.spawn("sh .config/qtile/scripts/Brightness down")),

]]
