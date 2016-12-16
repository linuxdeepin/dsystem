#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import utils
from lib import runner

result = True
casename = "all-2493:高效模式大图标显示"

class EfficientDockSize(unittest.TestCase):
    caseid = '68490'
    @classmethod
    def setUpClass(cls):
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()

        if utils.dock.displaymode_efficient != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        if utils.getDdeDockDisplayMode() != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(cls.defaultdisplaymode)

        if utils.getDdeDockPosition() != cls.defaultposition:
            utils.setDdeDockPosition(cls.defaultposition)

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
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_large)

    def testChangeIconSizeToMedium(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_medium)

    def testChangeIconSizeToSmall(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(EfficientDockSize('testIconSize'))
        suite.addTest(EfficientDockSize('testChangeIconSizeToLarge'))
        suite.addTest(EfficientDockSize('testIconSize'))
        suite.addTest(EfficientDockSize('testChangeIconSizeToMedium'))
        suite.addTest(EfficientDockSize('testIconSize'))
        suite.addTest(EfficientDockSize('testChangeIconSizeToSmall'))
        suite.addTest(EfficientDockSize('testIconSize'))
        suite.addTest(EfficientDockSize('testChangeIconSizeToMedium'))
        suite.addTest(EfficientDockSize('testIconSize'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(EfficientDockSize)
