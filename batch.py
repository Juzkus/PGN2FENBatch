import sys

# Change this to wherever you clone the pgnToFen repository
# Original: https://github.com/SindreSvendby/pgnToFen
PGN_TO_FEN_PATH = 'C:\\github.com\\Juzkus\\pgnToFen'

# Allows import statements to find modules in other directories.
sys.path.append(PGN_TO_FEN_PATH)

import pgntofen

# Function Definitions

def get_fen_string(obj):
    print(obj)

# Main Program Begins Here

if __name__ == "__main__":
    print("Process Started.")
