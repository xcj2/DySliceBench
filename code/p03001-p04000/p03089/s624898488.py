import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():

        N = int(input())
        B = list(map(int, input().split()))
        ans = []

        while len(B) > 0:
            flag = False

            for i in reversed(range(len(B))):
                if B[i] == i+1:
                    ans.append(B[i])
                    B.pop(i)
                    flag = True
                    break
            if not flag:
                return None

        return ans


    ans=main()
    if ans:
        for i in reversed(ans):
            print(i)
    else:
        print(-1)

resolve()