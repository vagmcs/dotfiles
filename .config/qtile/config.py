#        _   _ _
#   __ _| |_(_) | ___
#  / _` | __| | |/ _ \
# | (_| | |_| | |  __/
#  \__, |\__|_|_|\___|
#     |_|
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


#
# IMPORTS
#
import os
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Load PyWal colors
import pywal_colors
WAL_COLORS = pywal_colors.colors

#
# GLOBAL VARIABLES
#
MOD = "mod4"                    # Set mod key to SUPER 
ALT = "mod1"                    # Set application mod key to ALT
HOME = os.environ.get("HOME")   # HOME path
terminal = guess_terminal()     # Guess terminal application
FONT = "Hack Nerd Font"

CUSTOM_COLORS = [
    # POLAR NIGHT [0 to 3]
    "#2e3440",
    "#3b4252",
    "#434c5e",
    "#4c566a",
    # SNOW STORM [4 to 6]
    "#d8dee9",
    "#e5e9f0",
    "#eceff4"
    # FROST [7 to 10]
    "#8fbcbb",
    "#88c0d0",
    "#81a1c1",
    "#5e81ac",
    # AURORA [11 to 15]
    "#bf616a",
    "#d08770",
    "#ebcb8b",
    "#a3be8c",
    "#b48ead"
]


