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

import os # Helps us interact with the operating system
import shutil # Helps us move files

# Define the paths for the directories
base_dir = 'files'  # This is the directory where your files are located
images_dir = 'images'  # This will be the directory for image files
pdf_dir = 'pdf'  # This will be the directory for PDF files

# Create the images and pdf directories if they do not exist
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)
