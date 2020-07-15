import sys

# Change this to wherever you clone the pgnToFen repository
# Original: https://github.com/SindreSvendby/pgnToFen
PGN_TO_FEN_PATH = 'C:\\github.com\\Juzkus\\pgnToFen'

# Allows import statements to find modules in other directories.
sys.path.append(PGN_TO_FEN_PATH)

import pgntofen

# Application State

global pgnFilePath
global outputFilePath

# Function Definitions

def get_fen_string(obj):
    print(obj)

def print_usage():
    print('batch.py --pgn \'c:\\path\\to\\file.pgn\' --out \'c:\\path\\to\\out.fen\'')

# This will set our global variables for PGN file path and output file.
# I wrote this because getopt did not quite work as I expected.
def parse_cmd_args():
    
    nextIsPgn = False
    nextIsOut = False

    global pgnFilePath
    global outputFilePath

    for arg in sys.argv[1:]:

        if nextIsPgn:
            pgnFilePath = arg
        
        if nextIsOut:
            outputFilePath = arg
        
        if arg == '--pgn':
            nextIsPgn = True
            nextIsOut = False

        elif arg == '--out':
            nextIsOut = True
            nextIsPgn = False

        else:
            nextIsPgn = False
            nextIsOut = False

# Main Program Begins Here

if __name__ == "__main__":
    global pgnFilePath
    global outputFilePath

    pgnFilePath = ''
    outputFilePath = ''

    parse_cmd_args()

    if pgnFilePath == '' or outputFilePath == '':
        print_usage()
        sys.exit()

    print('PGN File: ' + pgnFilePath + "\n")
    print('OUT File: ' + outputFilePath + "\n")

    print("Process complete.")