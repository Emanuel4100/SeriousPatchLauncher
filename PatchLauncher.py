import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import time
import sys
import ctypes

CONFIG_FILE_PATH = "config.txt"

def open_program(exe_path):
    try:
        subprocess.Popen(f'"{exe_path}"', shell=True)
        print(f"Opened: {exe_path}")
        return True
    except Exception as e:
        print(f"Error opening {exe_path}: {e}")
        return False

def select_file(program_name):
    file_path = filedialog.askopenfilename(title=f"Select {program_name} exe file", filetypes=[("Executable files", "*.exe")])
    return file_path

def save_file_location(program_name, exe_path):
    with open(CONFIG_FILE_PATH, 'a') as config_file:
        config_file.write(f"{program_name}={exe_path}\n")

def load_file_locations():
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, 'r') as config_file:
            lines = config_file.readlines()
            config = {}
            for line in lines:
                key, value = line.strip().split('=')
                config[key] = value
            return config
    else:
        return {}

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Load existing file locations from the config file
    config = load_file_locations()

    # Set default paths
    patch_exe_path = config.get("patch", "")
    game_exe_path = config.get("game", "")

    # If either of the default paths is not valid, prompt the user to select them
    if not os.path.exists(patch_exe_path) or not os.path.exists(game_exe_path):
        print("Stored paths are not valid. Please select the exe files.")

        # Prompt user for patch exe path if not valid
        if not os.path.exists(patch_exe_path):
            patch_exe_path = select_file("patch")
            if not patch_exe_path:
                print("No patch program selected. Exiting.")
                sys.exit()

            # Store the selected patch path in the config file
            save_file_location("patch", patch_exe_path)

        # Prompt user for game exe path if not valid
        if not os.path.exists(game_exe_path):
            game_exe_path = select_file("game")
            if not game_exe_path:
                print("No game program selected. Exiting.")
                sys.exit()

            # Store the selected game path in the config file
            save_file_location("game", game_exe_path)

    # If paths are not valid, prompt the user to select them
    while not (open_program(patch_exe_path) and open_program(game_exe_path)):
        print("Selected paths are not valid. Please select the exe files again.")

        # Prompt user for patch exe path
        patch_exe_path = select_file("patch")
        if not patch_exe_path:
            print("No patch program selected. Exiting.")
            sys.exit()

        # Store the selected patch path in the config file
        save_file_location("patch", patch_exe_path)

        # Prompt user for game exe path
        game_exe_path = select_file("game")
        if not game_exe_path:
            print("No game program selected. Exiting.")
            sys.exit()

        # Store the selected game path in the config file
        save_file_location("game", game_exe_path)

    # Add a delay (adjust as needed)
    time.sleep(5)  # 5 seconds delay

    # Open game exe
    open_program(game_exe_path)

    # Close the console window
    ctypes.windll.kernel32.FreeConsole()

if __name__ == "__main__":
    main()
