@echo First install FontForge to default location in %%ProgramFiles(x86)%%
@echo Don't forget to run update_deps.bat and update FontForge before building
@pause
@chcp 65001 > NUL
@set PYTHONIOENCODING=utf-8
@"%ProgramFiles(x86)%\FontForgeBuilds\bin\ffpython.exe" .\%~n0.py
@pause
