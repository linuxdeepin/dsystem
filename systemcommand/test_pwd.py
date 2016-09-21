#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

result = True

class Pwd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '38941'
        cls.casename = 'all-1439:文件/文件夹操作命令--验证对pwd命令的支持'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPath(self):
        (status, output) = rt("cd /tmp && pwd")
        self.assertTrue(0 == status)
        self.assertEqual(output, '/tmp')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Pwd('testPath'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Pwd.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Pwd.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Pwd.MyTestResult).run(Pwd.suite())
