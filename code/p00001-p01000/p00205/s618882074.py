def check_aiko(arr):
    if all(arr[0] == a for a in arr):
        return True

    rps = [1, 2, 3]
    for t in rps:
        if t not in arr:
            return False

    return True


def check_v(arr):
    rps = {}
    o = []
    for t in arr:
        if t not in rps:
            rps[t] = 0
    if 1 in rps.keys() and 2 in rps.keys():
        rps[1], rps[2] = 1, 2
    elif 2 in rps.keys() and 3 in rps.keys():
        rps[2], rps[3] = 1, 2
    elif 1 in rps.keys() and 3 in rps.keys():
        rps[3], rps[1] = 1, 2

    for n in arr:
        o.append(rps.get(n))
    return o


def algorithm():
    g = []
    out = []

    while True:
        inp = int(input())
        if inp == 0:
            break

        g.append(inp)
        if len(g) == 5:
            if check_aiko(g):
                out = [3] * 5
            else:
                out = check_v(g)

            for o in out:
                print(o)
            g.clear()
            out.clear()


def main():
    algorithm()


if __name__ == '__main__':
    main()