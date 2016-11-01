#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True

class Sort(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '39010'
        cls.casename = 'all-1450:文件/文件夹操作命令--验证对sort命令的支持'
        cls.homedir = os.path.expanduser('~')

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSortOne(self):
        output = getoutput('cat /etc/passwd | sort')

        line_list = output.split('\n')

        for i in range(len(line_list) - 1):
            if line_list[i].startswith('mail'):
                break

            self.assertTrue(line_list[i] < line_list[i+1], "%s and %s" % (line_list[i], line_list[i+1]))

    def testSortTwo(self):
        output = getoutput('cat /etc/passwd | sort -t \':\' -k 3 -n')

        line_list = output.split('\n')

        for i in range(len(line_list) - 1):
            up_num = int(line_list[i].split(':')[2])
            down_num = int(line_list[i+1].split(':')[2])
            self.assertTrue(up_num < down_num, "%s not little than  %s" % (up_num, down_num))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Sort('testSortOne'))
        suite.addTest(Sort('testSortTwo'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Sort.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Sort.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Sort.MyTestResult).run(Sort.suite())