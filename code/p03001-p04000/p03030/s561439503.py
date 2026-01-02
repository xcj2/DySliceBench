import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    N = sc.intarr()[0]
    data = []
    for i in range(N):
        city, score = input().split()
        d = {'index': i+1, 'city': city, 'score': int(score)}
        data.append(d)
    tmp = sorted(data, key=lambda x: x['score'], reverse=True)
    sorted_data = sorted(tmp, key=lambda x: x['city'])

    for d in sorted_data:
        print(d['index'])


class Scan():

    def intarr(self):
        num_array = list(map(int, input().split()))
        return num_array

    def intarr_ver(self, n):
        return [int(input()) for _ in range(n)]

    def strarr(self):
        line = input()
        array = line.split(' ')
        array[-1] = array[-1].strip('\n')
        return array


def display(array):
    for a in range(len(array)):
        if len(array) - a != 1:
            print(array[a], end=' ')
        else:
            print(array[a])


def gcd(a, b):  # 最大公約数
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):  # 最小公倍数
    return a * b // gcd(a, b)


main()
