#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
caseid = '69087'
casename = 'all-2614:apt-cache命令'

class Apt_cache(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        pass

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApt_cache(self):
        (status, output) = rt('apt-cache policy dde')
        self.assertTrue(0 == status, "Error: %s" % output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Apt_cache('testApt_cache'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Apt_cache.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Apt_cache.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Apt_cache.MyTestResult).run(Apt_cache.suite())
