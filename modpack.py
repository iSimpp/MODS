import sys
import os
import zipfile
import json
import requests
from Library import *

# Load mod directories
ModdedDirs = LoadMods()

def AddMod(directory: str, link: str, name: str):
    # Download the mod
    url = requests.get(link)
    full_path = os.path.join(directory, name)
    
    # Save the file
    with open(full_path, 'wb') as f:
        f.write(url.content)
    return full_path

def ExtractMrpack(mrpack_path, destination):
    with zipfile.ZipFile(mrpack_path, 'r') as zip_ref:
        zip_ref.extractall(destination)
    print(f"Extracted .mrpack to {destination}")

def InstallFabricLoader(fabric_version, destination):
    # Fabric loader installation (assuming manual download and installation method)
    loader_url = f"https://fabricmc.net/download/loader/{fabric_version}"
    loader_path = os.path.join(destination, f"fabric-loader-{fabric_version}.jar")
    
    print(f"Downloading Fabric loader version {fabric_version}...")
    url = requests.get(loader_url)
    with open(loader_path, 'wb') as f:
        f.write(url.content)
    print(f"Installed Fabric loader to {loader_path}")

def InstallDependencies(dependencies, destination):
    if "fabric-loader" in dependencies:
        InstallFabricLoader(dependencies["fabric-loader"], destination)

    # Add other dependency checks here (e.g., specific Minecraft versions)

def ParseJsonFile(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def Main():
    # Get the link and name from command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python script.py <link> <name>")
        sys.exit(1)

    link = sys.argv[1]
    name = sys.argv[2]

    # Display available mod directories
    print(PrintItCool(ModdedDirs))

    # Ask the user for the destination directory
    try:
        choice = int(input(f'Where to save it?\nExample: 2 (2 is {ModdedDirs[1]})\n\n: ')) - 1
        if choice < 0 or choice >= len(ModdedDirs):
            raise IndexError
        destination_dir = os.path.join(Variables.DirectoryPaths, ModdedDirs[choice])
    except (IndexError, ValueError):
        raise IndexError(f"{Fore.RED}Invalid choice, please select a valid directory number.{Fore.RESET}")

    # Create a temporary folder for processing
    temp_folder = 'temp'
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)

    # Download the .mrpack file and extract it
    mrpack_path = AddMod(temp_folder, link, name + '.mrpack')

    # Extract the .mrpack to access the modrinth.index.json
    ExtractMrpack(mrpack_path, temp_folder)

    # Parse the modrinth.index.json for dependencies and mods
    json_path = os.path.join(temp_folder, 'modrinth.index.json')
    if not os.path.exists(json_path):
        print("Error: modrinth.index.json not found inside the .mrpack file.")
        sys.exit(1)

    # Parse the modpack JSON for dependencies and mods
    modpack_data = ParseJsonFile(json_path)

    # Install any necessary dependencies (e.g., Fabric loader)
    InstallDependencies(modpack_data["dependencies"], temp_folder)

    # Download and install each mod listed in the .json file
    for file in modpack_data["files"]:
        for mod_download in file["downloads"]:
            mod_name = mod_download.split("/")[-1]
            print(f"Downloading mod: {mod_name}")
            AddMod(destination_dir, mod_download, mod_name)

    # Clean up the temporary folder
    os.remove(mrpack_path)
    print(f"Modpack {name} installed successfully to {destination_dir}")

if __name__ == "__main__":
    Main()
