import sys
import json
from pathlib import Path


def rename_all_folders(main_folder):
    folders = [f for f in main_folder.iterdir() if f.is_dir()]
    for folder in folders:
        if not folder.name.isnumeric():
            continue
        workshop_file = folder / "zone" / "workshop.json"
        if not workshop_file.is_file():
            print(f"{folder.name} does not have a workshop file, skipping.")
            continue

        name = None
        with open(workshop_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                name = data.get("FolderName")
            except json.JSONDecodeError:
                print(f"Error decoding JSON in {workshop_file}, skipping.")
                continue

        if name:
            new_folder = folder.parent / name
            print(f"Renaming {folder} to {new_folder}")

            try:
                folder.rename(new_folder)
            except:
                print("Could not rename folder, try running as administrator, skipping.")


if getattr(sys, 'frozen', False):  # Running as compiled with PyInstaller
    script_dir = Path(sys.executable).parent
else:  # Running as a .py file
    script_dir = Path(__file__).parent

print("(Unofficial) BOIIIWD Helper -> Renamer")
print("BOIII game directory:", script_dir)

mods_folder = script_dir / "mods"
maps_folder = script_dir / "usermaps"

if not mods_folder.is_dir():
    print("The mods folder does not exist, skipping to maps.")
else:
    print("The mods folder exists, renaming folders.")
    rename_all_folders(mods_folder)

if not maps_folder.is_dir():
    print("The usermaps folder does not exist, quitting.")
    input("Press enter to continue...")
    quit(0)
else:
    print("The usermaps folder exists, renaming folders.")
    rename_all_folders(maps_folder)

print("Finished renaming folders, quitting.")
input("Press enter to continue...")
quit(0)
