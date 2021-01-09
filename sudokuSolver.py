## initialize puzzle board
puzzle = []

## read file in for puzzle
def readFile(board):
  file = open("sudoku.txt", 'r')
  nums = file.readlines() ## store list

  for line in nums: ## each item in list
    r = []
    for n in line: ## each character in item
      if n.isdigit(): 
        r.append(int(n)) ## add to inner list
    board.append(r) ## add to primary list

## solves using recursion + backtracking
def solve(board):
  found = findEmptySlot(board) ## slot that has no number, is a tuple!
  if not found:
    return True
  else:
    row, col = found 

  for n in range(1,10):
    if possible(board, n, (row, col)):
      board[row][col] = n  # n is possible

      if solve(board): ## take recursive step
        return True

      board[row][col] = 0 ## n does not fit, so backtrack

  return False

## is the number valid? using the puzzle, number, slot position (tuple)
def possible(board, num, slot):
  ## check row, loop through cols
  for i in range(len(board[0])):
    if board[slot[0]][i] == num and slot[1] != i:
      return False

  ## check col, loop through rows
  for i in range(len(board)):
    if board[i][slot[1]] == num and slot[0] != i:
      return False

  ## figure what quadrant we are in, using integer division
  quadX = (slot[1] // 3)
  quadY = (slot[0] // 3)

  ## check quadrant, loop through row & col
  for i in range(quadY*3, quadY*3 + 3):
    for j in range(quadX*3, quadX*3 + 3):
      if board[i][j] == num and (i, j) != slot:
          return False

  return True

## seperate into 9 quadrants
def printB(board):
  for i in range(len(board)):
    ## rows = 9, seperating at every third interval except the first
    if i % 3 == 0 and i != 0:
      print("---------------------")

    ## cols = 9, seperating at every third interval except the first
    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print("| ", end="")  ## to prevent '\n'

      if j == 8:
        print(board[i][j])
      else:
        print(str(board[i][j]) + " ", end="")

def findEmptySlot(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        return (i, j)  ## row, col

  return None

readFile(puzzle)
printB(puzzle)
solve(puzzle)
print("=====================")
printB(puzzle)
