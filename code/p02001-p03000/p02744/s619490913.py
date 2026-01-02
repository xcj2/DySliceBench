import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    return N,

def standalize(N):

    q = list()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    def dfs(i, s=[]):
        """i種類の文字から選んで、sの末尾に追加する
        """
        if len(s) == N:
            q.append(''.join(s))
        else:
            for j, a in enumerate(alphabets[:i-1]):
                dfs(i, s + [a])
            a = alphabets[i-1]
            dfs(i+1, s + [a])
    
    dfs(2, s=['a'])
    return q

def solve(N):
    for s in standalize(N):
        print(s)

if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % outputs)
