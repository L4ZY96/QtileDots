#!/bin/sh

#  █████╗ ██╗   ██╗████████╗ ██████╗ ███████╗████████╗ █████╗ ██████╗ ████████╗
# ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
# ███████║██║   ██║   ██║   ██║   ██║███████╗   ██║   ███████║██████╔╝   ██║   
# ██╔══██║██║   ██║   ██║   ██║   ██║╚════██║   ██║   ██╔══██║██╔══██╗   ██║   
# ██║  ██║╚██████╔╝   ██║   ╚██████╔╝███████║   ██║   ██║  ██║██║  ██║   ██║   
# ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝  

# https://github.com/L4ZYP4CM4N/DOTFILES

# put you custom resolution config here, you can use arandr
xrandr --output eDP --mode 1366x768 --pos 0x0 --output HDMI-A-0 --mode 1920x1080 --rate 120  --pos 1366x0 --primary

# keymap us #
setxkbmap us &

# keymap latam #
#setxkbmap latam &

# sys icons #

cbatticon -u 5 &

volumeicon &

udiskie -t &

nm-applet &

#wallpaper
nitrogen --restore &

# transparencia #
picom &

# notifications #
dunst &
