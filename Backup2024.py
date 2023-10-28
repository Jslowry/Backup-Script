import shutil
import os
from datetime import datetime, timedelta

todays_date = datetime.today().strftime('%m-%d-%Y')

current_dir = os.getcwd()
source = rf"C:\Users\FSAE\OneDrive - Mississippi State University\Documents - MSSTATE Formula SAE (UserCreated)\Mississippi State FSAE\FSAE 2024"
backupName = f'Bulldog Backup 2024 {todays_date}'
file_to_zip = rf"D:\BulldogBackup\Bulldog Backup 2024 {todays_date}"
dst = os.path.join(current_dir, backupName)
shutil.copytree(source,dst)
shutil.make_archive(backupName, 'zip', file_to_zip)
shutil.rmtree(f'Bulldog Backup 2024 {todays_date}')
for files in os.listdir():
    if files.endswith(".zip"):
        file_date = files[20:30]
        file_date = datetime.strptime(file_date, '%m-%d-%Y')
        if (file_date + timedelta(days=180) > todays_date):
            os.remove(files)

# Backup 2024 file



# Schedule job windows
# Backup 2024 folder in one drive Friday at 8pm and Saturday at 8pm
# Save to D:
# ZIP file
# append folder name with dd-mm-yyyy
# Keep most recent 6 backups, delete oldest on each download based on filename 
#
#

