import sys
import math
from typing import Tuple, List
input = sys.stdin.readline

def  print_vec (A: list):
    print (" ".join(map (str, A)))

def swap (A: List, i: int, j: int) -> None:
    temp = A [i]
    A [i] = A [j]
    A [j] = temp
 

def selection_sort(A: List) -> Tuple[List, int]:
    swap_cout = 0
    for i in range(len(A)):
        mini = i
        for j in range(i, len(A)):
            if A[j] < A[mini]:
                mini = j
        if (mini != i):
            swap(A, i, mini)
            swap_cout+=1
    return (A, swap_cout)


if __name__ == "__main__":
    n = int(input())
    vec = list (map (int, input ().split ()))
    result =  selection_sort(vec)
    print_vec (result [0])
    print(result [1])

