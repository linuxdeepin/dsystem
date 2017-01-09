#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

from dogtail.tree import *
from lib import utils
import time
import dbus

class Dde_control_center:
    def __init__(self):
        self.dccObj = root.application(appName='dde-control-center', description='/usr/bin/dde-control-center')
        self.dbus_name = 'com.deepin.dde.ControlCenter'
        self.obj_path = '/com/deepin/dde/ControlCenter'
        self.interface = 'com.deepin.dde.ControlCenter'

    def moveAllSettingsDown(self):
        allsettings_string = 'All Settings'
        allsettings = self.dccObj.child(allsettings_string)
        if None == allsettings:
            return False

        x, y = utils.getWidgetCenterPoint(allsettings)
        utils.m.move(x, y + 50)
        time.sleep(2)
        return True


    def openGUI(self):
        utils.m.move(utils.resolution.width - 1, utils.resolution.height - 1)
        time.sleep(3)

    def openModule(self, modulename = None):
        if None == modulename:
            return False

        module = self.dccObj.child(modulename)
        if None == module:
            return False

        if False == self.moveAllSettingsDown():
            return False

        while True:
            module = self.dccObj.child(modulename)

            if module.position[1] > 70 \
                    and module.position[1] < utils.resolution.height/2:
                return True
            elif module.position[1] <= 70:
                utils.m.scroll(vertical=1)
            elif module.position[1] >= utils.resolution.height/2:
                utils.m.scroll(vertical=-1)

class Appearance:
    def __init__(self):
        self.dbus_name  = "com.deepin.daemon.Appearance"
        self.obj_path   = "/com/deepin/daemon/Appearance"
        self.interface  = "com.deepin.daemon.Appearance"

        self.FontSize   = "FontSize"
        self.IconTheme  = "IconTheme"
        self.CursorTheme = "CursorTheme"
        self.MonospaceFont = "MonospaceFont"
        self.StandardFont = "StandardFont"


class Network:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Network"
        self.obj_path = "/com/deepin/daemon/Network"
        self.interface = "com.deepin.daemon.Network"

        self.VpnEnabled = 'VpnEnabled'

class Mouse:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.InputDevices"
        self.obj_path = "/com/deepin/daemon/InputDevice/Mouse"
        self.interface = "com.deepin.daemon.InputDevice.Mouse"

        self.DoubleClick = 'DoubleClick'
        self.LeftHanded = 'LeftHanded'
        self.NaturalScroll = 'NaturalScroll'
        self.DisableTpad = 'DisableTpad'
        self.MotionAcceleration = 'MotionAcceleration'

class Timedate:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Timedate"
        self.obj_path = "/com/deepin/daemon/Timedate"
        self.interface = "com.deepin.daemon.Timedate"

        self.UserTimezones = 'UserTimezones'
        self.CanNTP = 'CanNTP'
        self.LocalRTC = 'LocalRTC'
        self.NTP = 'NTP'
        self.Use24HourFormat = 'Use24HourFormat'
        self.DSTOffset = 'DSTOffset'
        self.Timezone = 'Timezone'

class Keyboard:
    def __init__(self):
        self.dbus_name  = "com.deepin.daemon.InputDevices"
        self.obj_path   = "/com/deepin/daemon/InputDevice/Keyboard"
        self.interface = "com.deepin.daemon.InputDevice.Keyboard"

        self.UserLayoutList = "UserLayoutList"
        self.CurrentLayout  = "CurrentLayout"
        self.CapslockToggle = 'CapslockToggle'
        self.RepeatDelay = 'RepeatDelay'
        self.RepeatInterval = 'RepeatInterval'

#dcc = Dde_control_center()
appearance = Appearance()
network = Network()
mouse = Mouse()
timedate = Timedate()
keyboard = Keyboard()

def getAppearanceProperty():
    appearance_obj = dbus.SessionBus().get_object(appearance.dbus_name,appearance.obj_path)
    return dbus.Interface(appearance_obj,dbus_interface=dbus.PROPERTIES_IFACE)

def getAppearanceFontSize():
    appearance_property = getAppearanceProperty()
    return appearance_property.Get(appearance.interface,appearance.FontSize)

def getAppearanceIconTheme():
    appearance_property = getAppearanceProperty()
    return appearance_property.Get(appearance.interface,appearance.IconTheme)

def getAppearanceCursorTheme():
    appearance_property = getAppearanceProperty()
    return appearance_property.Get(appearance.interface,appearance.CursorTheme)

def getNetworkVpnEnabled():
    network_session = dbus.SessionBus().get_object(network.dbus_name, network.obj_path)
    network_property = dbus.Interface(network_session, dbus_interface=dbus.PROPERTIES_IFACE)
    return network_property.Get(network.interface,network.VpnEnabled)

def getMouseProperty():
    mouse_obj = dbus.SessionBus().get_object(mouse.dbus_name,mouse.obj_path)
    return dbus.Interface(mouse_obj,dbus_interface=dbus.PROPERTIES_IFACE)

def getMouseDoubleClick():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.DoubleClick)

def getMouseLeftHanded():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.LeftHanded)

def getMouseNaturalScroll():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.NaturalScroll)

def getMouseDisableTpad():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.DisableTpad)

def getMouseMotionAcceleration():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.MotionAcceleration)

def getTimedateProperty():
    timedate_obj = dbus.SessionBus().get_object(timedate.dbus_name,timedate.obj_path)
    return dbus.Interface(timedate_obj,dbus_interface=dbus.PROPERTIES_IFACE)

def getTimedateTimezone():
    timedate_property = getTimedateProperty()
    return timedate_property.Get(timedate.interface, timedate.Timezone)

def getKeyboardProperty():
    keyboard_obj = dbus.SessionBus().get_object(keyboard.dbus_name,keyboard.obj_path)
    return dbus.Interface(keyboard_obj,dbus_interface=dbus.PROPERTIES_IFACE)

def getKeyboardCurrentLayout():
    keyboard_property = getKeyboardProperty()
    return keyboard_property.Get(keyboard.interface, keyboard.CurrentLayout)

def getKeyboardCapslockToggle():
    keyboard_property = getKeyboardProperty()
    return keyboard_property.Get(keyboard.interface, keyboard.CapslockToggle)

def getKeyboardRepeatDelay():
    keyboard_property = getKeyboardProperty()
    return keyboard_property.Get(keyboard.interface, keyboard.RepeatDelay)

def getKeyboardRepeatInterval():
    keyboard_property = getKeyboardProperty()
    return keyboard_property.Get(keyboard.interface, keyboard.RepeatInterval)

