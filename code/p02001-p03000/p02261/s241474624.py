from copy import copy
from collections import defaultdict


def bubblesort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if int(C[j][-1]) < int(C[j-1][-1]):
                C[j], C[j-1] = C[j-1], C[j]
    return C


def selectionsort(C, N):
    for i in range(N):
        minj = i
        for j in range(i+1, N):
            if int(C[j][-1]) < int(C[minj][-1]):
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C
  

def soot_order(C):
    ret = defaultdict(list)
    for c in C:
        soot = c[0]
        number = c[1]
        ret[number].append(soot)
    return ret


def judge_stable(C, N, order):
    
    cursor = 0
    stable = True
    while cursor < N:
        number = C[cursor][1]
        soots = order[number]
        for soot in soots:
            if C[cursor][0] != soot:
                print("Not stable")
                stable = False
                cursor += N
                break
            else:
                cursor += 1
    if stable:
        print("Stable")
        

def main():
    N = int(input())
    C = [c for c in input().split()]    
    
    order = soot_order(C)
    
    _C = copy(C)
    C_order = bubblesort(_C, N)
    print(' '.join(C_order))
    
    judge_stable(C_order, N, order)
    
    C_order = selectionsort(C, N)
    print(' '.join(C_order))
    
    judge_stable(C_order, N, order)
    
    
if __name__=="__main__":
    main()
