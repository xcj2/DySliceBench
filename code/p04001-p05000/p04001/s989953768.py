from inspect import currentframe


def debug_print(s):
    # print(s)
    return


def debug_key(*args):
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    debug_print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))


def solve(S):
    N = len(S)
    ans = 0

    for i in range(2 ** (N - 1)):
        culculate = S[0]
        for j in range(N - 1):
            if i & (1 << j):
                culculate += "+" + S[j + 1]
            else:
                culculate += S[j + 1]
        ans += eval(culculate)
        debug_key(culculate)
    print(ans)


if __name__ == '__main__':

    S_input = input()

    solve(S_input)

