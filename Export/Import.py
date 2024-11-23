import zipfile
import os
import sys
import Library
import requests

def unzip_file(zip_path):
    # Ensure the temp directory exists
    if not os.path.isdir('temp'):
        os.mkdir('temp')

    # Extract the files from the zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall('temp')

    # Get the full path to the temp directory
    temp_dir = os.path.abspath('temp')

    # Iterate through the files in the temp directory
    for file in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, file)  # Get the full file path
        if os.path.isfile(file_path):  # Check if it is a file
            destination = os.path.expandvars(r'%APPDATA%\\.minecraft\mods')
            # Move the file to the destination
            os.rename(file_path, os.path.join(destination, file))  # Renaming to move the file

    print("Files have been moved successfully.")


def main():
    link = sys.argv[1]
    name = sys.argv[2]
    request = requests.get(link)

    path = name
    with open(path, 'wb') as f:
        f.write(request.content)
    unzip_file(path)
main()
