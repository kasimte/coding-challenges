# Inspired and adapted from
# https://github.com/dvitsios/codesignal-my-solutions/blob/master/Sudoku2/sudoku2.py

def sudoku2(grid):

# Testing
#

# row = [1,2,3]
# row2 = [0,3,3]
# print(row_is_valid(row))
# print(rows_are_valid([row, row2]))

# grid = [[".",".",".",".","2",".",".","9","."], 
#  [".",".",".",".","6",".",".",".","."], 
#  ["7","1",".",".","7","5",".",".","."], 
#  [".","7",".",".",".",".",".",".","."], 
#  [".",".",".",".","8","3",".",".","."], 
#  [".",".","8",".",".","7",".","6","."], 
#  [".",".",".",".",".","2",".",".","."], 
#  [".","1",".","2",".",".",".",".","."], 
#  [".","2",".",".","3",".",".",".","."]]

print(sudoku2(
[[".",".",".",".",".",".",".",".","2"], 
 [".",".",".",".",".",".","6",".","."], 
 [".",".","1","4",".",".","8",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".",".","3",".",".",".","."], 
 ["5",".","8","6",".",".",".",".","."], 
 [".","9",".",".",".",".","4",".","."], 
 [".",".",".",".","5",".",".",".","."]]))

# print(rows_are_valid(grid))
