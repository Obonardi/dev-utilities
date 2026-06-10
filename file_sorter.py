import os
import shutil

# Configuration: Define where files should go
EXTENSIONS = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Archives': ['.zip', '.tar', '.gz']
}

def auto_sort(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue
            
        # Get extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        # Find category
        for category, extensions in EXTENSIONS.items():
            if ext in extensions:
                category_path = os.path.join(directory, category)
                os.makedirs(category_path, exist_ok=True)
                shutil.move(filepath, os.path.join(category_path, filename))
                print(f"Moved: {filename} to {category}")
                break

if __name__ == "__main__":
    path = input("Enter the directory to sort: ")
    auto_sort(path)