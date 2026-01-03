#!/usr/bin/python3

import sys

def dprint(*args):
    return
    print(*args)

def solve(s_str):
    ans = 0
    s_len = len(s_str)
    for bits in range(0, 1 << (s_len - 1)):
        dprint("bits: {0:b}".format(bits))
        rev_str = list(reversed(s_str))
        #dprint(f"rev_str: {rev_str}")
        cur_num_rev_str = ""
        # 12345
        for rev_i in range(0, s_len):
            dprint("rev_i: %d" % rev_i)
            plus_index = rev_i
            cur_num_rev_str += rev_str[0]
            rev_str = rev_str[1:]
            dprint("cur_num_rev_str: %s" % cur_num_rev_str)
            if rev_i == s_len - 1 or bits & (1 << plus_index):
                ans += int(''.join(list(reversed(cur_num_rev_str))))
                cur_num_rev_str = ""
    return ans

def main():
    s_str = sys.stdin.read().rstrip()
    dprint(s_str)
    print(solve(s_str))

main()