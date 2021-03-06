#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
import time
from lib import executeTestCase
from lib import utils
from lib import runner
from dogtail.tree import root
from dogtail import rawinput

casename = "all-441:google chrome"

class GoogleChrome(unittest.TestCase):
    caseid = '33440'
    @classmethod
    def setUpClass(cls):
        cls.chromeiconname = "Google Chrome"
        cls.ddedockobject = utils.getDdeDockObject()

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

    def testOpenRun(self):
        try:
            iconchrome = self.ddedockobject.child(self.chromeiconname)
        except:
            self.assertTrue(False, "Can't find the Google Chrome icon on the Dock")

        iconchrome.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testOpenNew(self):
        try:
            iconchrome = self.ddedockobject.child(self.chromeiconname)
        except:
            self.assertTrue(False, "Can't find the Google Chrome icon on the Dock")

        iconchrome.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testOpenHide(self):
        try:
            iconchrome = self.ddedockobject.child(self.chromeiconname)
        except:
            self.assertTrue(False, "Can't find the Google Chrome icon on the Dock")

        iconchrome.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testCloseGoogleChrome(self):
        chromewin = utils.findWindow("Google Chrome", comparetype="notequal")
        utils.closeWindow(chromewin)

        chromewin = utils.findWindow("Google Chrome", mode="nowait", comparetype="notequal")
        self.assertTrue(None == chromewin)

    def testGoogleChromeExist(self):
        chromewin = utils.findWindow("Google Chrome", comparetype="notequal")
        self.assertTrue(None != chromewin)

    def clickScreenCenter(self):
        rawinput.click(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(1)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(GoogleChrome('testOpenRun'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('testOpenNew'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('testOpenHide'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('clickScreenCenter'))

        # change display mode
        suite.addTest(GoogleChrome('testExChangeDisplayMode'))

        suite.addTest(GoogleChrome('testOpenRun'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('testOpenNew'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('testOpenHide'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('clickScreenCenter'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(GoogleChrome)
