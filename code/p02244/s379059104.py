
from collections import namedtuple

position = namedtuple("position","row column")
def input_queens():
    queens = []
    n = int(input())
    for _ in range(n):
        row,column = [int(x) for x in input().split()]
        queens.append(position(row,column))
    return queens

def output_board(queens):
    for r in range(8):
        for c in range(8):
            print("Q" if position(r,c) in queens else ".",end = "")
        print()

def atackable(p,queens):
    return(
        p.row in [q.row for q in queens]
        or p.column in [q.column for q in queens]
        or any([abs(p.row - q.row) == abs(p.column-q.column) for q in queens])
    )


def next_p(p):
    if p.column == 7:
        return position(p.row+1,0)
    else:
        return position(p.row,p.column+1)
def over(p):
    return p.row > 7
    
def all_queens(queens):
    def rec(p,queens):
        if len(queens) == 8:
            return queens
        elif over(p):
            return False
        elif atackable(p,queens):
            return rec(next_p(p),queens)
        else:
            result = rec(position(p.row+1,0),queens+[p])
            return result if result else rec(next_p(p),queens)
    return rec(position(0,0),queens)
    

queens = input_queens()
output_board(all_queens(queens))

