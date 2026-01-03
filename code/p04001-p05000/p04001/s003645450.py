import sys
import copy

sys.setrecursionlimit(10**6)

def solve():
    S = input()
    lst = [int(S)]
    print(sum(func(S, 1, lst)))
    
def func(s, insertInd, lst):
    if insertInd == len(s):
        return lst
    
    else:
        copied = s
        inserted = copied[:insertInd] + '+' + copied[insertInd:]
        lst.append(evalsum(inserted))
        a = func(inserted, insertInd + 2, lst) 

        inserted = copied[:insertInd] + ' ' + copied[insertInd:]
        if inserted in '+':
            lst.append(evalsum(inserted))
        func(inserted, insertInd + 2, lst)
        
        return a

def evalsum(s):
    s = s.replace(' ', '')
    return sum(list(map(int, s.split('+'))))

if __name__ == '__main__':
    solve()