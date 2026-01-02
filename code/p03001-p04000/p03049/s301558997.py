#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()

    words = []
    starts_with_B = 0
    end_with_A = 0
    contain_AB = 0
    starts_with_B_and_end_with_A = 0
    for i in range(N):
        word = input()
        words.append(word)
        contain_AB += len(word) - len(word.replace("AB", "_"))

        if word[0] == "B" and word[-1] == "A":
            starts_with_B_and_end_with_A += 1
        elif word[0] == "B":
            starts_with_B += 1
        elif word[-1] == "A":
            end_with_A += 1

    if starts_with_B_and_end_with_A == 0:
        print(contain_AB + min(starts_with_B, end_with_A))
        return
    if starts_with_B + end_with_A == 0:
        print(contain_AB + starts_with_B_and_end_with_A - 1)
        return
    print(contain_AB + starts_with_B_and_end_with_A +
          min(starts_with_B, end_with_A))


main()
