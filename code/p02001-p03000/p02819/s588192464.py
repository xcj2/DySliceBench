import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]

    
def main():
    X = int(input())
    N = [True] * 110000
    N[0] = False
    N[1] = False  

    n = 2
    while n < X:
        if N[n]:
            for s in range(1, 110000 // n):
                N[n * s] = False
            n += 1
            continue
        else:
            n += 1


    while not N[n]:
        n += 1
    
    print(n)

if __name__ == "__main__":
    main()