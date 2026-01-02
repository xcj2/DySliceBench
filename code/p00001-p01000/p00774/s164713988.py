from inspect import currentframe


def debug_print(s):
    # print(s)
    return


def debug_key(*args):
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    debug_print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))


def solve(H, stone):
    debug_print("\n-----solve-----")
    debug_key(stone)

    ans = -1
    tmp = 1
    while tmp:
        ans += tmp
        tmp = 0
        erase = [set() for _ in range(5)]
        for i in range(H):
            for j in range(1, 4):
                if stone[i][j - 1] == stone[i][j] == stone[i][j + 1]:
                    for k in range(j - 1, j + 2):
                        erase[k].add(i)
        stone2 = list(map(list, zip(*stone)))
        for j in range(5):
            for i in sorted(erase[j], reverse=True):
                tmp += stone[i][j]
                del stone2[j][i]
            stone2[j] = [0] * len(erase[j]) + stone2[j]
        stone = list(map(list, zip(*stone2)))
    print(ans)

    return


if __name__ == '__main__':

    while True:
        H_input = int(input())
        if H_input == 0:
            break
        stone_input = [list(map(int, input().split())) for _ in range(H_input)]
        solve(H_input, stone_input)


