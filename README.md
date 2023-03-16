
# Nero Chess Engine

This is a simple chess engine that uses Python and the [python-chess library](https://python-chess.readthedocs.io/en/latest/)  to play chess. The engine uses a basic evaluation function that assigns values to each piece and position on the board. It also uses the Polyglot book format to help with move selection.

## Installation

To use this chess engine, follow these steps:

1. Install Python. You can download it from the [official website](https://www.python.org/downloads/).
2. Install the python-chess library by running the following command:

```
pip install python-chess
```

3. Clone this repository or download the ZIP file and extract it.

## Usage

To use the chess engine, open a Python console in the project directory and run the following command:
```
python chessConsole.py
```

```
     a b c d e f g h

8    R N B Q K B N R    8
7    p p p p p p p p    7
6    x x x x x x x x    6
5    x x x x x x x x    5
4    x x x x x x x x    4
3    x x x x x x x x    3
2    p p p p p p p p    2
1    R N B Q K B N R    1

     a b c d e f g h
White Plays : e4
```
This will start a game of chess against the engine. The engine will play the white pieces, and you will play the black pieces.

When it's your turn to move, the engine will display the current state of the board and prompt you for your move. Moves should be entered in [Standard Algebraic Notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)#Notation_for_moves), such as `e4` to move the pawn to `e4`.

The engine will then make its move and the game will continue until checkmate or a draw is reached

## Evaluation Function
The engine's evaluation function assigns values to each piece and position on the board. The values are based on common strategies and tactics in chess, such as controlling the center of the board, protecting the king, and attacking the opponent's pieces.

The values are stored in tables for each piece type, such as `PawnTable`, `KnightsTable`, and so on. Each table represents the values for each square on the board for that piece type.

For example, the `PawnTable` looks like this:

```
0, 0, 0, 0, 0, 0, 0, 0,
5, 10, 10, -20, -20, 10, 10, 5,
5, -5, -10, 0, 0, -10, -5, 5,
0, 0, 0, 20, 20, 0, 0, 0,
5, 5, 10, 25, 25, 10, 5, 5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
0, 0, 0, 0, 0, 0, 0, 0
```
This table represents the values for each square on the board for a pawn. The value of each square is added to the overall score for the position.

## Polyglot Opening Book
The engine uses the Polyglot book format to help with move selection. This format provides a pre-built opening book that contains the most common opening moves and their responses.

The Polyglot book is loaded when the engine starts, and the engine will use it to select its opening moves. Once the book is exhausted, the engine will switch to its own move selection algorithm.

## Conclusion
This is a simple chess engine that uses Python and the python-chess library to play chess. It uses a basic evaluation function and the Polyglot opening book format to help with move selection.


