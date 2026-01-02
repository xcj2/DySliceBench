# -*- coding: utf-8 -*-

import sys
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
        # for line in sys.stdin:
        #     lines.append(line)
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
    
    k = int(lines[0])

    return (k, )


def solve(k):

    nums = [str(e) for e in range(1, 10)]

    def find(found):
        new_found = []
        for f in found:
            last_num = int(f[-1])

            if last_num == 0:
                new_found.append(f + str(last_num ))
                new_found.append(f + str(last_num + 1))
            elif 1 <= last_num and last_num <= 8:
                new_found.append(f + str(last_num - 1))
                new_found.append(f + str(last_num ))
                new_found.append(f + str(last_num + 1))
            elif last_num == 9:
                new_found.append(f + str(last_num - 1))
                new_found.append(f + str(last_num ))
        
        
        cnt = len(found) + len(new_found)
        if cnt < k:
            total_found = found + find(new_found)
        else:
            total_found = found + new_found
            
        return total_found

    total_found = find(nums)
    total_found_as_int = [int(e) for e in total_found]
    total_found_as_int.sort()

    result = total_found_as_int[k-1]
    
    return result

def main():
    # 出力
    new_found = solve(*parse_input())
    if isinstance(new_found, list):
        for r in new_found:
            print("%s" % r, sep='')
    else:
        print("%s" % new_found, sep='')

if __name__ == '__main__':

    main()