# ALDS_2_A.
# バブルソート。
from math import sqrt, floor

def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def show(a):
    # 配列の中身を出力する。
    _str = ""
    for i in range(len(a) - 1):
        _str += str(a[i]) + " "
    _str += str(a[len(a) - 1])
    print(_str)

def bubble_sort(a):
    # aをバブルソートする(交換回数をreturnする)。
    count = 0
    for i in range(1, len(a)):
        k = i - 1
        while k >= 0:
            # a[i]を前の数と交換していき、前の方が小さかったら止める。
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
                count += 1
            else: break
            k -= 1
    return count

def main():
    N = int(input())
    A = intinput()
    count = bubble_sort(A)
    show(A); print(count)

if __name__ == "__main__":
    main()
