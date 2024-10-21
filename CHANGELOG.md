# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-10-20

First finished version

## [0.2.5] - 2024-10-19

### Added

- Rule to stop the game when somebody types draw
- Readme now includes the rules

## [0.2.4] - 2024-10-19

### Added 

- Rule to end the game when a piece runs out of pieces and its tests

## [0.2.3] - 2024-10-18

### Added

- valid_positions_rook_and_bishop unites the 2 valid positions in one method
- Rules function in chess to use in the cli to verifier rules after every move
- get_possible_positions method

### Changed

- rooks and bishops valid_postions updated due to the change in 'Added' 
- simplified all moves 
- simplified possible_positions_vertical_and_horizontal
- simplified possible_positions_diagonal
- divided all_moves in more methods to pass codeclimate
- updated knight moves
- updated board str
- updated pawn change to other piece method
- changed structure for valid-postions in king,knight,pawn now uses get_possible_postiosn function

## [0.2.2] - 2024-10-17

### Changed

- Updated moves of moves.py to be all together (va,vd,hl and hr) and (dal,dar,ddl,ddr)
- simplified kings moves 
- change boards pieces definition, now knight,bishop,rook and pawn are together and king and queen are together
- simplified pawns move and eat methods
- simplified moves all_moves method
- simplified chesses pawn_change_verification and add new tests to it

## [0.2.1] - 2024-10-16

### Added

- Tests for new move due to the changes below

### Changed

- All updates are to fix codeclimate issues
- Now Knight have combined moves in: (vdr and hrd), (vdl and hld), (val and hla), (var and hra) and valid_positions due to this changes
- Moves logic now are combined in: (va and hl), (vd and hr), (dar and ddr), (dal and ddl) and individual moves have one more parameter to adapt to the new logic

### Deleted

- All individual knights moves and their tests because of the changes

## [0.2.1] - 2024-10-15

### Added

- Pawn promotion methods, includes the verification and action methods in chess and the input for the selected piece to replace and its execution in cli
- Exception for a wrong pawn change option
- Tests for all new methods mentioned before

### Changed

- King valid_positions doesnt need obligatory parameter 'for_all_moves', so chess move method is updated due to that change'

## [0.1.15] - 2024-10-14

### Added

- get_opposite_color method in piece and tests for the function
- Test fro all_moves function with a king in the board

### Changed

- Added a parameter to kings valid_positions and added conditionals due to the change in chesses move method and all_moves function
- Tests for kings valid_positions corrected, there was no piece that put in danger the king
- Updated king moves tests, if the piece is black is not tested

## [0.1.14] - 2024-10-12

### Added

- Tests for king str, valid_positions and moves
- Method in moves that shows all one team moves and its test

### Known Issues

- Tests for king valid_postions dont pass

## [0.1.13] - 2024-10-11

### Added

- Tests for knight out of board in every knight move
- All knight moves and valid_postions methods

### Delete

- Knight tests for pieces in the middle

## [0.1.12] - 2024-10-10

### Added

- Tests for al knight moves, str and valid_positions

## [0.1.11] - 2024-10-04

### Added

- Valid_postiosn method for queen

## [0.1.10] - 2024-10-03

### Added

- Test for queen moves, str and valid_positions

## [0.1.9] - 2024-10-02

### Added 

- Diagonal ascendant left and right and diagonal descendant left and right moves

## [0.1.8] - 2024-10-01

### Added

- Tests for the all pieces creation creation 
- Tests for bishop moves, str, valid_positions and vertical and horizontal wrong moves

## [0.1.7] - 2024-09-27

### Added

- Moves file for all de moves that are in 2 or more pieces

### Changed

- Board str now has numbers from 0 to 7 not 1 to 8
- Updated rook test because of the moves changes
- Updated rook valid_positions method due to the moves changes

## [0.1.6] - 2024-09-26

### Added 

- Definition method for king, queen, bishop and knight
- Tests fro piece str one for each piece

### Changed

- Pawns possible_positions_move method now only have black and white options

## [0.1.5] - 2024-09-24

### Added

- New files for king, queen, bishop and knight with their str for each color

### Changed

- tests that include board print

### Known Issues

- All tests including the board str dont pass, update after adding other pieces

## [0.1.4] - 2024-09-23

### Added 

- Good path tests for move method in chess

### Changed

- Improved the board print

### Known Issues

- All tests including the board str dont pass, update after adding other pieces

## [0.1.3] - 2024-09-22

### Added

- Exception for wrong pawn move
- Tests fro piece methods: str and get_color

### Changed

- Now is_row_col_in_valid_postions is a piece method
- is_row_col_in_valid_positions tests in piece tests

## [0.1.2] - 2024-09-20

### Added 

- Tests for valid_postions for pawn

### Changed

- Corrected valid_positions method for pawn, because of possible_eat and possible move changes

## [0.1.1] - 2024-09-19

### Added

- Pawn file with methods: valid positions, possible_postions_eat, possible_positions_move
- Tests for pawn possible_postions_move and possible_positions_eat and str

### Changed

- Pawn str format
- STR tests in rook

