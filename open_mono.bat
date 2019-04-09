@echo First install FontForge to default location in %%ProgramFiles(x86)%%
@echo Then `conda install fonttools` to the python available from %%PATH%%
@echo Don't forget to run update_deps.bat and update FontForge before building
@pause
@cd /d "%~dp0"
@where python.exe > __tmp__ && set /p python3=<__tmp__ && del __tmp__
@chcp 65001 > NUL
@set PYTHONIOENCODING=utf-8
@"%ProgramFiles(x86)%\FontForgeBuilds\bin\ffpython.exe" .\%~n0.py
@pause
