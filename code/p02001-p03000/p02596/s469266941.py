#create date: 2020-08-02 21:08

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def divisor(n):
    i = 1
    table = [7, ]
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(7*i)
            table.append(n // i)
            table.append((n//i)*7)
        i += 1
    table = set(table)
    return table


def main():
    k = ni()
    a = 0
    for i in range(1, 10**6+1):
        a = (10*a + 7) % k
        if a == 0:
            print(i)
            quit()
    print(-1)

if __name__ == "__main__":
    main()