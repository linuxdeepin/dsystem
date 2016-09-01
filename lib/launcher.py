#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import unittest
from time import sleep
from dogtail.tree import *
from lib.window import *
from lib.dde_dock import *
import pyautogui
import pexpect
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck



pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1

homePath = os.path.expanduser('~')

class Launcher:
    def __init__(self):
        self.launcherObj = root.application(appName='dde-launcher', description='/usr/bin/dde-launcher')
        #self.launcherApps = self.launcherObj.child('all',roleName='list').children
        
    def getDefaultDeepinApps(self):
        deepinApps = ['深度用户反馈', '深度终端', '深度云打印', '深度启动盘制作工具', '深度商店', '深度影院', 
                        '深度截图', '深度音乐', '日历', '文件管理器', '远程协助', '多任务视图', '显示桌面', '控制中心']
        return deepinApps

    def getShenduApps(self):
        shenduApps = ['深度用户反馈', '深度终端', '深度启动盘制作工具', '深度商店', '深度云打印', '深度截图', '深度音乐']
        return shenduApps

    def openLauncher(self):
        win = findWindow('dde-launcher')
        if win == None:
            pyautogui.press('winleft')

    def getIconCoorFree(self,icon):
        coor = []
        position = self.launcherObj.child(icon).position
        size = self.launcherObj.child(icon).size
        coor.append(position[0]+size[0]/2)
        coor.append(position[1]+size[1]/2)
        return coor

    def getIconCoorCategory(self,lst):
        coor = []
        position = self.launcherObj.child(lst,roleName='list').children[0].position
        size = self.launcherObj.child(lst,roleName='list').children[0].size
        coor.append(position[0]+size[0]/2)
        coor.append(position[1]+size[1]/2)
        return coor

    def getKidsCategory(self,lst):
        kids = []
        apps = self.launcherObj.child(lst,roleName='list').children
        for i in range(len(apps)):
            kids.append(apps[i].name)
        return kids

    def getLauncherAllApps(self):
        apps = []
        for i in range(len(self.launcherObj.child('all',roleName='list').children)):
            apps.append(self.launcherObj.child('all',roleName='list').children[i].name)
        return apps

    def getAppSize(self,app):
        return self.launcherObj.child(app).size

    def getAppCenterCoor(self,app):
        size = self.getAppSize(app)
        position = self.launcherObj.child(app).position
        x = position[0]+size[0]/2
        y = position[1]+size[1]/2
        return x,y

    def getAppCenterCoorCategory(self,lst,index):
        kids = self.launcherObj.child(lst,roleName='list').children
        kid = kids[index]
        position = kid.position
        size = kid.size
        x = position[0]+size[0]/2
        y = position[1]+size[1]/2
        return x,y

    def dragAppToDockFree(self):
        self.freeMode()
        app = Dock().getLastItemName()
        app_coor = Dock().getAppCoor(app)
        pyautogui.press('winleft')
        launcher = findWindow('dde-launcher')
        if launcher != None:
            icon_coor = self.getIconCoorFree('QQ')
            pyautogui.mouseDown(icon_coor[0], icon_coor[1])
            pyautogui.moveTo(app_coor[0]-1, app_coor[1]-1, duration=2, pause=1)
            pyautogui.mouseUp(app_coor[0], app_coor[1], duration=1)
            self.exitLauncher()

    def dragAppToDockCategory(self,listName):
        self.categoryMode()
        app = Dock().getLastItemName()
        app_coor = Dock().getAppCoor(app)
        pyautogui.press('winleft')
        launcher = findWindow('dde-launcher')
        if launcher != None:
            QQName = self.launcherObj.child(listName,roleName='list').children[0].name
            icon_coor = self.getIconCoorCategory('chat')
            pyautogui.mouseDown(icon_coor[0], icon_coor[1], duration=2, pause=1)
            pyautogui.moveTo(app_coor[0], app_coor[1], duration=2, pause=1)
            pyautogui.mouseUp(app_coor[0], app_coor[1], duration=0.5)
            self.exitLauncher()

    def unDock(self):
        app_coor = Dock().getAppCoor('QQ')
        center_coor = pyautogui.size()
        pyautogui.mouseDown(app_coor[0], app_coor[1])
        pyautogui.dragTo(center_coor[0]/2, center_coor[1]/2, duration=2)

    def exitLauncher(self):
        launcher = findWindow('dde-launcher')
        if launcher != None:
            pyautogui.press('esc')

    def getLauncherMode(self):
        mode = subprocess.check_output(["gsettings get com.deepin.dde.launcher display-mode"],shell=True).decode().split("\n")
        mode = [ n for n in mode if len(n.strip()) > 0]
        mode = ''.join(mode)
        return mode

    def freeMode(self):
        mode = self.getLauncherMode()
        win = findWindow('dde-launcher')
        if mode == '\'category\'' and win == None:
            pyautogui.press('winleft')
            launcher = findWindow('dde-launcher')
            if launcher != None:
                self.launcherObj.child('mode-toggle-button').click()
                self.exitLauncher()
        elif mode == '\'category\'' and win != None:
            self.launcherObj.child('mode-toggle-button').click()
        else:
            self.exitLauncher()

    def categoryMode(self):
        mode = self.getLauncherMode()
        win = findWindow('dde-launcher')
        if mode == '\'free\'' and win == None:
            pyautogui.press('winleft')
            launcher = findWindow('dde-launcher')
            if launcher != None:
                self.launcherObj.child('mode-toggle-button').click()
                self.exitLauncher()

    def dragSrcToDest(self, s, d, btn='left'):
        pyautogui.press('winleft')
        launcher = findWindow('dde-launcher')
        if launcher != None:
            apps = self.getLauncherAllApps()
            src = apps[s]
            dest = apps[d]
            src_size = self.getAppSize(src)
            dest_size = self.getAppSize(dest)
            src_position = self.launcherObj.child(src).position
            dest_position = self.launcherObj.child(dest).position
            src_x = src_position[0]+src_size[0]/2
            src_y = src_position[1]+src_size[1]/2
            dest_x = dest_position[0]+dest_size[0]/2
            dest_y = dest_position[1]+dest_size[1]/2
            if src_y<0:
                pyautogui.scroll(30)
            pyautogui.mouseDown(src_x, src_y, button=btn)
            if d>27:
                pyautogui.scroll(-30)
                pyautogui.dragTo(dest_x, dest_y, duration=6, button=btn)
            pyautogui.dragTo(dest_x, dest_y, duration=2, button=btn)

    def dragToCenterLeftKey(self):
        self.dragSrcToDest(0, 17)
        self.exitLauncher()

    def dragToFirstLeftKey(self):
        self.dragSrcToDest(17, 0)
        self.exitLauncher()

    def dragToCenterRightKey(self):
        self.dragSrcToDest(0, 17, 'right')

    def dragToSecond(self):
        self.dragSrcToDest(0, 1)
        self.exitLauncher()

    def dragToFirstRowEnd(self):
        self.dragSrcToDest(0, 6)
        self.exitLauncher()

    def dragToFirstColumnEnd(self):
        columnEndIndex = self.getColumnEndIndex()
        self.dragSrcToDest(0, columnEndIndex)
        self.exitLauncher()

    def dragToEnd(self):
        endIndex = len(self.launcherObj.child('all',roleName='list').children)
        self.dragSrcToDest(0, endIndex-1)
        self.exitLauncher()

    def getColumnEndIndex(self):
        nums = len(self.launcherObj.child('all',roleName='list').children)
        left = nums%7
        clumns = nums/7
        if left !=0:
            return clumns*7
        else:
            return (clumns-1)*7

    def disableDrag(self):
        self.categoryMode()
        win = findWindow('dde-launcher')
        if win == None:
            pyautogui.press('winleft')
            googleCoor = self.getIconCoorCategory('internet')
            musicCoor = self.getIconCoorCategory('music')
            pyautogui.mouseDown(googleCoor)
            pyautogui.dragTo(musicCoor, duration=2)
            self.exitLauncher()

    def menuDesktop(self,app):
        win = findWindow('dde-launcher')
        if win == None:
            pyautogui.press('winleft')
            self.launcherObj.child(app).click(3)
        menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')  
        if menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')
        else:
            raise Exception('Launcher Menu did not opened!')

    def menuDock(self,app):
        dockApps = Dock().getAllDockApps()
        if app in dockApps:
            appCoor = Dock().getAppCoor(app)
            screen = pyautogui.size()
            screen_center = (screen[0]/2,screen[1]/2)
            pyautogui.mouseDown(appCoor)
            pyautogui.dragTo(screen_center, duration=2)
        win = findWindow('dde-launcher')
        if win == None:
            pyautogui.press('winleft')
            self.launcherObj.child(app).click(3)
        menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        if menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')
        else:
            raise Exception('Launcher Menu did not opened!')

    def menuUnDock(self,app):
        win = findWindow('dde-launcher')
        if win == None:
            pyautogui.press('winleft')
            self.launcherObj.child(app).click(3)
        menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        if menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')
        else:
            raise Exception('Launcher Menu did not opened!')

    def menuBoot(self,arg,*args):
        win = findWindow('dde-launcher')
        if win == None:
            pyautogui.press('winleft')
            self.launcherObj.child(arg).click(3)
            try:

                menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
            except:
                assertEqual(len(menuObj.children),0,'Launcher Menu did not opened!')
            else:
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('enter')
            if args:
                for app in args: 
                    self.launcherObj.child(app).click(3)
                    try:

                        menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
                    except:
                        assertEqual(len(menuObj.children),0,'Launcher Menu did not opened!')
                    else:
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('down')
                        pyautogui.press('enter')

    def installApp(self,app):
        #pyautogui.press('winleft')
        #self.launcherObj.child('深度终端').click()
        #sleep(5)
        #winName = getWindowName()
        #if winName == '深度终端':

        passwd = 'a'
        try:

            c = pexpect.spawnu('sudo apt-get -y install ' + app)
            c.expect('sudo', timeout=10)
            c.sendline(passwd+'\n')
            c.expect('$', timeout=300)
            c.interact()
        except Exception as e:
            print (str(c))
            print (e)

    def removeApp(self,app):
        #pyautogui.press('winleft')
        #self.launcherObj.child('深度终端').click()
        #sleep(5)
        #winName = getWindowName()
        #if winName == '深度终端':

        passwd = 'a'
        try:

            c = pexpect.spawnu('sudo apt-get -y remove ' + app)
            c.expect('sudo', timeout=10)
            c.sendline(passwd+'\n')
            c.expect('$', timeout=300)
            c.interact()
        except Exception as e:
            print (str(c))
            print (e)

    def checkLableKids(self,label):
        pyautogui.press('winleft')
        mode = self.getLauncherMode()
        if mode == '\'free\'':
            self.launcherObj.child('mode-toggle-button').click()
        self.launcherObj.child(label).click()

    def searchApp(self,char):
        pyautogui.press('winleft')
        self.launcherObj.child('search-edit').text = char

    def pasteMsgInLauncher(self,msg):
        pyautogui.press('winleft')
        if findWindow('dde-launcher') != None:
            pasteMsgWithKey()
        else:
            raise Exception('Launcher did not opened!')


    

