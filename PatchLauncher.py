import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import time
import sys  # Import the sys module

# Default paths (change these as needed)
DEFAULT_PATCH_EXE_PATH = " "
DEFAULT_GAME_EXE_PATH = " "

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

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Set default paths
    patch_exe_path = DEFAULT_PATCH_EXE_PATH
    game_exe_path = DEFAULT_GAME_EXE_PATH

    # If either of the default paths is not valid, prompt the user to select them
    if not os.path.exists(patch_exe_path) or not os.path.exists(game_exe_path):
        print("Default paths are not valid. Please select the exe files.")

        # Prompt user for patch exe path if not valid
        if not os.path.exists(patch_exe_path):
            patch_exe_path = select_file("patch")
            if not patch_exe_path:
                print("No patch program selected. Exiting.")
                sys.exit()

        # Prompt user for game exe path if not valid
        if not os.path.exists(game_exe_path):
            game_exe_path = select_file("game")
            if not game_exe_path:
                print("No game program selected. Exiting.")
                sys.exit()

    # If paths are not valid, prompt the user to select them
    while not (open_program(patch_exe_path) and open_program(game_exe_path)):
        print("Selected paths are not valid. Please select the exe files again.")

        # Prompt user for patch exe path
        patch_exe_path = select_file("patch")
        if not patch_exe_path:
            print("No patch program selected. Exiting.")
            sys.exit()

        # Prompt user for game exe path
        game_exe_path = select_file("game")
        if not game_exe_path:
            print("No game program selected. Exiting.")
            sys.exit()

    # Add a delay (adjust as needed)
    time.sleep(5)  # 5 seconds delay

    # Open game exe
    open_program(game_exe_path)

if __name__ == "__main__":
    main()
