import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def calc(F):    
    res = 0
    for f in F:
        S = format(f, "024b")[22::-1]
        count = 12
        tmp = 1
        for s in S:
            if s == "1":
                count = min(count, tmp)
                tmp = 1
            else:
                tmp += 1
        count = min(count, tmp)
        res = max(res, count)
    
    return res


def g(D, F):
    if len(D) == 0:
        return calc(F)

    d = D[0]
    s = set()
    for f in F:
        if (f >> d) & 1 == 0:
            s.add(f + 2 ** d)
        
        d = 24 - d
        if (f >> d) & 1 == 0:
            s.add(f + 2 ** d)
    
    return g(D[1:], s)
    

def main():
    N = int(input())

    D = read_list()
    if D.count(0) > 0:
        print(0)
        return
    F = {1,}    
    print(g(D, F)) 
    

if __name__ == "__main__":
    main()
