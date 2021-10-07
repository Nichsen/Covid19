@REM @Author: Nichsen   https://github.com/Nichsen 
@REM @Date:   2021-10-07 18:24:18
@REM @Last Modified by:   Nichsen   https://github.com/Nichsen 
@REM Modified time: 2021-10-07 18:48:06@echo ofF

REM Will just call the python and HTML an open it in defaul browser

.\CreateNewPlot.py

SET DATUM=%DATE:~6,4%_%DATE:~3,2%_%DATE:~0,2%
SET HTMLFILE=.\HTML\report_%DATUM%.html

echo %DATUM%
echo %HTMLFILE%

%HTMLFILE%

REM pause