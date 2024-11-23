import Library
import colorama
import os
import requests
import shutil
from pathlib import Path

# Load modded directories
ModdedDirs = Library.LoadMods()
print(ModdedDirs)

# Prompt user to choose a version to export
print("Choose a Version to export:")
print(Library.PrintItCool(ModdedDirs))

version = int(input()) - 1

# Get the selected directory
ExportedDir = ModdedDirs[version]

# Full path of the folder to be exported
Exported = os.path.join(Library.Variables.DirectoryPaths, ExportedDir)


def compress_folder(folder_path):
    """Compress a folder into a .zip file in the 'Exports' directory."""
    folder_path = Path(folder_path).resolve()  # Resolve full path
    if not folder_path.is_dir():
        raise ValueError(f"{folder_path} is not a valid directory.")

    # Define the destination .zip file path
    export_dir = Path("Exports").resolve()
    zip_name = export_dir / f"{folder_path.name}.zip"

    # Compress the folder into the defined .zip file path
    shutil.make_archive(str(zip_name.with_suffix("")), 'zip', folder_path)
    return zip_name


def upload_to_fileio(file_path):
    """Upload a file to file.io."""
    url = "https://file.io"
    with open(file_path, 'rb') as file:
        response = requests.post(url, files={"file": file})
    return response.json()


def main(folder_path):
    try:
        # Compress the folder
        print(f"Compressing folder: {folder_path}")
        zip_file = compress_folder(folder_path)
        print(f"Folder compressed to: {zip_file}")

        # Upload the compressed folder
        print(f"Uploading {zip_file} to file.io...")
        response = upload_to_fileio(zip_file)

        # Optionally clean up the zip file
        os.remove(zip_file)
        print("Temporary zip file deleted.")

        print(f'{colorama.Fore.GREEN}Link: {response.get('link')}{colorama.Fore.RESET}')
        input()

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    folder = Exported
    main(folder)
