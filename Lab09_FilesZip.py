"""
Author: Raymond Llamas
Course: PCC - CIS188 - Scripting for Automation
Instructor: P. Farmer
Description:
This program organizes files into designated folders based on their file types. It performs the following tasks:
1. Creates two new folders, called images and pdf.
2. Traverses the given directory structure to identify and move PDF and image files to the respective folders.
3. Prints a directory listing of both the images and pdf folders.
4. Displays the total number of files in each folder.

"""

import os
import shutil
from pathlib import Path
import zipfile

# Step 1: Unzip the file
# This block of code will unzip the 'files.zip' archive into a directory named 'files'
zip_file = 'files.zip'
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall('files')

# Step 2: Create directories for images and pdfs
# Define the base directory where files are extracted
base_dir = Path('files')

# Define the paths for the new directories 'images' and 'pdf'
images_dir = base_dir.parent / 'images'
pdf_dir = base_dir.parent / 'pdf'

# Create the 'images' and 'pdf' directories if they don't already exist
images_dir.mkdir(exist_ok=True)
pdf_dir.mkdir(exist_ok=True)

# Step 3: Walk through the directory tree and move files
# Use os.walk to go through each directory and subdirectory in the 'files' directory
for root, _, files in os.walk(base_dir):
    for file in files:
        file_path = Path(root) / file  # Get the full path of the current file
        # Check the file extension and move to the appropriate directory
        if file_path.suffix == '.jpg':
            shutil.move(str(file_path), str(images_dir / file_path.name))
        elif file_path.suffix == '.pdf':
            shutil.move(str(file_path), str(pdf_dir / file_path.name))

# Step 4: Print directory listings and the total number of files
# Define a function to print the contents of a directory and count the files
def print_directory_listing_and_count(directory):
    print(f"\nDirectory listing for {directory}:")  # Print the directory name
    file_count = 0  # Initialize a counter for the number of files
    # Use os.walk to go through each directory and subdirectory
    for root, _, files in os.walk(directory):
        for file in files:
            print(file)  # Print each file name
            file_count += 1  # Increment the file counter
    print(f"Total number of files in {directory}: {file_count}")  # Print the total count of files

# Print the listings and counts for the 'images' and 'pdf' directories
print_directory_listing_and_count(images_dir)
print_directory_listing_and_count(pdf_dir)
