chcp 65001 > NUL
set PYTHONIOENCODING=utf-8

"%ProgramFiles(x86)%\FontForgeBuilds\bin\ffpython.exe" libertinus.py

::# Python 3 debug
::call prepare
::# 'prepare.bat' contains:
::# set PYTHONPATH=%UserProfile%\Miniconda3
::# set PythonEnv=the_environment
::set PATH=%PYTHONPATH%;%PYTHONPATH%\Scripts;%PYTHONPATH%\Library\bin;%PATH%
::call activate %PythonEnv%
::python libert_serif.py

pause
