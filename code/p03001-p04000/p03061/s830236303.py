

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    

def gcd_all(lst):
    g = gcd(lst[0], lst[1])
    for e in lst[2:]:
        g = gcd(g, e)
    return g


def submit():
    n = int(input())
    alist = list(map(int, input().split()))

    if n == 2:
        print(max(alist))
    else:
        # 左から計算したgcd列
        gcd_left = [alist[0]]
        for a in alist[1:]:
            gcd_left.append(gcd(gcd_left[-1], a))
        
        # 右から計算したgcd列
        gcd_right = [alist[-1]]
        for a in reversed(alist[:-1]):
            gcd_right.append(gcd(gcd_right[-1], a))
        gcd_right = gcd_right[::-1]

        gcd_max = 0
        for i in range(n):
            if i == 0:
                gcd_i = gcd_right[i + 1]
            elif i == n - 1:
                gcd_i = gcd_left[i - 1]
            else:
                gcd_i = gcd(gcd_left[i - 1], gcd_right[i + 1])

            if gcd_max < gcd_i:
                gcd_max = gcd_i

        print(gcd_max)


if __name__ == "__main__":
    submit()
