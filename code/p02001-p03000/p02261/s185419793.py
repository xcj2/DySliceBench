import sys
import math
import copy
from typing import Tuple, List
input = sys.stdin.readline

class Card:
    def __init__(self, idx):
        self.number = int(idx[1])
        self.design = idx[0]
    def __repr__(self):
        return "{}{}".format (self.design, self.number)


def  print_vec (A: list):
    print (" ".join(map (str, A)))

def swap (A: List, i: int, j: int) -> None:
    temp = A [i]
    A [i] = A [j]
    A [j] = temp



def bubble_sort (C: List [Card]) -> List [Card]:
    for i in range (len (C)):
        for j in range (len (C) - 1, i, -1):
            if C [j].number < C [j-  1].number:
                swap (C, j, j-1)
    return C

def selection_sort (C: List [Card]) -> List [Card]:
    for i in range (len (C)):
        minj = i
        for j in range (i, len (C)):
            if C [j].number < C [minj].number:
                minj = j
        if i != minj:
            swap (C, i, minj)
    return C

if __name__ == "__main__":
    n = int(input())
    vec =  list (map (lambda x: Card (x), input ().split ()))
    bubble_result = bubble_sort (copy.copy (vec))
    print_vec(bubble_result)
    print ("Stable")
    selection_result = selection_sort(copy.copy (vec))
    print_vec (selection_result)
    flag=  True
    for i in range (len (bubble_result)):
        if bubble_result [i] != selection_result [i]:
            flag = False
    if flag:
        print ("Stable")
    else:
        print ("Not stable")

