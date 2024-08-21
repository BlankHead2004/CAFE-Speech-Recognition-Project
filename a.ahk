#Persistent
#SingleInstance Force
SetTitleMatchMode, 2
SetTimer, KeepOnTop, 1000
Return

KeepOnTop:
  WinSet, AlwaysOnTop, On, cmd.exe
Return
