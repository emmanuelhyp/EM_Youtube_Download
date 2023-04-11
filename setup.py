from cx_Freeze import setup, Executable
import os
import sys
import os.path



import sys
import os
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['Tk_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')

from cx_Freeze import setup, Executable
import cx_Freeze.hooks

build_exe_options = {"packages": ['os','sys'],
                     "includes":['PyQt5','pafy','humanize','urllib'],
                    }


executables = [
    Executable('d_mano.py', targetName='MANAPP.exe',base = 'Win32GUI',)
]

setup(name='Man App',
      version='1.0',
      description='download video and any file',
      executables=executables,
      options={"build_exe":build_exe_options},
      )
