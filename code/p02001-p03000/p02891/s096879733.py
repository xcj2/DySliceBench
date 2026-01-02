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
        # for line in sys.stdin:
        #     lines.append(line)
        lines.append(input())
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    s = lines[0]
    k = int(lines[1])

    return (s, k)


def solve(s, k):

    compress = []
    previous_c = None
    cnt = 1
    for c in s:
        if c == previous_c:
            cnt = cnt + 1
        else:
            if previous_c:
                compress.append((previous_c, cnt))
                cnt = 1
        previous_c = c
    compress.append((previous_c, cnt))
    if debug:
        log("compress=%s" % compress)

    if len(compress) == 1:
        return compress[0][1] * k // 2
    elif len(compress) == 2:
        return (compress[0][1] // 2 + compress[1][1] // 2) * k
        
    head = compress[0]
    if len(compress) > 1:
        body = compress[1:-1]
    else:
        body = []
    tail = compress[-1]
    if debug:
        log("head=%s" % (head,))
        log("body=%s" % (body,))
        log("tail=%s" % (tail,))
    
    body_count = 0 
    for b in body:
        body_count = body_count + b[1] // 2

    total_replace_count = 0
    if head[0] == tail[0]:
        length = head[1] + tail[1]
        replace_count = length // 2 * (k-1)
        total_replace_count = total_replace_count + head[1] // 2 + replace_count + tail[1] // 2
        total_replace_count = total_replace_count + body_count * k
    else:
        total_replace_count = total_replace_count + (head[1] // 2 + body_count + tail[1] // 2) * k

    return total_replace_count


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        for r in result:
            print("%s" % r, sep='')
    else:
        print("%s" % result, sep='')

if __name__ == '__main__':

    main()
	