for /r "10_Python" %%i in (.) do @copy "Readme.md" "%%i"

::for /r "30_Javascript" %%i in (.) do echo. 2>EmptyFile.txt

::@For /D %%I In ("30_Javascript\*")Do @(For %%J In ("%%I\*.jpg")Do @Echo %%~nxJ)>"%%I\%%~nxI.txt"

::@For /D %%I In ("30_Javascript\*")Do @echo "Hello">readme.txt