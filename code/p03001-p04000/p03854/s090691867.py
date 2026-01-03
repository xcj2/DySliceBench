#!/usr/bin/env python
"""AtCoder Beginner Contest 049: C - 白昼夢 / Daydream
https://atcoder.jp/contests/abc049/tasks/arc065_a
"""

__author__ = 'bugttle <bugttle@gmail.com>'

WORDS = ['dream', 'dreamer', 'erase', 'eraser']


def match_word(S):
    for word in WORDS:
        if S.endswith(word):
            return word
    return None


def check(S):
    while True:
        word = match_word(S)
        if word is None:
            return 'NO'
        S = S[:S.rfind(word)]
        if S == '':
            return 'YES'


def main():
    S = input()
    print(check(S))


if __name__ == '__main__':
    main()
