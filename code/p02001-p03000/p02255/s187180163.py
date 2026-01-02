# ALDS_1_A.

def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def show(a):
    # 配列aの中身を出力する。
    _str = ""
    for i in range(len(a) - 1): _str += str(a[i]) + " "
    _str += str(a[len(a) - 1])
    print(_str)

def main():
    n = int(input())
    a = intinput()
    # a[0]から順に、挿入していく。
    for i in range(n):
        # a[i]を順次前の数とswapしていき、
        # 前の数の方が大きくなかったら止める。
        cur = i
        while cur > 0:
            if a[cur - 1] > a[cur]:
                a[cur - 1], a[cur] = a[cur], a[cur - 1]
            else: break
            cur -= 1
        show(a)

if __name__ == "__main__":
    main()
