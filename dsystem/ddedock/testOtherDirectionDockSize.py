#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib import executeTestCase
from lib import utils
from lib import runner

casename = "all-2496:大图标在四个方向上显示"

class OtherDirectionDockSize(unittest.TestCase):
    caseid = '68501'
    @classmethod
    def setUpClass(cls):
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        cls.defaulticonsize = utils.getDdeDockIconSize()

    @classmethod
    def tearDownClass(cls):
        if utils.getDdeDockDisplayMode() != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(cls.defaultdisplaymode)

        if utils.getDdeDockPosition() != cls.defaultposition:
            utils.setDdeDockPosition(cls.defaultposition)

        if utils.getDdeDockIconSize() != cls.defaulticonsize:
            utils.setDdeDockIconSize(cls.defaulticonsize)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIconSize(self):
        launcher = self.ddedockobject.child("Launcher")
        dbus_iconsize = utils.getDdeDockIconSize()
        displaymode = utils.getDdeDockDisplayMode()
        calculate_iconsize_y = 0
        calculate_iconsize_x = 0
        if utils.dock.displaymode_fashion == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.5)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.1)
        elif utils.dock.displaymode_efficient == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.2)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.4)

        self.assertTrue(abs(calculate_iconsize_x - launcher.size[0]) < 3)
        self.assertTrue(abs(calculate_iconsize_y - launcher.size[1]) < 3)

    def testChangeIconSizeToLarge(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.right_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def testChangePosition(self):
        if utils.getDdeDockPosition() == utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_top)
        elif utils.getDdeDockPosition() == utils.dock.position_top:
            utils.setDdeDockPosition(utils.dock.position_right)
        elif utils.getDdeDockPosition() == utils.dock.position_right:
            utils.setDdeDockPosition(utils.dock.position_left)

    def testCheckDockSizeTop(self):
        launcher = self.ddedockobject.child("Launcher")
        main_window = self.ddedockobject.child("dock-mainwindow")
        dbus_iconsize = utils.getDdeDockIconSize()
        displaymode = utils.getDdeDockDisplayMode()
        calculate_iconsize_y = 0
        calculate_iconsize_x = 0
        if utils.dock.displaymode_fashion == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.5)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.1)
        elif utils.dock.displaymode_efficient == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.2)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.4)

        self.assertEquals((calculate_iconsize_x, calculate_iconsize_y),
                          launcher.size)
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)
        self.assertTrue(main_window.position[1] == 0)

    def testCheckDockSizeRight(self):
        launcher = self.ddedockobject.child("Launcher")
        main_window = self.ddedockobject.child("dock-mainwindow")
        dbus_iconsize = utils.getDdeDockIconSize()
        displaymode = utils.getDdeDockDisplayMode()
        calculate_iconsize_y = 0
        calculate_iconsize_x = 0
        if utils.dock.displaymode_fashion == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.5)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.1)
        elif utils.dock.displaymode_efficient == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.2)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.4)

        self.assertEquals((calculate_iconsize_x, calculate_iconsize_y),
                          launcher.size)
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)
        self.assertTrue(main_window.position[0] == (utils.resolution.width - main_window.size[0]))

    def testCheckDockSizeLeft(self):
        launcher = self.ddedockobject.child("Launcher")
        main_window = self.ddedockobject.child("dock-mainwindow")
        dbus_iconsize = utils.getDdeDockIconSize()
        displaymode = utils.getDdeDockDisplayMode()
        calculate_iconsize_y = 0
        calculate_iconsize_x = 0
        if utils.dock.displaymode_fashion == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.5)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.1)
        elif utils.dock.displaymode_efficient == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.2)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.4)

        self.assertEquals((calculate_iconsize_x, calculate_iconsize_y),
                          launcher.size)
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)
        self.assertTrue(main_window.position[0] == 0)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(OtherDirectionDockSize('testIconSize'))
        suite.addTest(OtherDirectionDockSize('testChangeIconSizeToLarge'))
        suite.addTest(OtherDirectionDockSize('testChangePosition'))
        suite.addTest(OtherDirectionDockSize('testCheckDockSizeTop'))
        suite.addTest(OtherDirectionDockSize('testExChangeDisplayMode'))
        suite.addTest(OtherDirectionDockSize('testCheckDockSizeTop'))
        suite.addTest(OtherDirectionDockSize('testChangePosition'))
        suite.addTest(OtherDirectionDockSize('testCheckDockSizeRight'))
        suite.addTest(OtherDirectionDockSize('testExChangeDisplayMode'))
        suite.addTest(OtherDirectionDockSize('testCheckDockSizeRight'))
        suite.addTest(OtherDirectionDockSize('testChangePosition'))
        suite.addTest(OtherDirectionDockSize('testCheckDockSizeLeft'))
        suite.addTest(OtherDirectionDockSize('testExChangeDisplayMode'))
        suite.addTest(OtherDirectionDockSize('testCheckDockSizeLeft'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(OtherDirectionDockSize)
