# ALDS1_5_A.

def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def binary_search(S, k):
    a = 0; b = len(S) - 1
    if b == 0: return S[0] == k
    while b - a > 1:
        c = (a + b) // 2
        if k <= S[c]: b = c
        else: a = c
    return S[a] == k or S[b] == k

def show(a):
    # 配列aの中身を出力する。
    _str = ""
    for i in range(len(a) - 1): _str += str(a[i]) + " "
    _str += str(a[len(a) - 1])
    print(_str)

def main():
    n = int(input())
    A = intinput()
    q = int(input())
    m = intinput()
    # 配列Aの作る数を調べる。
    nCanMake = [0]
    for i in range(n):
        for k in range(len(nCanMake)):
            x = nCanMake[k] + A[i]
            if not x in nCanMake: nCanMake.append(x)
    # show(nCanMake)
    for i in range(q):
        if m[i] in nCanMake: print("yes")
        else: print("no")

if __name__ == "__main__":
    main()