launcher = Launcher()

def copyMsg(msg):
    pyperclip.copy(msg)

def pasteMsg(msg):
    pyperclip.paste(msg)

def pasteMsgWithKey():
    pyautogui.hotkey('ctrl','v')

def getAllWindows():
    try:
        wins = []
        screen = Wnck.Screen.get_default()
        screen.force_update()
        for win in screen.get_windows():
            wins.append(win)
        return wins
    finally:
        win = None
        screen = None
        Wnck.shutdown()

def getWindowName():
    sleep(2)
    try:
        screen = Wnck.Screen.get_default()
        screen.force_update()
        window = screen.get_active_window()
        return window.get_name()
    finally:
        window = None
        screen = None
        Wnck.shutdown()

def getDesktopFiles():
    desktopPath = homePath + '/桌面'
    desktopFile = subprocess.check_output(["ls " + desktopPath],shell=True).decode().split("\n")
    files = [ n for n in desktopFile if len(n.strip()) > 0]
    return files

def getBootFeild(fileName):
    filePath = homePath + '/.config/autostart/' + fileName
    bootFeild = subprocess.check_output(["cat " + filePath + " |grep Hidden"],shell=True).decode().split("\n")
    feild = [ n for n in bootFeild if len(n.strip()) > 0]
    feild = ''.join(feild)
    return feild

