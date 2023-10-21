import shutil
import os
import datetime

todays_date = datetime.datetime.today().strftime('%m-%d-%Y')

current_dir = os.getcwd()
print(current_dir)
source = 'C:/Users/FSAE/OneDrive - Mississippi State University/Documents - MSSTATE Formula SAE (UserCreated)/Mississippi State FSAE/FSAE 2024'
dst = os.path.join(current_dir, f'Bulldog Backup 2024 {todays_date}')
shutil.copytree(source,dst)
print("done")

# Backup 2024 file



# Schedule job windows
# Backup 2024 folder in one drive Friday at 8pm and Saturday at 8pm
# Save to D:
# ZIP file
# append folder name with dd-mm-yyyy
# Keep most recent 6 backups, delete oldest on each download based on filename 
#
#

