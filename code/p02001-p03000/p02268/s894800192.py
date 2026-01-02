# ALDS1_4_B.
# バイナリサーチ。

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
    
def main():
    n = int(input())
    S = intinput()
    q = int(input())
    T = intinput()
    count = 0
    for k in T:
        if binary_search(S, k): count += 1
    print(count)

    
if __name__ == "__main__":
    main()
