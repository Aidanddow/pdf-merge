import merger
import os
import sys
from pathlib import Path

DEFAULT_NAME = "OUTPUT_PDF"

# Return the path of user's desktop
def get_desktop():
    return os.path.join(str(Path.home(),"Desktop")

# Display basic help message
def help():
    print("Call pdf merger with:")
    print('"python3 main.py <path> <fname>"')
    print("-----------------------------------\n")
    sys.exit()

def handle_input():
    try:
        if sys.argv[1] in ('help', 'h', '-help', '--help', '-h', '--h', 'HELP', 'H'):
            help()
        # Set path to first command line argument
        path = sys.argv[1]
        
    except IndexError:
        # User has not specified a path, quit.
        print("No path specified")
        sys.exit()

    # If user has specified a filename, store it, otherwise use default
    try:
        fname = sys.argv[2]
    except IndexError:
        fname = DEFAULT_NAME

    return path, fname

def main():
    path, filename = handle_input()
    destination = os.path.join(get_desktop(),filename+".pdf")
    files = merger.getFiles(path)
    writer = merger.mergeFiles(files)

    with open(destination, 'wb') as f:
        writer.write(f)

if __name__ == "__main__":
    main()