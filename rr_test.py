#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import gettext
import unittest
from lib import runTest

from RRTestCase import Launcher_StartAllAPP
from RRTestCase import Launcher_SendToDesktop
from RRTestCase import Launcher_AddToDock
from RRTestCase import Launcher_AutoStart
from RRTestCase import Launcher_Uninstall

from RRTestCase import Dock_Exist
from RRTestCase import Dock_DefaultSetting
from RRTestCase import Dock_ChangeDisplay
from RRTestCase import Dock_ChangePosition
from RRTestCase import Dock_ChangeIconSize
from RRTestCase import Dock_ChangeHide
from RRTestCase import Dock_DragDockiconToDel

from RRTestCase import DCC_Click_SoundSlider
from RRTestCase import DCC_Click_LightSlider
from RRTestCase import DCC_ShowModules

from RRTestCase import Command_useradd
from RRTestCase import Command_userdel
from RRTestCase import Command_passwd
from RRTestCase import Command_pwd
from RRTestCase import Command_cd
from RRTestCase import Command_mkdir
from RRTestCase import Command_rmdir
from RRTestCase import Command_cp
from RRTestCase import Command_mv
from RRTestCase import Command_rm
from RRTestCase import Command_file
from RRTestCase import Command_find
from RRTestCase import Command_grep
from RRTestCase import Command_chown
from RRTestCase import Command_sort
from RRTestCase import Command_wc

id_key = 'lava_id'
idfilename = 'id.txt'

def getIdList():
    f = open(idfilename)
    content = f.read()
    jsonstring = json.loads(content)
    return jsonstring[id_key]

def main():
    allids = getIdList()

    classes = []

    # Launcher
    if Launcher_StartAllAPP.caseid in allids:
        classes.append(Launcher_StartAllAPP)

    if Launcher_SendToDesktop.caseid in allids:
        classes.append(Launcher_SendToDesktop)

    if Launcher_AddToDock.caseid in allids:
        classes.append(Launcher_AddToDock)

    if Launcher_AutoStart.caseid in allids:
        classes.append(Launcher_AutoStart)

    if Launcher_Uninstall.caseid in allids:
        classes.append(Launcher_Uninstall)

    # Dock
    if Dock_Exist.caseid in allids:
        classes.append(Dock_Exist)

    if Dock_DefaultSetting.caseid in allids:
        classes.append(Dock_DefaultSetting)

    if Dock_ChangeDisplay.caseid in allids:
        classes.append(Dock_ChangeDisplay)

    if Dock_ChangePosition.caseid in allids:
        classes.append(Dock_ChangePosition)

    if Dock_ChangeIconSize.caseid in allids:
        classes.append(Dock_ChangeIconSize)

    if Dock_ChangeHide.caseid in allids:
        classes.append(Dock_ChangeHide)

    if Dock_DragDockiconToDel.caseid in allids:
        classes.append(Dock_DragDockiconToDel)

    # Dde control center
    if DCC_Click_SoundSlider.caseid in allids:
        classes.append(DCC_Click_SoundSlider)

    if DCC_Click_LightSlider.caseid in allids:
        classes.append(DCC_Click_LightSlider)

    if DCC_ShowModules.caseid in allids:
        classes.append(DCC_ShowModules)

    # Command
    if Command_useradd.caseid in allids:
        classes.append(Command_useradd)

    if Command_userdel.caseid in allids:
        classes.append(Command_userdel)

    if Command_passwd.caseid in allids:
        classes.append(Command_passwd)

    if Command_pwd.caseid in allids:
        classes.append(Command_pwd)

    if Command_cd.caseid in allids:
        classes.append(Command_cd)

    if Command_mkdir.caseid in allids:
        classes.append(Command_mkdir)

    if Command_rmdir.caseid in allids:
        classes.append(Command_rmdir)

    if Command_cp.caseid in allids:
        classes.append(Command_cp)

    if Command_mv.caseid in allids:
        classes.append(Command_mv)

    if Command_rm.caseid in allids:
        classes.append(Command_rm)

    if Command_file.caseid in allids:
        classes.append(Command_file)

    if Command_find.caseid in allids:
        classes.append(Command_find)

    if Command_grep.caseid in allids:
        classes.append(Command_grep)

    if Command_chown.caseid in allids:
        classes.append(Command_chown)

    if Command_sort.caseid in allids:
        classes.append(Command_sort)

    if Command_wc.caseid in allids:
        classes.append(Command_wc)

    if 0 == len(classes):
        print("classes length is 0.\nExit")
        sys.exit()

    for c in classes:
        runTest(c)

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    main()
