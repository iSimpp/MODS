from addmods import AddMod
import sys
from Library import *
import zipfile
import os
ModdedDirs = LoadMods()

def Main():
    link = sys.argv[1]
    name = sys.argv[2]
    # Dir choosing
    print(PrintItCool(ModdedDirs))
    choice = int(input(f'Where to save it?\nExample: 2 (2 is {ModdedDirs[1]})\n\n: '))
    choice = choice -1
    try:
        ModdedDirs[choice]
    except IndexError:
        raise IndexError(f"{Fore.RED}There aren't THAT many choices tho{Fore.RESET}")
    
    temp_folder = os.mkdir('temp')
    AddMod(temp_folder, link, name, True)
    zipfile.ZipFile.extractall(Variables.DirectoryPaths, ModdedDirs[choice])