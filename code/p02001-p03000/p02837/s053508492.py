import sys
input = sys.stdin.readline
from operator import eq, ne

def readlines(n):
    for _ in range(n):
        x, y = input().split()
        yield int(x)-1, y

def main():
    n = int(input())
    graph = []

    for _ in range(n):
        a = int(input())
        graph.append(list(readlines(a)))

    def check(bits):
        for pre_honest, asserts in zip(bits, graph):
            if pre_honest == "0":
                continue
            for x, y in asserts:
                if bits[x] != y:
                    return -1
        
        return len([b for b in bits if b == "1"])

    for i in range(2**n-1, -1, -1):
        bit = format(i, "0{}b".format(n))
        ans = check(bit)
        if ans > -1:
            print(ans)
            return
    
    print(0)

main()
