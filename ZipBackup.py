from datetime import datetime
import shutil, os

# Gets current date and formats it to MM-DD-YYYY
current_date = datetime.today()
formatted_date = current_date.strftime("%m-%d-%Y")

# Filename with current date
fileName = f'Bulldog Backup {formatted_date}'

# Path to Backup Folder
file2zip = os.path.join(os.getcwd(), f"Bulldog Backup {formatted_date}")

# Path to Log File
logFile = os.path.join(os.getcwd(), "LogFile")

# Checks if file2zip actually exists, if u dont check it'll just make a zip named fileName without data
if os.path.exists(file2zip):
    try:
        # If archive fails it will write to the log and will not delete the backup folder
        shutil.make_archive(fileName, 'zip', file2zip)
        shutil.rmtree(file2zip)
    except FileNotFoundError as e:
        with open(logFile, 'a') as f:
            f.write(f"\nError zipping backup: {e}\n")
    except Exception as e:
        with open(logFile, 'a') as f:
            f.write("\nError\n")
else:
    with open(logFile, 'a') as f:
        f.write("\nBackup folder doesn't exist\n")