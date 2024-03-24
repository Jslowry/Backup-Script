REM Extracts year, month and day from our system's date env variable

REM Pulls tokens 2, 3, and 4 from the %date% commands result and addresses them as %%a, %%b, and %%c, even if the data is split by a space or a /
for /f "tokens=2,3,4 delims=/ " %%a in ("%date%") do (
    set "dateFormat=%%a-%%b-%%c"
)

REM Copies entire file tree including empty files and excludes mp4's. Log file is truncated every run.

REM set "BackupPATH=C:\Backup"
set "BackupPATH="

set "destinationPATH=%cd%\Backup %dateFormat%"
set "logFilePATH=%cd%\LogFile"
robocopy "%oneDrivePATH%" "%destinationPATH%" /E /xf *.mp4 /log:"%logFilePATH%"

REM Runs python script that zips up the backup
REM Python script must be in same directory

python ZipBackup.py



