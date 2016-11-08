#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import runner
from lib import utils

result = True
caseid = '39116'
casename = 'all-1469:其他命令--验证对重定向的支持'

class Redirect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        os.system('touch /tmp/testfile')

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

        os.system('rm /tmp/testfile')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRedirect(self):
        (status, output) = rt('echo bbbb > /tmp/testfile')
        (status, output) = rt('more /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('bbbb' == output)

        (status, output) = rt('echo aaaa >> /tmp/testfile')
        (status, output) = rt('more /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('bbbb\naaaa' == output)

        (status, output) = rt('date -s aa > /tmp/testfile 2>&1')
        (status, output) = rt('cat /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('date: 无效的日期"aa"' == output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Redirect('testRedirect'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Redirect.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Redirect.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Redirect.MyTestResult).run(Redirect.suite())
