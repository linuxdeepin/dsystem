__ALL__ = ['Launcher_StartAllAPP',
           'Launcher_Start',
           'Launcher_SendToDesktop',
           'Launcher_AddToDock',
           'Launcher_AutoStart',
           'Launcher_Uninstall',
           'Dock_Exist',
           'Dock_FashionIconsPopup',
           'Dock_EfficientIconsPopup',
           'Dock_DefaultSetting',
           'Dock_ChangeDisplay',
           'Dock_ChangePosition',
           'Dock_ChangeIconSize',
           'Dock_ChangeHide',
           'Dock_DragDockiconToDel',
           'Dock_AutoDisplay',
           'Dock_IconDocked',
           'Dock_IconMenuDock',
           'Dock_Uninstall',
           'Dock_IconMenuForceQuit',
           'Dock_IconMenuMultiClose',
           'Dock_PluginShutDownLeftClick',
           'Dock_PluginNetworkLeftClick',
           'Dock_PluginSoundLeftClick',
           'Dock_PluginDatetimeLeftClick',
           'Dock_PluginTrashLeftClick',
           'Dock_PluginShutDownRightClick',
           'Dock_PluginNetworkRightClick',
           'Dock_PluginSoundRightClick',
           'Dock_PluginDatetimeRightClick',
           'Dock_PluginTrashRightClick',
           'DCC_Click_LightSlider',
           'DCC_Click_SoundSlider',
           'DCC_ShowModules',
           'Command_useradd',
           'Command_userdel',
           'Command_passwd',
           'Command_pwd',
           'Command_cd',
           'Command_mkdir',
           'Command_rmdir',
           'Command_cp',
           'Command_mv',
           'Command_rm',
           'Command_file',
           'Command_find',
           'Command_grep',
           'Command_chown',
           'Command_sort',
           'Command_wc',
           'Command_ifconfig',
           'Command_ping',
           'Command_ping_ip',
           'Command_ping_local_ip',
           'Command_netstat_i',
           'Command_netstat_r',
           'Command_telnet',
           'Command_traceroute',
           'Command_tar',
           'Command_gzip',
           'Command_gunzip',
           'Command_kill',
           'Command_ps',
           'Command_vi',
           'DFM_OpenFile',
           'DFM_OpenFileByApp',
           'DFM_CompressFiles',
           'DFM_DecompressFile',
           'DFM_DecompressFileHere',
           'DFM_RenameFile',
           'DFM_DeleteFiles',
           'DFM_MoveToTrash',
           'DFM_RestoreFromTrash',
           'DFM_PasteFile',
           'DFM_NewFolder',
           'DFM_NewFile',
           'DFM_OpenFileLocation',
           'DFM_CreateSymlink',
           'DFM_FileShare',
           'DFM_OpenInTerminal',
           'DFM_OpenNewWindow',

           'DeepinMovie'
           ]

from .testLauncher_StartAllAPP import Launcher_StartAllAPP
from .testLauncher_Start import Launcher_Start
from .testLauncher_SendToDesktop import Launcher_SendToDesktop
from .testLauncher_AddToDock import Launcher_AddToDock
from .testLauncher_AutoStart import Launcher_AutoStart
from .testLauncher_Uninstall import Launcher_Uninstall

