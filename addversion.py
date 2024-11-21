import os
import tkinter as tk
import sys
import shutil

# CONTROL, DO NOT TOUCH
DirectoryPaths = os.path.expandvars(r"%APPDATA%\Mods")

ModdedDirs = list()

if not os.path.exists(DirectoryPaths):
    os.mkdir(DirectoryPaths)

def SelectMod(moddir):
    # Join moddir with the base directory
    moddir = os.path.join(DirectoryPaths, moddir)
    
    # Check if the moddir exists
    if not os.path.exists(moddir):
        raise FileNotFoundError(f"The directory {moddir} does not exist.")
    
    # Get the Minecraft mods directory from the environment variable
    minecraft_mods_dir = os.path.expandvars(r'%APPDATA%\.minecraft\mods')
    
    # Try to copy the contents of moddir to the Minecraft mods directory
    try:
        # If the destination directory exists, delete its contents first
        if os.path.exists(minecraft_mods_dir):
            for filename in os.listdir(minecraft_mods_dir):
                file_path = os.path.join(minecraft_mods_dir, filename)
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
        
        # Copy the contents of moddir into minecraft_mods_dir
        for item in os.listdir(moddir):
            source = os.path.join(moddir, item)
            destination = os.path.join(minecraft_mods_dir, item)
            
            if os.path.isdir(source):
                shutil.copytree(source, destination)  # Copy subdirectories
            else:
                shutil.copy2(source, destination)  # Copy files
        
        print(f"Contents of {moddir} successfully copied to {minecraft_mods_dir}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def LoadMods():
    if not os.listdir(DirectoryPaths):
        print("There are no Directories")
    else:
        for eachdir in os.listdir(DirectoryPaths):
            ModdedDirs.append(eachdir)
        return ModdedDirs
        
def set_all_widgets_black(widget):
    # Set background color to black and text color to white if applicable
    if isinstance(widget, tk.Widget):
        widget.config(bg='#272A2C', bd=0, highlightthickness=0)  # Set background color to black, remove border
        if isinstance(widget, (tk.Label, tk.Button, tk.Entry)):  # Set text color for text-based widgets
            widget.config(fg='white')
    for child in widget.winfo_children():
        set_all_widgets_black(child)

def Ui():

    if sys.argv[1] == "cmduse":
        idx = sys.argv[2]
        LoadMods()
        SelectMod(ModdedDirs[idx])
    else:

        global root
        root = tk.Tk()
        root.title("Main Window")
        root.geometry("1000x500")
        root.config(bg="black")

        label = tk.Label(root, text="Versions Available", font=("Arial Rounded MT Bold", 24), bg="black")
        label.pack(pady=20)

        for idx, Dirs in enumerate(LoadMods()):
            button = tk.Button(root, text=ModdedDirs[idx], command=lambda idx=idx: SelectMod(ModdedDirs[idx]))
            button.pack(pady=5)

        set_all_widgets_black(root)
        root.mainloop()

        Ui()

