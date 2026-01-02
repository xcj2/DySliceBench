import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0:
        a, b = b, a % b
    return b
  
def solve():
    N, M = map(int, line_input())
    food_liked = [0] * M
    for i in range(N):
        person_i = list(map(int, line_input()))
        for a in person_i[1:]:
            food_liked[a-1] += 1
    num_of_everyone_like = 0
    for m in range(M):
        if food_liked[m] == N:
            num_of_everyone_like += 1
    return num_of_everyone_like

  
if __name__ == "__main__":
    print(solve())