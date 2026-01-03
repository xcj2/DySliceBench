import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def read():
    S = input().strip()
    return S,


def solve(S):
    N = len(S)
    
    def dfs(i):
        enable = False
        if i == N:
            return True
        elif i > N:
            return False
        if S[i:i+7] == "dreamer":
            enable |= dfs(i+7)
        if S[i:i+6] == "eraser":
            enable |= dfs(i+6)
        if S[i:i+5] in ["dream", "erase"]:
            enable |= dfs(i+5)
        return enable
    
    return "YES" if dfs(0) else "NO"


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
