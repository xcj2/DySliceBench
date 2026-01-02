import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7
res = 0


def resolve():
    n = int(input())

    def is_ok(L):
        l = "".join(L)
        if int(l) <= n:
            for i in ["7", "5", "3"]:
                if i not in l:
                    return False
            else:
                return True
        else:
            return False

    def dfs(L):
        global res
        if len(L) == len(str(n)):
            return

        for i in ["7", "5", "3"]:
            L.append(i)
            if is_ok(L):
                res += 1
            dfs(L)
            L.pop()

        return res

    print(dfs([]))


if __name__ == '__main__':
    resolve()
