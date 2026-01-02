# -*- coding: utf-8 -*-

import sys

def parse_input(lines_as_string = None):


    lines = []
    if lines_as_string is None:
        lines.append(input())
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    tokens = lines[0].split(" ")
    s = tokens[0]

    return (s,)


def solve(s):

    m = 0
    for ss_length in range(len(s) + 1):
        for i in range(len(s)):
            if i+ss_length > len(s):
                break

            ss = s[i:i+ss_length]
#            print("ss=%s" % ss)
            count = 0
            for c in ss:
                if c in "ACGT":
                    count = count + 1
            if count == ss_length and m < ss_length:
                m = ss_length
                break


    return m

def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
