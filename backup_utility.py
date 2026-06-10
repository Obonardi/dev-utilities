import shutil
import os
from datetime import datetime

def create_backup(source_dir, backup_dir):
    # Create a timestamped name for the backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = os.path.join(backup_dir, f"backup_{timestamp}")
    
    try:
        shutil.make_archive(backup_filename, 'zip', source_dir)
        print(f"Success: Backup created at {backup_filename}.zip")
    except Exception as e:
        print(f"Error creating backup: {e}")

if __name__ == "__main__":
    src = input("Enter the directory to back up: ")
    dst = input("Enter the backup destination folder: ")
    create_backup(src, dst)