## [0.1.28] - 2024-09-18

### Added 

- Tests for methods is_playing, turn and show_board from chess

## [0.1.27] - 2024-09-17

### Changed 

- Move method in chess now uses the method is_row_col_in_valid_postions 

## [0.0.26] - 2024-09-16

### Added

- Tests for move method in chess

## [0.0.25] - 2024-09-15

### Changed

- Updated tests for wrong diagonal moves in rook, due to the valid_positions change

## [0.0.24] - 2024-09-14

### Added

- Test for valid positions for rook
- Method to see if to_row and to-col are in valid_positions

### Changed

- Update valid_positions method for rook adding the horizontal moves

## [0.0.23] - 2024-09-13

### Added

- Horizontal left and right method for rook

## [0.0.22] - 2024-09-12

### Added

- Tests for horizontal right and left moves for rook

## [0.0.21] - 2024-09-11

### Added

- Added all possible wrong diagonal moves for rook

## [0.0.20] - 2024-09-06

### Added

- Tests for rook vertical asc with own and enemy piece in the middle
- Description in tests 

### Changed

- Vertical asc now detects other pieces
- Restructure rook movement tests with an empty board (for_test=True atribute)

## [0.0.19] - 2024-09-05

### Added

- ColumnOutOfRange and RowOutOfRange exceptions
- Tests for each specific mistake for get_piece and set_piece

### Changed

- Get_piece and set_piece now drops an specific exception if it the row, the column or both which failes

## [0.0.18] - 2024-09-04

### Added

- tests for set piece, in and out of range of board

### Changed

- restructure board tests, deleting the board setup
- set_piece has now condition for not setting out of board range

## [0.0.17] - 2024-09-03

### Added

- Add move method to board
- Test for rook not to move in diagonal descendant
- Test for board move
- messages to exceptions
- get_color method for piece
- test atribute to board to spwn an empty board 
- test for board getting cell out of the board

### Changed

- improved the get_piece method in board for not getting so it doesnt pick a cell ouside the board
- correct exceptions in code to throw the message
- Move from chess class now have conditions fro turn and empty positions

## [0.0.16] - 2024-09-02

### Changed

- Definitions that put rooks in the board are now a board method, the same with pawns

##  [0.0.15] - 2024-09-01

### Added 

- created rook file

### Changed

- Corrected piece str for str tests to pass

## [0.0.14] - 2024-08-30

### Changed

- Corrected test_rook for vertical descendant with own piece in the middle.
- Test for the rook str doesnt pass

### Known Issues

- Test for the rook str doesnt pass

## [0.0.13] - 2024-08-29

### Added

- Test for rook vertical descendant with a diferent color piece in the column

### Changed

- Corrected test for rook descendent moves 

### Known Issues

- Test for the rook str doesnt pass
- Test for vertical down move for rook doesnt pass

## [0.0.12] - 2024-08-28

### Added 

- Exceptions file, with invaled move, invaled move rook and invaled move no piece
- To turn method in chess, added the exception for invaled move
- Set piece method in board class
- Possible vertical up and down positions for rook

### Known Issues

- Test for the rook str doesnt pass
- Valid positions for rook unfinished
- Test for vertical down move for rook doesnt pass

## [0.0.11] - 2024-08-27

### Changed

- Pieces str is a Piece method, not an type of pieces method
- Add all test files to a test directory

### Removed 

-test main

### Known Issues

- Test for the rook str dont pass
- Possible moves for rook unfinished

## [0.0.10] - 2024-08-25

### Added

- Test for pawn creation in the board

### Changed

- Include de pawns in the board print

## [0.0.9] - 2024-08-24

### Added

- Pawn class, with constructor and str methods.
- Definition of the pawns in the board

## [0.0.8] - 2024-08-23

### Added

- Created new test for other wrong input entrys in cli

### Changed

- Deleted de name attribute for pieces
- Corrected test for rook defintion where a name was asked

## [0.0.7] - 2024-08-20

### Added

- Created test for cli,including 1 fro good input entry, 2 bad input entry and an invalid move
- Class for invalid move (in cli)
- Str method in board for printing the board
- Str method for rook in pieces for printing the rooks

### Known Issues

- To put test in test folder, import issue

## [0.0.6] - 2024-08-19

### Changed

- Update test for rook creation in test_board with the pieces name atribute

### Known Issues

- To put test in test folder, import issue

## [0.0.5] - 2024-08-17

### Added

- Name atribute to pieces

### Known Issues

- To put test in test folder, import issue

## [0.0.4] - 2024-08-16

### Added

- Test for empty board spaces

### Known Issues

- To put test in test folder, import issue

## [0.0.3] - 2024-08-15

### Added

- Test for board class, for get turn and the rooks creation
- Test_main file

### Known Issues

- To put test in test folder, import issue


## [0.0.2] - 2024-08-14

### Added

- Test for chess class, fof turn and change_turn methods'

### Known Issues

- To put test in test folder, import issue

## [0.0.1] - 2024-08-13

### Added

- CLI file
- Pieces file 
- Chess file
- Board file
- Docker file

### Changed

### Removed

### Known Issues

