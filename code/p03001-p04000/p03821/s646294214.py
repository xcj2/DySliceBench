# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_c
 
import sys
# sys.setrecursionlimit(100000)
 
 
def input():
    return sys.stdin.readline().strip()
 
 
def input_int():
    return int(input())
 
 
def input_int_list():
    return [int(i) for i in input().split()]
 
 
def main():
    n = int(input())
    A = []
    B = []
    for _ in range(n):
        a, b = input_int_list()
        A.append(a)
        B.append(b)
 
    cnt = 0
    for a, b in zip(A[::-1], B[::-1]):
        tmp = (a + cnt) % b
        if tmp != 0:
            cnt += b - tmp
    print(cnt)
 
 
if __name__ == "__main__":
    main()