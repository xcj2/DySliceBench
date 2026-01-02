# -*- coding: utf-8 -*-

import math

debug = False

def log(text):
    if debug:
        print(text)

def parse_input(lines_as_string = None):

    global debug
    lines = []
    if lines_as_string is None:
        debug = False
        lines.append(input())
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]    


    token = lines[0].split(" ")
    n = int(token[0])
    
    a = [int(e) for e in lines[1].split(" ")]
    
    return (n, a)


def solve(n, a):


    current_max = -1
    result = "Yes"
    reduced_all = set()
    last_j = 0
    for i in range(n):

        if a[i] >= current_max:
            current_max = a[i]
        else:
            reduced_tmp = set()
            for j in range(last_j, i):
                if a[j] == current_max:
                    if j in reduced_all:
                        result = "No"
                        break
                    else:
                        reduced_tmp.add(j)

            if result == "No":
                break

            current_max = current_max - 1
            for j in reduced_tmp:
                reduced_all.add(j)
                a[j] = a[j] - 1
                if a[j] > a[i]:
                    result = "No"
                    break
                else:
                    last_j = max(j, last_j)


            if result == "No":
                break

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))


if __name__ == '__main__':

    main()
