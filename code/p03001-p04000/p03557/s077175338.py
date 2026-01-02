#import generator


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

"""
with open('generator.txt', 'r') as f:
    read = f.read().split('\n')
    N = int(read[0])
    A = list(map(int, read[1].split()))
    B = list(map(int, read[2].split()))
    C = list(map(int, read[3].split()))
"""
A.sort()
C.sort()


def binary_search(lst, value, high):
    l = 0
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if lst[mid] < value:
            l = mid + 1
        elif lst[mid] > value:
            r = mid - 1
        else:
            # lstの中にある場合
            if high:
                # 真に大きい
                return binary_search(lst, value + 0.5, high)
            else:
                # 真に小さい
                return binary_search(lst, value - 0.5, high)
    if high:
        return l
    else:
        return r


def main():
    ans = 0
    # Bの値でループしてそれより小さいA、大きいCの個数を求めて掛け合わせる
    for middle in B:
        lower = binary_search(A, middle, False) + 1 # 0-indexedで返るので+1する
        higher = N - binary_search(C, middle, True)
        ans += lower * higher
    print(ans)

    
# 愚直解
def main2():
    ans = 0
    for a in A:
        for b in B:
            for c in C:
                if a < b < c:
                    ans += 1
    print(ans)
    

if __name__ == "__main__":
    main()
    #main2()