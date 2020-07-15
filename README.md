# PGN2FENBatch

This project is made for Simon, but it can be used by anyone who may find it useful.

## Background

[Chess.com - How to automatically extract FEN code of several ammount of games?](https://www.chess.com/clubs/forum/view/how-to-automatically-extract-fen-code-of-several-ammount-of-games)

The goal is to create a script that can easily convert PGN data into FEN for end positions.

## Dependency

### Language/Runtime

Python 3

### Library

[pgnToFen - Original](https://github.com/SindreSvendby/pgnToFen)

I have also created a fork of this repository for convenience:

[pgnToFen - Fork](https://github.com/Juzkus/pgnToFen)

## Usage

### Example

This will create the file "BobbyFischer.fen" with a list of FEN strings in the same order as BobbyFischer.pgn.

```
python batch.py -pgn 'c:\users\your_user\desktop\BobbyFischer.pgn' -out 'c:\users\your_user\desktop\BobbyFischer.fen'
```

## Important Note

The batch.py file requires the user to define the location of the pgnToFen module. Change the PGN_TO_FEN_PATH variable in the code to point to wherever you clone the pgnToFen code.
