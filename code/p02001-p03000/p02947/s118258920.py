# -*- coding: utf-8 -*-

import sys

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
        n = int(lines[0])
        for i in range(n):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        n = int(lines[0])

    s = lines[1:]

    return (n, s)


def cnt_dict_to_tuple(cnt_dict):
    t = (
        cnt_dict.get("a", 0),
        cnt_dict.get("b", 0),
        cnt_dict.get("c", 0),
        cnt_dict.get("d", 0),
        cnt_dict.get("e", 0),
        cnt_dict.get("f", 0),
        cnt_dict.get("g", 0),
        cnt_dict.get("h", 0),
        cnt_dict.get("i", 0),
        cnt_dict.get("j", 0),
        cnt_dict.get("k", 0),
        cnt_dict.get("l", 0),
        cnt_dict.get("m", 0),
        cnt_dict.get("n", 0),
        cnt_dict.get("o", 0),
        cnt_dict.get("p", 0),
        cnt_dict.get("q", 0),
        cnt_dict.get("r", 0),
        cnt_dict.get("s", 0),
        cnt_dict.get("t", 0),
        cnt_dict.get("u", 0),
        cnt_dict.get("v", 0),
        cnt_dict.get("w", 0),
        cnt_dict.get("x", 0),
        cnt_dict.get("y", 0),
        cnt_dict.get("z", 0),
    )
    return t



def solve(n, s):

    cnt_tuple_dict = dict()
    for i in range(n):
        cnt_dict = dict()    
        for c in s[i]:
            cnt = cnt_dict.get(c, 0)
            cnt = cnt + 1
            cnt_dict[c] = cnt
    
        t = cnt_dict_to_tuple(cnt_dict)
        if debug:
            log("t=%s" % str(t))

        same_cnt_index_list = cnt_tuple_dict.get(t, [])
        same_cnt_index_list.append(i)
        cnt_tuple_dict[t] = same_cnt_index_list


    result = 0
    for t, same_cnt_index_list in cnt_tuple_dict.items():
        n = len(same_cnt_index_list)

        result = result + int(n*(n-1)/2)

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
	