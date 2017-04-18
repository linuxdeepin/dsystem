#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center
from lib import LangSelector
from subprocess import getstatusoutput as rt

LANGUAGELIST = ['am_ET',
                'ast_ES.UTF-8',
                'cs_CZ.UTF-8',
                'da_DK.UTF-8',
                'de_DE.UTF-8',
                'es_ES.UTF-8',
                'fr_FR.UTF-8',
                'gl_ES.UTF-8',
                'hr_HR.UTF-8',
                'hu_HU.UTF-8',
                'it_IT.UTF-8',
                'lt_LT.UTF-8',
                'ms_MY.UTF-8',
                'nb_NO.UTF-8',
                'nl_NL.UTF-8',
                'pl_PL.UTF-8',
                'pt_PT.UTF-8',
                'pt_BR.UTF-8',
                'ru_RU.UTF-8',
                'sk_SK.UTF-8',
                'sl_SI.UTF-8',
                'tr_TR.UTF-8',
                'zh_CN.UTF-8',
                'zh_TW.UTF-8']

class TestLanguage(unittest.TestCase):
    caseid = '999999'

    @classmethod
    def setUpClass(cls):
        cls.old_LANG = os.getenv("LANG")
        cls.old_LANGUAGE = os.getenv("LANGUAGE")
        cls.dbus_langselector = LangSelector()

    @classmethod
    def tearDownClass(cls):
        os.putenv("LANG", cls.old_LANG)
        os.putenv("LANGUAGE", cls.old_LANGUAGE)

    def testAllLanguade(self):
        times = 10

        while True:
            try:
                langlist = self.dbus_langselector.GetLocaleList()
                break
            except:
                print("try to get langlist again...")
                times -= times

                if times:
                    continue

                self.assertTrue(False, "Can't get langlist")

        langs = []
        for k, v in langlist:
            print(k)
            langs.append(k)

        for lang in LANGUAGELIST:
            self.assertTrue(lang in langs)

        for lang in LANGUAGELIST:
            os.putenv("LANG", lang)
            os.putenv("LANGUAGE", lang.split(".")[0])
            time.sleep(1)
            (status, output) = rt("./testLanguage")
            print(output)
            self.assertTrue(1 == status, "Test language %s failed." % lang)
            time.sleep(2)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestLanguage('testAllLanguade'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(TestLanguage)
