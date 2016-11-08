#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '33795'
casename = "all-509:中文字符串搜索"

class LauncherPkgNameSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.text1 = 'eog'
        cls.text2 = 'deepin-screenshot'
        cls.appName1 = '图像查看器'
        cls.appName2 = '深度截图'

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def testPkgNameSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        #apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertIn(self.appName1, apps)

    def testPkgNameSearch2(self):
        launcher.searchApp(self.text2)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName2, apps)

    def suite():
        suite = unittest.TestSuite()
        #suite.addTest(LauncherPkgNameSearch('testPkgNameSearch1'))
        suite.addTest(LauncherPkgNameSearch('testPkgNameSearch2'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherPkgNameSearch.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherPkgNameSearch.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherPkgNameSearch.MyTestResult).run(LauncherPkgNameSearch.suite())
