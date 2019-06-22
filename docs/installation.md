---
layout: default
title: Installation
nav_order: 3
---

# Installation

Dwarf vs your first target
{: .fs-6 .fw-300 }

---

### Pre requisites
A frida server running anywhere.

#### Android Session:
  + make sure you can use 'adb' command in console or [Read here](https://www.xda-developers.com/adb-fastboot-any-directory-windows-linux/)
  + root on the device/emulator is required!
  + make sure frida is in /system/bin|xbin with a+x permissions or eventually use Dwarf to automatically install latest frida server 

### Setup and run

```
git clone https://github.com/iGio90/Dwarf

cd Dwarf

pip3 install -r requirements.txt

python3 dwarf.py
```

### Optionally

You can install keystone-engine to enable assembler:

```
Windows
x86: https://github.com/keystone-engine/keystone/releases/download/0.9.1/keystone-0.9.1-python-win32.msi
x64: https://github.com/keystone-engine/keystone/releases/download/0.9.1/keystone-0.9.1-python-win64.msi

OSX / Unix
pip3 install keystone-engine
```

dex2jar tools (required for baksmali/decompiling)
```
Guide: https://sourceforge.net/p/dex2jar/wiki/UserGuide/
Files: https://github.com/pxb1988/dex2jar/releases

On Windows add d2j folder to %PATH% and change:
'java -Xms512m -Xmx1024m -cp "%CP%" %*'
in d2j_invoke.bat to
'java -Xms512m -Xmx4096m -cp "%CP%" %*'
```

### Settings
You can change in .dwarf
```
"dwarf_ui_hexedit_bpl": 32 (default: 16) - Bytes per line in hexview
"dwarf_ui_hexstyle": "upper", "lower" (default: "upper") - overall hexstyle 0xabcdef or 0xABCDEF (note: click on the "Offset (X)" in hexview to change)
"dwarf_ui_font_size": 12 (default: 12) - (note: hexview/disasm use other font wait for settingsdlg or change lib/utils.py get_os_monospace_font())
```

