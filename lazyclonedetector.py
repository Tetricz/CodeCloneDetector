import sys
import os

from preprocessor import preprocessor

def main(target_dir):

    prp = preprocessor()

    prp.process_dir(target_dir)

if __name__ == "__main__":
    print(" argv: ",sys.argv)
    nargs = len(sys.argv)
    if (nargs < 2):
        print(" Usage: lazyclonedetector {filename}")
        exit()
    directory = sys.argv[1]
    main(directory)
