import sys
sys.setrecursionlimit(500000)

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N = ii()
    A = list(mi())
    dic = {}
    l = []
    for a in A:
        if not a in dic:
            dic[a] = 0
        dic[a] += 1

    for k, v in dic.items():
        if v >= 2:
            l.append(k)
        if v >= 4:
            l.append(k)
        
    l.sort(reverse=True)

    if len(l) >= 2:
        print(l[0]*l[1])
    else:
        print(0)


if __name__ == '__main__':
    main()