from .testDock_Exist import Dock_Exist
from .testDock_FashionIconsPopup import Dock_FashionIconsPopup
from .testDock_EfficientIconsPopup import Dock_EfficientIconsPopup
from .testDock_DefaultSetting import Dock_DefaultSetting
from .testDock_ChangeDisplay import Dock_ChangeDisplay
from .testDock_ChangePosition import Dock_ChangePosition
from .testDock_ChangeIconSize import Dock_ChangeIconSize
from .testDock_ChangeHide import Dock_ChangeHide
from .testDock_DragDockiconToDel import Dock_DragDockiconToDel
from .testDock_AutoDisplay import Dock_AutoDisplay
from .testDock_IconDocked import Dock_IconDocked
from .testDock_IconMenuDock import Dock_IconMenuDock
from .testDock_Uninstall import Dock_Uninstall
from .testDock_PluginShutDownLeftClick import Dock_PluginShutDownLeftClick
from .testDock_PluginNetworkLeftClick import Dock_PluginNetworkLeftClick
from .testDock_PluginSoundLeftClick import Dock_PluginSoundLeftClick
from .testDock_PluginDatetimeLeftClick import Dock_PluginDatetimeLeftClick
from .testDock_PluginTrashLeftClick import Dock_PluginTrashLeftClick
from .testDock_PluginShutDownRightClick import Dock_PluginShutDownRightClick
from .testDock_PluginNetworkRightClick import Dock_PluginNetworkRightClick
from .testDock_PluginSoundRightClick import Dock_PluginSoundRightClick
from .testDock_PluginDatetimeRightClick import Dock_PluginDatetimeRightClick
from .testDock_PluginTrashRightClick import Dock_PluginTrashRightClick
from .testDock_IconMenuForceQuit import Dock_IconMenuForceQuit
from .testDock_IconMenuMultiClose import Dock_IconMenuMultiClose

from .testDCC_ClickLightslider  import DCC_Click_LightSlider
from .testDCC_ClickSoundslider  import DCC_Click_SoundSlider
from .testDCC_ShowAllModules  import DCC_ShowModules

from .testCommand_useradd import Command_useradd
from .testCommand_userdel import Command_userdel
from .testCommand_passwd import Command_passwd
from .testCommand_pwd import Command_pwd
from .testCommand_cd import Command_cd
from .testCommand_mkdir import Command_mkdir
from .testCommand_rmdir import Command_rmdir
from .testCommand_cp import Command_cp
from .testCommand_mv import Command_mv
from .testCommand_rm import Command_rm
from .testCommand_file import Command_file
from .testCommand_find import Command_find
from .testCommand_grep import Command_grep
from .testCommand_chown import Command_chown
from .testCommand_sort import Command_sort
from .testCommand_wc import Command_wc
from .testCommand_ifconfig import Command_ifconfig
from .testCommand_ping import Command_ping
from .testCommand_ping_ip import Command_ping_ip
from .testCommand_ping_local_ip import Command_ping_local_ip
from .testCommand_netstat_i import Command_netstat_i
from .testCommand_netstat_r import Command_netstat_r
from .testCommand_telnet import Command_telnet
from .testCommand_traceroute import Command_traceroute
from .testCommand_tar import Command_tar
from .testCommand_gzip import Command_gzip
from .testCommand_gunzip import Command_gunzip
from .testCommand_kill import Command_kill
from .testCommand_ps import Command_ps
from .testCommand_vi import Command_vi
from .testCommand_man import Command_man
from .testCommand_who import Command_who
from .testCommand_whoami import Command_whoami
from .testCommand_cal import Command_cal
from .testCommand_date import Command_date
from .testCommand_more import Command_more
from .testCommand_redirect import Command_redirect
from .testCommand_pipe import Command_pipe
from .testCommand_apt_get import Command_apt_get
from .testCommand_apt_cache import Command_apt_cache


from .testDFM_OpenFile import DFM_OpenFile
from .testDFM_OpenFileByApp import DFM_OpenFileByApp
from .testDFM_CompressFiles import DFM_CompressFiles
from .testDFM_DecompressFile import DFM_DecompressFile
from .testDFM_DecompressFileHere import DFM_DecompressFileHere

from .testDFM_RenameFile import DFM_RenameFile
from .testDFM_DeleteFiles import DFM_DeleteFiles
from .testDFM_MoveToTrash import DFM_MoveToTrash
from .testDFM_RestoreFromTrash import DFM_RestoreFromTrash
from .testDFM_PasteFile import DFM_PasteFile

from .testDFM_NewFolder import DFM_NewFolder
from .testDFM_NewFile import DFM_NewFile
from .testDFM_OpenFileLocation import DFM_OpenFileLocation
from .testDFM_CreateSymlink import DFM_CreateSymlink
from .testDFM_FileShare import DFM_FileShare

from .testDFM_OpenInTerminal import DFM_OpenInTerminal
from .testDFM_OpenNewWindow import DFM_OpenNewWindow

from .testDeepinMovie import DeepinMovie
