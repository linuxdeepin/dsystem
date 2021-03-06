#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
import pyautogui
from time import sleep
from lib import executeTestCase
from lib import utils
from lib import runner
from lib import Dock
from lib import window

casename = 'all-6236:回收站插件-右键'

class Dock_PluginTrashRightClick(unittest.TestCase):
    caseid = '283428'
    @classmethod
    def setUpClass(cls):
        cls.testiconname = "trash-"
        cls.dock = Dock()

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    def testPluginTrashRightClick(self):
        icon = self.dock.dockObj.child(self.testiconname)
        self.assertTrue(icon)
        icon.click(3)
        sleep(2)

        pyautogui.press('down')
        pyautogui.press('enter')
        sleep(3)

        w = window.findWindow(self.dock.string_Deepin_File_Manager)
        self.assertTrue(w != None)
        window.closeWindow(w)
        w = window.findWindow(self.dock.string_Deepin_File_Manager, mode="nowait")
        self.assertTrue(w == None)

        pyautogui.moveTo(400, 400, duration=1)
        pyautogui.click()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_PluginTrashRightClick('testPluginTrashRightClick'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Dock_PluginTrashRightClick)
