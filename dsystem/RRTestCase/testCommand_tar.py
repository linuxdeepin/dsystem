#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput

casename = 'all-5400:备份、压缩和解压缩操作命令--验证对tar命令的支持'

class Command_tar(unittest.TestCase):
    caseid = '192188'
    @classmethod
    def setUpClass(cls):
        cls.file1    = "testsys1"
        cls.file2    = "testsys2"
        cls.alltar    = "all.tar"
        cls.alltarbz2    = "all.tar.bz2"
        cls.alltargz    = "all.tar.gz"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.file1):
            os.remove(cls.file1)

        if os.path.exists(cls.file2):
            os.remove(cls.file2)

        if os.path.exists(cls.alltar):
            os.remove(cls.alltar)

        if os.path.exists(cls.alltarbz2):
            os.remove(cls.alltarbz2)

        if os.path.exists(cls.alltargz):
            os.remove(cls.alltargz)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTarOne(self):
        os.system("touch %s" % self.file1)
        os.system("touch %s" % self.file2)
        self.assertTrue(os.path.exists(self.file1))
        self.assertTrue(os.path.exists(self.file2))

        os.system("tar -cvf %s testsys*" % self.alltar)
        self.assertTrue(os.path.exists(self.alltar))

    def testTarTwo(self):
        os.system("rm testsys*")
        self.assertFalse(os.path.exists(self.file1))
        self.assertFalse(os.path.exists(self.file2))

        os.system("tar -xvf %s" % self.alltar)
        self.assertTrue(os.path.exists(self.file1))
        self.assertTrue(os.path.exists(self.file2))

        os.system("tar -cjvf %s testsys*" % self.alltarbz2)
        self.assertTrue(os.path.exists(self.alltarbz2))

    def testTarThree(self):
        os.system("rm testsys*")
        self.assertFalse(os.path.exists(self.file1))
        self.assertFalse(os.path.exists(self.file2))

        os.system("tar -xjvf %s" % self.alltarbz2)
        self.assertTrue(os.path.exists(self.file1))
        self.assertTrue(os.path.exists(self.file2))

        os.system("tar -czvf %s testsys*" % self.alltargz)
        self.assertTrue(os.path.exists(self.alltargz))

    def testTarFour(self):
        os.system("rm testsys*")
        self.assertFalse(os.path.exists(self.file1))
        self.assertFalse(os.path.exists(self.file2))

        os.system("tar -xzvf %s" % self.alltargz)
        self.assertTrue(os.path.exists(self.file1))
        self.assertTrue(os.path.exists(self.file2))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_tar('testTarOne'))
        suite.addTest(Command_tar('testTarTwo'))
        suite.addTest(Command_tar('testTarThree'))
        suite.addTest(Command_tar('testTarFour'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_tar)
