def get_input(inp):
    li = inp.split("\n")

    def inner():
        return li.pop(0)
    return inner

INPUT="""ABCBC"""
input = get_input(INPUT)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))

def main():
    n = int(input())
    if n == 3:
        print(2, 5, 63)
    elif n == 4:
        print(2, 5, 20, 63)
    elif n == 5:
        print(2, 5, 20, 30, 63)
    else:
        sz = 0
        ans = set()
        anss = 0
        i = 0
        while True:
            if sz < n:
                ans.add(6 * i + 2)
                anss += 6 * i + 2
                sz += 1
            else:
                break
            if sz < n:
                ans.add(6 * i + 3)
                anss += 6 * i + 3
                sz += 1
            else:
                break
            if sz < n:
                ans.add(6 * i + 4)
                anss += 6 * i + 4
                sz += 1
            else:
                break
            if sz < n:
                ans.add(6 * i + 6)
                anss += 6 * i + 6
                sz += 1
            else:
                break
            i += 1
        if anss % 6 == 2:
            ans.remove(8)
            ans.add(6 * i + 6)
        elif anss % 6 == 3:
            ans.remove(9)
            ans.add(6 * i + 6)
        elif anss % 6 == 5:
            ans.remove(9)
            ans.add(6 * i + 4)
        for s in ans:
            print(s)


if __name__ == '__main__':
    main()
