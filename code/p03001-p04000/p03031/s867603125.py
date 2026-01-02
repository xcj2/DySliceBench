#	!/usr/bin/env python3
#	encoding: UTF-8
#	Modified: <26/May/2019 07:02:39 PM>


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology (IIIT), Gwalior


import sys


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline().strip()


def binary(n):
    global length
    op = []
    bit = 1 << length - 1
    while (bit):
        if n & bit == 0:
            op.append(0)
        else:
            op.append(1)
        bit >>= 1
    return op


def main():
    global length
    length, m = get_ints()
    d = {}
    for i in range(m):
        tmp = get_array()
        d[i] = tmp[1:]
    p = get_array()
    ans = 0
    x = 1 << length
    combinations = []
    for i in range(x):
        combinations.append(binary(i))

    for i in combinations:
        flag = True
        for j in range(m):
            cnt = 0
            for k in d[j]:
                if i[k - 1] == 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
                break
        if flag == True:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
