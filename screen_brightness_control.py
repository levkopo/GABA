import os
import subprocess


def __dbus_installed():
    try:
        subprocess.run(['dbus-send'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        pass

    return True


def list_monitors():
    if __dbus_installed():
        return ["dbus"]

    output = os.popen('xrandr -q | grep " connected"').read()
    monitors = []
    for line in output.split("\n"):
        monitors.append(line.split(" ")[0])

    return monitors


def get_brightness(display=False):
    output = os.popen('xrandr --verbose | grep "Brightness: "').read()
    data = []
    for line in output.split("\n"):
        line = line.split(": ")
        if len(line) == 2:
            data.append(int(float(line[1]) * 100))

    if not display:
        return data

    if display == 'dbus':
        return [100]

    return [data[list_monitors().index(display)]]


def set_brightness(value, display):
    if display == 'dbus':
        os.system('dbus-send '
                  '--session '
                  '--type=method_call '
                  '--dest="org.gnome.SettingsDaemon.Power" '
                  '/org/gnome/SettingsDaemon/Power org.freedesktop.DBus.Properties.Set '
                  'string:"org.gnome.SettingsDaemon.Power.Screen" string:"Brightness" '
                  'variant:int32:' + str(value))
    else:
        value = value / 100

        os.system(f"xrandr --output {display} --brightness {value}")
