# Main
import merger
import os


OUTPUT = '/Users/aidan/desktop'
NAME = "OUTPUT_PDF"

def main():
    path = '/Users/aidan/downloads/pdfs'
    destination = os.path.join(OUTPUT,NAME+".pdf")

    files = merger.getFiles(path)
    writer = merger.mergeFiles(files)

    with open(destination, 'wb') as f:
        writer.write(f)
        f.close()


if __name__ == "__main__":
    main()