import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    S = [input() for i in range(N)]
    MARCH = 'MARCH'
    dic = {
        'M': 0,
        'A': 0,
        'R': 0,
        'C': 0,
        'H': 0
    }
    for i in range(N):
        if S[i][0] in dic:
            dic[S[i][0]] += 1

    ans = 0

    for i in range(3):
        for j in range(i+1, 4):
            for k in range(j+1, 5):
                ans += dic[MARCH[i]]*dic[MARCH[j]]*dic[MARCH[k]]

    print(ans)

if __name__ == '__main__':
    main()
