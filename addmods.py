import os
import sys
from colorama import Fore
import requests
from version import SelectMod
from Library import *

ModdedDirs = LoadMods()


def AddMod(directory: str, link: str, name: str, zip=False):
    if not zip:
        url = requests.get(link)
        name = name + '.jar'
        full_path = os.path.join(directory, name)
        with open(full_path, 'wb') as f:
            f.write(url.content)
    elif zip:
        url = requests.get(link)
        name = name + '.zip'
        full_path = os.path.join(directory, name)
        with open(full_path, 'wb') as f:
            f.write(url.content)



def main():
    print(PrintItCool(ModdedDirs))
    choice = int(input(f'Choose the version\nExample: 2 (2 is {ModdedDirs[1]})\n\n: '))
    choice = choice -1
    try:
        ModdedDirs[choice]
    except IndexError:
        raise IndexError(f"{Fore.RED}There aren't THAT many choices tho{Fore.RESET}")

    link = sys.argv[1]
    name = sys.argv[2]

    FullPath = os.path.join(Variables.DirectoryPaths, ModdedDirs[choice])
    AddMod(FullPath, link=link, name=name)
    SelectMod(ModdedDirs[choice])
    
main()