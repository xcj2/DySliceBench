def read():
    return int(input())

def reads(sep=None):
    return list(map(int, input().split(sep)))

def main():
    w, h = reads()
    p = sorted([read() for _ in range(w)])[::-1]
    q = sorted([read() for _ in range(h)])[::-1]

    pi = w-1
    qi = h-1
    res = 0
    while 0<=pi and 0<=qi:
        if p[pi] < q[qi]:
            res += p[pi] * (h+1)
            pi -= 1
            w -= 1
        else:
            res += q[qi] * (w+1)
            qi -= 1
            h -= 1
    res += sum(p[:pi+1]) + sum(q[:qi+1])
    print(res)

main()
