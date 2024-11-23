import os
from colorama import Fore

class Variables:
    DirectoryPaths = os.path.expandvars(r"%APPDATA%\Mods")

def LoadMods():
    ModdedDirs = list()
    if not os.listdir(Variables.DirectoryPaths):
        print(f"{Fore.RED}There are no Directories")
    else:
        for eachdir in os.listdir(Variables.DirectoryPaths):
            ModdedDirs.append(eachdir)
        return ModdedDirs
def PrintItCool(thelist: list):
    idx = 1
    theprint = ""
    for directory in thelist:
        theprint += f"{idx} |\t{directory}\t|\n"
        idx += 1
    return theprint