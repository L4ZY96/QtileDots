# ██╗    ██╗██╗██████╗  ██████╗ ███████╗████████╗███████╗
# ██║    ██║██║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝██╔════╝
# ██║ █╗ ██║██║██║  ██║██║  ███╗█████╗     ██║   ███████╗
# ██║███╗██║██║██║  ██║██║   ██║██╔══╝     ██║   ╚════██║
# ╚███╔███╔╝██║██████╔╝╚██████╔╝███████╗   ██║   ███████║
#  ╚══╝╚══╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝

# https://github.com/L4ZYP4CM4N/DOTFILES


from libqtile import widget
from .theme import colors
from libqtile.lazy import lazy
from libqtile.command import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration


# Quick settings #
font="UbuntuMono Nerd Font Bold"
arch_size= 30
power_line_size = 37
font_size = 20
icon_size = 22
workspace_icon_size = 28

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }
def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        **decorations(),
        text=" ", #   
        fontsize= power_line_size,
        padding= -3
    )

def powerline1(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        **decorations(),
        text=" ", #   
        fontsize= power_line_size,
        padding= -3
    )

def icon(fg='text', bg='dark', fontsize=icon_size, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        **decorations(),
        fontsize=fontsize,
        text=text,
        padding=1,
    )

def decorations():
    return { "decorations" : [
            BorderDecoration (
                border_width = [4, 0, 4, 0],
                colour=colors['dark']
            ) 
        ]}


def workspaces(): 
    return [

        powerline('color5', 'dark'),

        widget.TextBox(
            text="󰣇 ",
            **base("light", "color5"),
            #decorations = [
            #BorderDecoration (
            #    border_width = [8, 0, 8, 0],
            #    colour=colors['dark']
            #) 
        #],
            fontsize=arch_size,
            mouse_callbacks={"Button1": lazy.spawn("rofi -show drun"), "Button3": lazy.spawn("sh .config/qtile/scripts/rofi/powermenu.sh")}
        ), 
            
        powerline1('color5', 'dark'),

        widget.GroupBox(
            **base(fg='light'),
            font=font,
            fontsize=workspace_icon_size,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='text', # box, text, block, line
            urgent_alert_method='text',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),

    ]


primary_widgets = [
    *workspaces(),

    powerline1('dark', 'color5'),

    widget.CurrentLayoutIcon(**base(bg='color5'), scale=0.65),

    widget.CurrentLayout(**base(fg='text', bg='color5'), padding=5),
    
    powerline1('color5', 'dark'),

    widget.WindowName(**base(fg='focus'), padding=5),

    powerline('color4', 'dark'),

    icon(bg="color4", text='󰅢 '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string=' 0',
        display_format=' {updates}',
        update_interval=1800,
        custom_command='checkupdates',
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e sudo pacman -Syu")},
    ),

    powerline('color3', 'color4'),

    icon(bg="color3", text='  '),  
    
    widget.Memory(
        **base(bg="color3"),
        measure_mem='G',
        format='{MemUsed: .0f}{mm} ',# /{MemTotal: .0f}{mm}
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e gotop")}
    ), 

    icon(bg="color3", text=' '), 

    widget.Net(
        **base(bg='color3'),
        interface='wlan0',
        format='{total}', #to have the up and down separed put this {down}  {up}
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e gotop")}
    ),

    powerline("color2", "color3"),

    icon(bg="color2", text='󱤓 '), 

    widget.CPU(
        **base(bg='color2'),
        format='{load_percent}%',  #{freq_current}GHz',
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e gotop")}
    ), 

    icon(bg="color2", text=' 󱩅 '), 

    widget.ThermalSensor(
        **base(bg='color2'),
        tag_sensor="edge",
        threshold=70,
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e gotop")}
    ),

    powerline('color1', 'color2'),

    icon(bg="color1", text='󰃰 '), 

    widget.Clock(
        **base(bg='color1'),
        format='%H:%M %d/%m/%y ', 
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e calcurse")}
    ),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),

    separator(),
]

secondary_widgets = [
    *workspaces(),
        
    powerline1('dark', 'color5'),

    widget.CurrentLayoutIcon(**base(bg='color5'), scale=0.65),

    widget.CurrentLayout(**base(bg='color5'), padding=5),
    
    powerline1('color5', 'dark'),

    widget.WindowName(**base(fg='focus'), padding=5),

    powerline('color4', 'dark'),

    icon(bg="color4", text='󰅢 '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string=' 0',
        display_format=' {updates}',
        update_interval=1800,
        custom_command='checkupdates',
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e sudo pacman -Syu")},
    ),

    powerline('color3', 'color4'),

    icon(bg="color3", text='  '),  
    
    widget.Memory(
        **base(bg="color3"),
        measure_mem='G',
        format='{MemUsed: .0f}{mm} ',# /{MemTotal: .0f}{mm}
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e gotop")}
    ), 

    icon(bg="color3", text=' '), 

    widget.Net(
        **base(bg='color3'),
        interface='wlan0',
        format='{total}', #to have the up and down separed put this {down}  {up}
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e gotop")}
    ),


    powerline("color2", "color3"),

    icon(bg="color2", text='󱤓 '), 

    widget.CPU(
        **base(bg='color2'),
        format='{load_percent}%',  #{freq_current}GHz',
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e gotop")}
    ), 

    icon(bg="color2", text=' 󱩅 '), 

    widget.ThermalSensor(
        **base(bg='color2'),
        tag_sensor="edge",
        threshold=70,
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e gotop")}
    ),

    powerline('color1', 'color2'),

    icon(bg="color1", text='󰃰 '), 

    widget.Clock(
        **base(bg='color1'),
        format='%H:%M %d/%m/%y ', 
        mouse_callbacks={"Button1": lazy.spawn("alacritty -e calcurse")}
    ),

    powerline1("color1", "dark")
]

widget_defaults = {
    **decorations(),
    'font': font,
    'fontsize': font_size,
    'padding': -1,
}
extension_defaults = widget_defaults.copy()
