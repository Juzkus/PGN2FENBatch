# PGN2FENBatch

This project is made for Simon, but it is here for anyone finds it useful.

This script can be used to easily convert PGN data into FEN for end position analysis.

## Background

[Chess.com - How to automatically extract FEN code of several ammount of games?](https://www.chess.com/clubs/forum/view/how-to-automatically-extract-fen-code-of-several-ammount-of-games)

## Dependencies

### Language/Runtime

Python 3

### Library

python-chess
```powershell
pip install python-chess
```

## Usage

### Example

This will create the file "BobbyFischer.fen" with a list of FEN end position strings in the same order as BobbyFischer.pgn.

```powershell
python batch.py --pgn 'c:\users\your_user\desktop\BobbyFischer.pgn' --out 'c:\users\your_user\desktop\BobbyFischer.fen'
```
