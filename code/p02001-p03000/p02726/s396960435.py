mod = 10**9 + 7

def iip(listed = False):
    ret = [int(i) for i in input().split()]
    if len(ret) == 1 and not listed:
        return ret[0]
    return ret

def soinsuu_bunkai(n):
    ret = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            n //= i
            ret.append(i)
        if i > n:
            break
    if n != 1:
        ret.append(n)
    return ret


def conbination(n, r, mod, test=False):
    if n <=0:
        return 0
    if r == 0:
        return 1
    if r < 0:
        return 0
    if r == 1:
        return n
    ret = 1
    for i in range(n-r+1, n+1):
        ret *= i
        ret = ret % mod

    bunbo = 1
    for i in range(1, r+1):
        bunbo *= i
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod
    if test:
        #print(f"{n}C{r} = {ret}")
        pass
    return ret


def inv(n, mod):
    return power(n, mod-2)

def power(n, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p//2) ** 2) % mod
    if p % 2 == 1:
        return (n * power(n, p-1)) % mod

#####################################################ライブラリ集ここまで

def main():
    N, X, Y = iip()
    X -= 1
    Y -= 1

    ret = 0

    result = []
    for k in range(1, N):
        ret = 0
        for i in range(N):
            ret += search(i, k, N, X, Y)
        result.append(str(ret))

    print("\n".join(result))

def search(a, k, N, X, Y):
    kouho = []

    if abs(a-X)+1+abs(a+k-Y) >= k and abs(a-Y) + 1 + abs(a+k-X) >= k:
        #print(f"追加 {a+k} a, k = {a}, {k} by 条件1")
        kouho.append(a+k)

    asy = k-abs(a-X)-1
    if asy < 0:
        pass
    elif asy == 0:
        if abs(a-X) + 1 <= abs(a-Y):
            kouho.append(Y)
            #print(f"追加 {Y} a, k = {a}, {k} by 条件6")
    else:
        if abs(a-(Y-asy)) > k:
            kouho.append(Y-asy)
            #print(f"追加 {Y-asy} a, k = {a}, {k} by 条件2")
        if abs(a-(Y+asy)) > k:
            #print(f"追加 {Y+asy} a, k = {a}, {k} by 条件3")
            kouho.append(Y+asy)

    asx = k-abs(a-Y)-1
    if asx < 0:
        pass
    elif asx == 0:
        if abs(a-Y) + 1 < abs(a-X):
            kouho.append(X)
            #print(f"追加 {X} a, k = {a}, {k} by 条件7")
    else:
        if abs(a-(X-asx)) > k:
            kouho.append(X-asx)
            #print(f"追加 {X-asx} a, k = {a}, {k} by 条件4")
        if abs(a-(X+asx)) > k:
            kouho.append(X+asx)
            #print(f"追加 {X+asx} a, k = {a}, {k} by 条件5")

    kakutei = []
    result = 0
    for kh in kouho:
        if kh == a:
            continue
        if kh < 0:
            continue
        if kh > N-1:
            continue
        if kh in kakutei:
            continue
        if kh < a:
            continue
        kakutei.append(kh)
        result += 1
    #print(f"--result開始 a, k = {a}, {k}")
    #print(result)
    #print(kakutei)
    #print("--result終了")
    return result



if __name__ == "__main__":
    main()