SEG_LEN = 1 << 18

seg = [0 for i in range(2*SEG_LEN)]

def add(ind, v):
    ind += SEG_LEN
    seg[ind] += v
    while True:
        ind //= 2
        if ind == 0:
            break
        seg[ind] = seg[ind*2] + seg[ind*2+1]

def sum(l, r):
    l += SEG_LEN
    r += SEG_LEN
    ans = 0
    while l < r:
        if (l % 2 == 1):
            ans += seg[l]
            l += 1
        l //= 2
        if r % 2 == 1:
            ans += seg[r-1]
            r -= 1
        r //= 2
    return ans


def main():
    n, q = map(int, input().split())
    ans = []
    for i in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            add(x, y)
        elif com == 1:
            ans.append(sum(x, y+1))
    for i in range(len(ans)):
        print(ans[i])

    

if __name__ == '__main__':
    main()
