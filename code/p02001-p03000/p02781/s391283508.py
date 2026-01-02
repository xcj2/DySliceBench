mod = 10**9 + 7
from collections import deque

def main():
    N = iip(False)
    K = iip(False)
    ret = solve(N, K)
    print(ret)

def solve(N, K):

    strn = str(N)

    A = []
    B = []

    for i in range(len(strn), 0, -1):
        if strn[len(strn)-i] != "0":
            A.append(int(strn[len(strn)-i]))
            B.append(i)


    if K == 1:
        return 9*(B[0]-1) + A[0]


    if K == 2:
        if len(strn) < 2:
            return 0
        ret = 0
        ret += (B[0]-1) * (B[0]-2) // 2 * (9**2) #桁数がmaxじゃない場合
        ret += (A[0]-1) * 9 * (B[0]-1) #桁数がmaxで先頭桁がmax以外の場合
        if len(B) >= 2 and len(A) >= 2:
            ret += (B[1]-1) * 9 + A[1] #先頭桁がmaxの場合
        return ret

    ret = 0
    ret += (B[0] - 1) * (B[0] - 2) * (B[0] - 3) // 6 * 9**3 #桁数がmaxじゃない場合
    ret += (A[0] - 1) * (B[0] - 1) * (B[0] - 2) // 2 * 9**2 #桁数がmaxで先頭桁がmaxじゃない場合

    #以下、桁数はmaxで先頭桁はmaxとする
    if len(strn) < 3:
        return 0
    if len(B) >= 2:
        ret += (B[1]-1) * (B[1]-2) // 2 * 9**2 #有効2桁目の桁数がmaxじゃない場合
    if len(B) >= 2 and len(A) >= 2:
        ret += (A[1] - 1) * (B[1]-1) * 9 #有効2桁目の桁数がmaxで数字がmaxじゃない場合
    if len(B) >= 3 and len(A) >= 3:
        ret += (B[2] - 1) * 9 + A[2] #有効2桁目,3桁目がmaxの場合
    return ret


#####################################################ライブラリ集ここから

def split_print_space(s):
    print(" ".join([str(i) for i in s]))

def split_print_enter(s):
    print("\n".join([str(i) for i in s]))


def searchsorted(sorted_list, n, side):
    if side not in ["right", "left"]:
        raise Exception("sideはrightかleftで指定してください")

    l = 0
    r = len(sorted_list)

    if n > sorted_list[-1]:
        #print(sorted_list)
        return len(sorted_list)
    if n < sorted_list[0]:
        return 0

    while r-l > 1:
        x = (l+r)//2
        if sorted_list[x] > n:
            r = x
        elif sorted_list[x] < n:
            l = x
        else:
            if side == "left":
                r = x
            elif side == "right":
                l = x

    if side == "left":
        if sorted_list[l] == n:
            return r - 1
        else:
            return r

    if side == "right":
        if sorted_list[l] == n:
            return l + 1
        else:
            return l


def iip(listed):
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


if __name__ == "__main__":
    main()