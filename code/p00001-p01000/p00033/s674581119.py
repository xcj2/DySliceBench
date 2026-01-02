import sys
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    n = Z()
    for _ in range(n):
        A = ZZ()
        done = [False] * 10

        def dfs(i, a):
            if done[i]:
                if i+1 < 10: dfs(i+1, a)
                else: return
            else:
                if a < A[i]:
                    done[i] = True
                    if i+1 < 10: dfs(i+1, A[i])
                else:
                    if i+1 < 10: dfs(i+1, a)

        cc = 0
        for i in range(10):
            if done[i]: continue
            cc += 1
            done[i] = True
            dfs(i, A[i])

        print('YES' if cc <= 2 else 'NO')


    return

if __name__ == '__main__':
    main()

