# -*- coding: utf-8 -*-

def parse_input():

    # 出力
    nm = input().split(" ")
    n = int(nm[0])
    m = int(nm[1])

    rows = []
    for i in range(0, n):
        rows.append([int(e) for e in input().split(" ")])

    return (n, m, rows)

def solve(n, m, rows):

    result = []
    for k in range(1, m + 1):
        tmp = []
        for i in range(0, n):
#            print(rows[i])
            r = rows[i]
#            print(r[1:r[0] + 1])
            if k in r[1:r[0]+1]:
               tmp.append(i+1)
        if len(tmp) == n:
            result.append(k)

    return str(len(result))

def main():

    n, m, rows = parse_input()
    print(solve(n, m, rows))

if __name__ == '__main__':

    main()
