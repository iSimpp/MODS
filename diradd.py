import sys
import os

DirectoryPaths = os.path.expandvars(r"%APPDATA%\Mods")

def AddDir(name: str):
    FullPath = os.path.join(DirectoryPaths, name)
    try:
        if not os.path.exists(FullPath):
            os.mkdir(FullPath)
            print(f"Directory '{name}' created successfully.")
        else:
            print(f"Directory '{name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Could not create directory '{name}'.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <dirname>")
        sys.exit(1)
        
    dirname = sys.argv[1]
    AddDir(dirname)

if __name__ == "__main__":
    main()
