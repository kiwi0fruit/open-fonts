@echo First install FontForge to default location in %%ProgramFiles(x86)%%
@echo Then `conda install -c defaults -c conda-forge fonttools` to the python env available from %%PATH%%
@echo Don't forget to run update_deps.bat and update FontForge before building
@pause
@cd /d "%~dp0"
@chcp 65001 > NUL
@set PYTHONIOENCODING=utf-8
@"%ProgramFiles(x86)%\FontForgeBuilds\bin\ffpython.exe" .\%~n0.py
@pause
