import sys

def extractMax(A):
    x = A[0]
    A[0] = A[-1]
    A.pop()
    H = len(A)
    i = 0
    while i < H: # ???????????????
        v = A[i]
        rv = 0
        lv = 0
        r = (i+1) * 2
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

def insert(A, n):
    i = len(A)
    A.append(n)
    while i > 0: # ???????????????
        p = int((i + 1) / 2) - 1
        v = A[i]
        pv = A[p]
        if pv < v: # ???????????§??????
            A[p] = v
            A[i] = pv
            i = p
        else:
            break

def main():
    """ ????????? """
    istr = sys.stdin.read()
    cmds = list(istr.splitlines())

    end = False
    S = []
    for cmd in cmds: # input()
#        print("cmd:{} S:{}".format(cmd,S))
        if cmd[0] == "i":
            insert(S,int(cmd[7:]))

        elif cmd == "extract":
            a = extractMax(S)
            print(a)

        elif cmd == "end":
            end = True
            break


if __name__ == '__main__':
    main()