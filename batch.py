import sys
import chess
import chess.pgn

# See: https://python-chess.readthedocs.io/en/latest/index.html

# Application State

global pgnFilePath
global outputFilePath

# Function Definitions

def parse_pgn_file():
    pgnConverter = pgntofen.PgnToFen()
    pgnConverter.resetBoard()

    return pgnConverter.pgnFile(pgnFilePath)

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

    # Parse PGN File

    pgn = open(pgnFilePath)
    game = chess.pgn.read_game(pgn)
    print(game)
    game = chess.pgn.read_game(pgn)
    print(game)
    game = chess.pgn.read_game(pgn)
    print(game)

    sys.exit()
    
    board = first_game.board()

    for move in first_game.mainline_moves():
        board.push(move)
    
    print(board.fen())

    #print(first_game)
    #sys.exit()
    #print("event: " + evt)
    print("Process complete.")