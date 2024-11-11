import sys
import os

DirectoryPaths = os.path.expandvars(r"%APPDATA%\Mods")
def AddDir(name: str):
    FullPath = os.path.join(DirectoryPaths, name)
    if not os.path.exists(FullPath):
        os.mkdir(FullPath)
    else:
        print("Already exists.")

def main():
    dirname = sys.argv[1]
    AddDir(dirname)