#File Management Script

import os
import shutil

# Source directory
source_dir = 'files/'

# List all files in the source directory
files = os.listdir(source_dir)

# Create subdirectories
os.makedirs('images', exist_ok=True)
os.makedirs('documents', exist_ok=True)
os.makedirs('other', exist_ok=True)

# Move files to respective subdirectories
for file in files:
    if os.path.isfile(file):
        if file.endswith(('.jpg', '.png', '.gif')):
            shutil.move(file, 'images/' + file)
        elif file.endswith(('.pdf', '.doc', '.txt')):
            shutil.move(file, 'documents/' + file)
        else:
            shutil.move(file, 'other/' + file)
