import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    data = sc.strarr()
    stack = []
    for d in data:
        if d == '+':
            stack.append(stack.pop() + stack.pop())
        elif d == '-':
            stack.append(((-1) * stack.pop()) + stack.pop())
        elif d == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(d))
    print(stack[0])


class Scan():

    def intarr(self):
        line = input()
        array = line.split(' ')
        num_array = [int(n) for n in array]
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


main()

