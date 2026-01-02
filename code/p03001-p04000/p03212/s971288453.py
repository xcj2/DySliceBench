import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = input()
    n_len = len(N)

    def dfs(val, is357):
        c = 0

        if (not is357
            and val.count('3') > 0
            and val.count('5') > 0
            and val.count('7') > 0):
            is357 = True

        if len(val) == n_len:
            if is357 and int(val) <= int(N):
                return 1
            else:
                return 0

        if is357:
            c+= 1

        c += dfs(val + '3', is357)
        c += dfs(val + '5', is357)
        c += dfs(val + '7', is357)
        return c

    print(dfs('', False))

if __name__ == '__main__':
    main()
