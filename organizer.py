"""
DEV UTILS: File Organizer
Purpose: Automatically sort files in a development directory by extension.
Helps maintain a clean workspace for long-term projects.
"""
import os
import shutil

def organize_directory(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            extension = filename.split('.')[-1]
            if not os.path.exists(os.path.join(path, extension)):
                os.makedirs(os.path.join(path, extension))
            shutil.move(os.path.join(path, filename), os.path.join(path, extension, filename))
    print("Cleanup complete.")

if __name__ == "__main__":
    organize_directory(".")