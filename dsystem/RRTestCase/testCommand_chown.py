#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

casename = 'all-5388:文件/文件夹操作命令--验证对chown命令的支持'

class Command_chown(unittest.TestCase):
    caseid = '192131'
    @classmethod
    def setUpClass(cls):
        cls.loginuser = getpass.getuser()

        if not os.path.exists('/home/user'):
            (status, output) = rt('sudo useradd -m user')

        if os.path.exists('/tmp/testdir'):
            (status, output) = rt('sudo rm -rf /tmp/testdir')

        if os.path.exists('/tmp/testfile'):
            (status, output) = rt('sudo rm /tmp/testfile')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('/tmp/testdir'):
            (status, output) = rt('sudo rm -rf /tmp/testdir')

        if os.path.exists('/tmp/testfile'):
            (status, output) = rt('sudo rm /tmp/testfile')

        if os.path.exists('/home/user'):
            (status, output) = rt('sudo deluser --remove-home user')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChownFile(self):
        self.assertTrue(os.path.exists('/home/user'))
        (status, output) = rt('touch /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/tmp/testfile'))

        (status, output) = rt('ls -l /tmp/testfile')
        d_list = output.split()
        d_user = d_list[2]
        d_group = d_list[3]
        self.assertTrue(self.loginuser == d_user)
        self.assertTrue(self.loginuser == d_group)

        (status, output) = rt('sudo chown user.user /tmp/testfile')
        (status, output) = rt('ls -l /tmp/testfile')
        t_list = output.split()
        t_user = t_list[2]
        t_group = t_list[3]
        self.assertFalse(self.loginuser == t_user)
        self.assertFalse(self.loginuser == t_group)
        self.assertTrue('user' == t_user)
        self.assertTrue('user' == t_group)

    def testChownDir(self):
        self.assertTrue(os.path.exists('/home/user'))
        (status, output) = rt('mkdir /tmp/testdir')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/tmp/testdir'))
        (status, output) = rt('touch /tmp/testdir/test')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/tmp/testdir/test'))

        (status, output) = rt('ls -l /tmp/testdir/test')
        d_list = output.split()
        d_user = d_list[2]
        d_group = d_list[3]
        self.assertTrue(self.loginuser == d_user)
        self.assertTrue(self.loginuser == d_group)

        (status, output) = rt('sudo chown -R user.user /tmp/testdir')
        (status, output) = rt('ls -l /tmp/testdir/test')
        t_list = output.split()
        t_user = t_list[2]
        t_group = t_list[3]
        self.assertFalse(self.loginuser == t_user)
        self.assertFalse(self.loginuser == t_group)
        self.assertTrue('user' == t_user)
        self.assertTrue('user' == t_group)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_chown('testChownFile'))
        suite.addTest(Command_chown('testChownDir'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_chown)
