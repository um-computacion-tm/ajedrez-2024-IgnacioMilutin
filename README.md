# **CHESS**

## by Ignacio Milutin 

## Rules

First lets start with some of the main features.Chess is a 2 player game. There are two colors, BLACK and WHITE (one for each player), and a board of 8x8 cells where the pieces will be displayed. There are 6 type of pieces. Each team has the same amount of each piece:

- 1 King (♚,♔)
- 1 Queen (♛,♕)
- 2 Bishops (♝,♗)
- 2 Knights (♞,♘)
- 2 Rooks (♜,♖)
- 8 Pawns (♟,♙)

The first turn of the game always belong to the white side. Only one piece can be moved in each turn, regardless of whether one piece ate another. The objective is that the players move and eat the other player pieces to reach the following conditions to end the game:

- Eat all the enemy color pieces

Anyway the game can be stoped with a draw if both player agree to end it. To ask the other player for a draw, type 'Draw' when being ask some for: from row, from col, to row or to col. NOTE: after typing draw the question to the other player if he or she wants to finish with a draw will be asked after typing all from row, from col, to row or to col. 

### Board

The board has a size of 8x8 cells, starting in the row 0 (cero) and finishing in the row 7 (seven). The same with the columns, starts in the column 0 (cero) and finishes in the column 7 (seven). The white player pieces are are always displayed in the bottom side of the board and the black player pieces always displayed in the upper side of the board. The pieces are displayed in the following order:

![alt text](/images/board.png)


### How to move each piece

Each piece has a diferent rule to move. In general, pieces cannot move through other piece (except for the night, which can jump through pieces). Pieces cannot move to a cell with a piece of their own color. They can be moved to an empty cell or a cell where a piece of the opposite color is displayed and eat it. When a piece is eaten, its taken out of the game.

To move a piece, first type the row and the column of the piece you ewant to move when asked (first from row and the from col) and then type the row and the column you would like to move the piece to, also when asked (first to col and the to row). 

Pieces rules to move are the following

- King: The king can only move one cell in any direction, up, down to the sides and diagonally. Anyway, the king cant be moved to a cell which an enemy piece is attacking.

- Queen: The queen can move any amount of cells she wants in the directions up, down, to the sides and diagonally

- Rook: the rook can move any amount of cells it wants in the directions up, down and to the sides

- Bishop: The bishop can move any amount of cells it wants in the diagonal directions

- Knight: The knight is the only piece that can move through other pieces. It moves like an 'L', to cells up, down or to the sides and then one cell 90 degree angle. he can only move or eat in the end of this movement.

- Pawn: The pawn moves and eats in to diferent directs. First lets talk about he move rules. It can move only one cell forward, except in their first move. When is its first move it can be moved one or two cells forward. The pawn only can eat a piece in a one cell move in a diagonal direction.

### Special Rules

Chess have several special moves. this are the following

- Pawn Promotion: When a pawn reaches the end of the board (if its a white pawn the row 0 (cero) and if its a black pawn the row 7 (seven)), it can be promoted an transformed to one of the following pieces: Queen, Bishop, knight or Rook.


### Thanks for reading the rules.

## Play

### Run and play with Docker

Install docker for Debian

```bash
sudo apt install docker
```

Create a docker Image, the xyntax is as follows:

```bash
docker buildx build -t name_of_the_image path/to/Dockerfile
```

Anyway you can cd into the repo directory and use:

```bash
docker buildx build -t ajedrez-2024-ignaciomilutin .
```
Play and run tests

```bash
docker run -i ajedrez-2024-IgnacioMilutin
```

### Play local

Clone the repository

```bash
git clone https://github.com/um-computacion-tm/ajedrez-2024-IgnacioMilutin.git
```

Install requirements

```bash
pip install -r requirements.txt 
```

Run the game

```bash
python -m cli
```

###  THANKS AND ENJOY THE GAME



## Circleci
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-IgnacioMilutin/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-IgnacioMilutin/tree/main)

## Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/0736aa4c8b6ce45f9436/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-IgnacioMilutin/maintainability)

## Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/0736aa4c8b6ce45f9436/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-IgnacioMilutin/test_coverage)

