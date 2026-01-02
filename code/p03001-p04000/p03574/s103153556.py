import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())


def main():
    H, W = mi()
    S = ['w'*(W+2)]+['w'+input()+'w' for i in range(H)]+['w'*(W+2)]
    ans = [[0]*W for i in range(H)]

    for j in range(1, W+1):
        for i in range(1, H+1):
            if S[i][j] == '#':
                ans[i-1][j-1] = '#'
            else:
                t = S[i-1][j-1]+S[i-1][j]+S[i-1][j+1] \
                +S[i][j-1]+S[i][j+1] \
                +S[i+1][j-1]+S[i+1][j]+S[i+1][j+1]
                ans[i-1][j-1] = str(t.count('#'))
    print(*(''.join(ans[i]) for i in range(H)), sep='\n')



if __name__ == '__main__':
    main()
