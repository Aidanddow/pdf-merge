import merger
import tkinter as tk

import os
import sys
from pathlib import Path

DEFAULT_NAME = "OUTPUT_PDF"

# Return the path of user's desktop
def get_desktop():
    return os.path.join(str(Path.home()),"Desktop")

# Display basic help message
def help():
    print("Call pdf merger with:")
    print('"python3 main.py <path> <fname>"')
    print("-----------------------------------\n")
    sys.exit()


def funct(path, fname=DEFAULT_NAME):
    destination = os.path.join(get_desktop(),fname+".pdf")
    files = merger.getFiles(path)
    writer = merger.mergeFiles(files)

    with open(destination, 'wb') as f:
        writer.write(f)

def main():
    pass

main()