import os

def bulk_rename(directory, prefix):
    # Get list of files
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for index, filename in enumerate(files):
        # Skip the script itself if it's in the same folder
        if filename == 'bulk_renamer.py':
            continue
            
        extension = os.path.splitext(filename)
        new_name = f"{prefix}_{index + 1}{extension}"
        
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    pref = input("Enter the prefix: ")
    bulk_rename(path, pref)