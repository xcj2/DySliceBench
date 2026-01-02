from collections import defaultdict
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

def main():
    num = int(input())
    data = [list(map(int, input().split())) for i in range(num)]
    data.sort(key=lambda x: x[1])
    now_time = 0

    flg = 1
    for i in range(num):
        if now_time + data[i][0] <= data[i][1]:
            now_time += data[i][0]
        else:
            flg = 0
            break
    if flg:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()

