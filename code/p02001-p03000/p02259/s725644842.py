import sys
import math
from typing import Tuple
input = sys.stdin.readline

def  print_vec (A: list):
    print (" ".join(map (str, A)))

def swap (A, i, j):
    temp = A [i]
    A [i] = A [j]
    A [j] = temp
 

def bubble_sort(A: list) -> Tuple[list, int]:
    if len (A) <= 1:
        return (A, 0)
    swap_cout = 0
    for i in range(len(A)):
        for j in range(len(A) - 1, i + 1 - 1, -1):
            if A[j] < A[j - 1]:
                swap_cout += 1
                swap (A, j, j - 1)
    return (A, swap_cout)



if __name__ == "__main__":
    n = int(input())
    res = 0
    vec = list (map (int, input ().split ()))
    result=  bubble_sort(vec)
    print_vec (result [0])
    print(result [1])