#
# KEYBINDINGS
#
keys = [

    # Navigate between windows in current stack pane
    Key([MOD], "h", lazy.layout.left(),
        desc="Move focus right in stack pane"),
    Key([MOD], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([MOD], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([MOD], "l", lazy.layout.right(),
        desc="Move focus left in stack pane"),

    # Move windows in current stack
     Key([MOD, "control"], "h", lazy.layout.shuffle_left(),
        desc="Move window down in current stack "),
    Key([MOD, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([MOD, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([MOD, "control"], "l", lazy.layout.shuffle_right(),
        desc="Move window up in current stack "),

    # Move windows in current stack
    Key([MOD, "shift"], "h", lazy.layout.grow_left(),
        desc="Move window down in current stack "),
    Key([MOD, "shift"], "j", lazy.layout.grow_up(),
        desc="Move window up in current stack "),
    Key([MOD, "shift"], "k", lazy.layout.grow_down(),
        desc="Move window down in current stack "),
    Key([MOD, "shift"], "l", lazy.layout.grow_right(),
        desc="Move window up in current stack "),

    Key([MOD, "shift"], "i", lazy.layout.increase_ratio(), desc="Inc"),

    # Switch window focus to other pane(s) of stack
    Key([MOD], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    #Key([MOD, "shift"], "space", lazy.layout.rotate(),
        #desc="Swap panes of split stack"),

    # Toggle between different layouts as defined below
    Key([MOD, "shift"], "Tab", lazy.previous_layout(),
        desc="Toggle between layouts"),
    Key([MOD], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([MOD, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([MOD], "Return", lazy.spawn(terminal),
        desc="Launch terminal application"),

    Key([MOD, "shift"], "Return", lazy.spawn("rofi -show drun"),
        desc="Launch rofi launcher"),

    Key([MOD, "shift"], "c", lazy.window.kill(),
        desc="Kill focused window"),

    Key([MOD, "control"], "r", lazy.restart(),
        desc="Restart qtile"),

    Key([MOD, "control"], "q", lazy.shutdown(),
        desc="Shutdown qtile"),

    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute"))
]


#
# MOUSE BINDINGS
#
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front())
]


#
# GROUPS
#
group_names = [
    (" SYS", {'layout': 'monadtall'}),
    (" DEV", {'layout': 'monadtall'}),
    (" WWW", {'layout': 'monadtall'}),
    (" DOC", {'layout': 'monadtall'}),
    (" SCI", {'layout': 'monadtall'}),
    (" MAIL", {'layout': 'monadtall'}),
    (" MUS", {'layout': 'monadtall'}),
    (" VID", {'layout': 'monadtall'}),
    (" FUN", {'layout': 'floating'})
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([MOD], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([MOD, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group


#
# LAYOUTS
#
layout_config = {
    "margin": 8,
    "border_width": 4,
    "border_focus": WAL_COLORS[6], #CUSTOM_COLORS[13],
    "border_normal": WAL_COLORS[8] #CUSTOM_COLORS[4]
}

layouts = [
    layout.Max(),
    layout.Bsp(**layout_config),
    layout.Matrix(**layout_config),
    layout.MonadTall(**layout_config),
    layout.MonadWide(**layout_config),
    layout.Floating(border_width=4, border_focus=WAL_COLORS[6], border_normal=WAL_COLORS[8])
]


#
# WIDGETS
#
widget_defaults = dict(
    font = FONT,
    fontsize = 15,
    padding = 3,
    background = WAL_COLORS[0], #CUSTOM_COLORS[0],
    foreground = WAL_COLORS[7] #CUSTOM_COLORS[5]
)
extension_defaults = widget_defaults.copy()

widget_list = [
    widget.Sep(linewidth = 0, padding = 5),
    widget.GroupBox(
        rounded = True,
        #padding_x = 2,
        padding_y = 6,
        #borderwidth = 3,
        active = WAL_COLORS[3], #CUSTOM_COLORS[12],
        inactive = WAL_COLORS[7], #CUSTOM_COLORS[5],
        block_highlight_text_color = WAL_COLORS[15], #CUSTOM_COLORS[5],
        this_current_screen_border = WAL_COLORS[1], #CUSTOM_COLORS[11],
        this_screen_border = WAL_COLORS[1], #CUSTOM_COLORS[11],
        highlight_method = "block"
    ),
    widget.Spacer(length=bar.STRETCH),
    widget.CPU(
        format = " {load_percent}%",
        background = WAL_COLORS[1] #CUSTOM_COLORS[11]
    ),
    #widget.ThermalSensor(
    #    fmt = " {}",
    #    background = CUSTOM_COLORS[11]
    #),
    widget.Memory(
        format = " {MemUsed}MB",
        background = WAL_COLORS[11] #CUSTOM_COLORS[11]
    ),
    widget.TextBox(
        text = "Layout:",
        background = WAL_COLORS[4] #CUSTOM_COLORS[8]
    ),
    widget.CurrentLayoutIcon(
        scale = 0.7,
        background = WAL_COLORS[4] #CUSTOM_COLORS[8]
    ),
    widget.Volume(
        fmt = " {}",
        background = WAL_COLORS[6] #CUSTOM_COLORS[9]
    ),
    widget.Clock(
        format = " %a %d %b  %H:%M",
        background = WAL_COLORS[8] #CUSTOM_COLORS[3]
    ),
    widget.KeyboardLayout(
        configured_keyboards=["us", "gr"]
    )
]


#
# SCREENS
#
screens = [Screen(
    top=bar.Bar(widgets = widget_list, margin = [4, 6, 1, 6], opacity = 0.85, size = 28),
    bottom=bar.Bar(background=WAL_COLORS[0], widgets=[
        widget.WindowName(
            foreground = WAL_COLORS[5], #CUSTOM_COLORS[14],
            font = FONT + " Bold"
        ),
        widget.CheckUpdates(
            background= WAL_COLORS[0], #CUSTOM_COLORS[0],
            display_format=" : {updates}",
            fontsize = 15,
            mouse_callbacks = {"Button1": lambda qtile: qtile.cmd_spawn("pamac-manager")}
        ),
        widget.Systray(
            icon_size=24,
            padding=10
        )
    ], margin = [1, 6, 4, 6], opacity = 0.85, size = 28)
)]


#
# HOOKS
#
@hook.subscribe.startup_once
def autostart():
    subprocess.call([HOME + "/.config/qtile/autostart.sh"])


#
# GENERAL CONFIGURATION
#
main = None
auto_fullscreen = True
bring_front_click = True
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []
focus_on_window_activation = "smart"
follow_mouse_focus = True

floating_layout = layout.Floating(float_rules=[
    # Run xprop to see the wm class 
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])

wmname = "LG3D" # Hack for Java UI toolkit

