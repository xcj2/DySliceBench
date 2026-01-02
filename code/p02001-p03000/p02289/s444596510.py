import sys


def extract_max(A):
    x = A[0]
    A[0] = A[-1]
    A.pop()
    H = len(A)
    i = 0
    while i < H:
        v = A[i]
        rv = 0
        lv = 0
        r = (i + 1) * 2
        l = r - 1
        if l < H:
            lv = A[l]
            if r < H:
                rv = A[r]

        if v < lv and lv > rv:
            A[l] = v
            A[i] = lv
            i = l
        elif v < rv:
            A[r] = v
            A[i] = rv
            i = r
        else:
            break
    return x


def insert(a, n):
    i = len(a)
    a.append(n)
    while i > 0:
        p = int((i + 1) / 2) - 1
        v = a[i]
        pv = a[p]
        if pv < v:
            a[p] = v
            a[i] = pv
            i = p
        else:
            break


def main():
    istr = sys.stdin.read()
    cmds = list(istr.splitlines())
    S = []
    for cmd in cmds:  # input()
        if cmd[0] == "i":
            insert(S, int(cmd[7:]))

        elif cmd == "extract":
            a = extract_max(S)
            print(a)

        elif cmd == "end":
            break


if __name__ == '__main__':
    main()
