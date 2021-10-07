@echo ofF

REM Will just call the python and HTML

.\CreateNewPlot.py

SET DATUM=%DATE:~6,4%_%DATE:~3,2%_%DATE:~0,2%
SET HTMLFILE=.\HTML\report_%DATUM%.html

echo %DATUM%
echo %HTMLFILE%

%HTMLFILE%

REM pause