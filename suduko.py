#!/usr/bin/env python
# coding: utf-8


#solving sudoku without out backtracking

N = 9


def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()


def isSafe(grid, row, col, num):

    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(grid, row, col):

    if (row == N - 1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1):

        if isSafe(grid, row, col, num):

            grid[row][col] = num

            if solveSudoku(grid, row, col + 1):
                return True

        grid[row][col] = 0
    return False
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (solveSudoku(grid, 0, 0)):
    printing(grid)
else:
    print("no solution exists ")





# solving sudoku using backtracking


def print_grid(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j],end=" ")
        print('')


def evaluate(a, listV):
    for r in range(9):
        for c in range(9):
            if(a[r][c]== 0):
                listV[0]= r
                listV[1]= c
                return True
    return False


def rowEval(a, r, n):
    for i in range(9):
        if(a[r][i] == n):
            return True
    return False


def columnEval(a, c, n):
    for i in range(9):
        if(a[i][c] == n):
            return True
    return False


def boxEval(a, r, c, n):
    for i in range(3):
        for j in range(3):
            if(a[i + r][j + c] == n):
                return True
    return False


def locationCheck(a, r, c, n):
    return not rowEval(a, r, n) and not columnEval(a, c, n) and not boxEval(a, r - r % 3,c - c % 3, n)


def sudoku_solver(a):
    listV=[0, 0]
    if(not evaluate(a, listV)):
        return True
    r = listV[0]
    c = listV[1]
    for n in range(1, 10):
        if(locationCheck(a, r, c, n)):
            a[r][c]= n
            if(sudoku_solver(a)):
                return True
            a[r][c] = 0
    return False


if __name__=="__main__":
    grid =[[0 for x in range(9)]for y in range(9)]
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
           [5, 2, 0, 0, 0, 0, 0, 0, 0],
           [0, 8, 7, 0, 0, 0, 0, 3, 1],
           [0, 0, 3, 0, 1, 0, 0, 8, 0],
           [9, 0, 0, 8, 6, 3, 0, 0, 5],
           [0, 5, 0, 0, 9, 0, 6, 0, 0],
           [1, 3, 0, 0, 0, 0, 2, 5, 0],
           [0, 0, 0, 0, 0, 0, 0, 7, 4],
           [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if(sudoku_solver(grid)):
        print_grid(grid)
    else:
        print("No solution exists")


