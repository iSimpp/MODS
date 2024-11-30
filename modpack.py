import sys
import os
import zipfile
from addmods import AddMod
from Library import *

# Load mod directories
ModdedDirs = LoadMods()

def Main():
    # Get the link and name from command-line arguments
    link = sys.argv[1]
    name = sys.argv[2]

    # Display available mod directories
    print(PrintItCool(ModdedDirs))

    # Ask the user for the destination directory
    try:
        choice = int(input(f'Where to save it?\nExample: 2 (2 is {ModdedDirs[1]})\n\n: ')) - 1
        # Ensure the choice is valid
        if ModdedDirs[choice]:
            pass
    except (IndexError, ValueError):
        raise IndexError(f"{Fore.RED}Invalid choice, please select a valid directory number.{Fore.RESET}")

    # Create a temporary folder for processing
    temp_folder = 'temp'
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)

    # Add mod to the chosen directory
    AddMod(temp_folder, link, name, True)

    # Extract mod contents to the selected directory
    with zipfile.ZipFile(Variables.DirectoryPaths, 'r') as zip_ref:
        zip_ref.extractall(ModdedDirs[choice])
