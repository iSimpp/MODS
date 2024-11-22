import os
import sys
from colorama import Fore
import requests
from addversion import SelectMod
DirectoryPaths = os.path.expandvars(r"%APPDATA%\Mods")
ModdedDirs = list()

def LoadMods():
    if not os.listdir(DirectoryPaths):
        print(f"{Fore.RED}There are no Directories")
    else:
        for eachdir in os.listdir(DirectoryPaths):
            ModdedDirs.append(eachdir)
        return ModdedDirs
def PrintItCool(thelist: list):
    idx = 1
    theprint = ""
    for directory in thelist:
        theprint += f"{idx} |\t{directory}\t|\n"
        idx += 1
    return theprint

def AddMod(directory: str, link: str, name: str):
    url = requests.get(link)
    name = name + '.jar'
    full_path = os.path.join(directory, name)
    with open(full_path, 'wb') as f:
        f.write(url.content)

LoadMods()


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

    FullPath = os.path.join(DirectoryPaths, ModdedDirs[choice])
    AddMod(FullPath, link=link, name=name)
    SelectMod(ModdedDirs[choice])
    
main()