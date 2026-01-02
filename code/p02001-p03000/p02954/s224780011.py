import sys


def roundup_div(a, b):
    return (a + b - 1) // b


def solve(S: str):
    pressed = []
    r = []
    rc = 0
    l = []
    lc = 0
    for c in S:
        if c == "R":
            rc += 1
            if lc > 0:
                l.append(lc)
                pressed.append(lc)
            lc = 0
        else:
            lc += 1
            if rc > 0:
                r.append(rc)
                pressed.append(rc)
            rc = 0
    l.append(lc)
    pressed.append(lc)

    rlim = []
    llim = []
    for rlen, llen in zip(r, l):
        llim.append(roundup_div(llen, 2) + rlen // 2)
        rlim.append(llen // 2 + roundup_div(rlen, 2))

    is_R = True
    ans = []
    ri, li = 0, 0
    for con in pressed:
        if is_R:
            for _ in range(con - 1):
                ans.append(0)
            ans.append(rlim[ri])
            ri += 1
        else:
            ans.append(llim[li])
            li += 1
            for _ in range(con - 1):
                ans.append(0)
        is_R = not is_R

    return " ".join(map(str, ans))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    ans = solve(S)
    if ans is not None:
        print(ans)


if __name__ == '__main__':
    main()
