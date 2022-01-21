' VBScript to created shortcut
Const strProgramTitle = "DeepMeed"

Dim FSO
Set fso = CreateObject("Scripting.FileSystemObject")
CurrentDirectory = FSO.GetAbsolutePathName(".")
strProgram =  fso.BuildPath(CurrentDirectory, "DeepMed.bat")
strWorkDir = CurrentDirectory
Dim objShortcut, objShell
Set objShell = WScript.CreateObject ("Wscript.Shell")
strLPath = objShell.SpecialFolders ("Desktop")
Set objShortcut = objShell.CreateShortcut (strLPath & "\" & strProgramTitle & ".lnk")
objShortcut.TargetPath = strProgram
objShortcut.WorkingDirectory = strWorkDir
objShortcut.Description = strProgramTitle
objShortcut.IconLocation = fso.BuildPath(CurrentDirectory, "icons\icon.ico, 0")
objShortcut.Save
WScript.Quit

