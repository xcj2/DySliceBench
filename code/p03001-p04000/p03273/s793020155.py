#!/usr/bin/env python
# coding: utf-8
#

import copy

def check_w(in_l):
    l = copy.deepcopy(in_l)
    for i in range(len(l)):
        line = list(l[i])
        # print(line)
        if '#' not in line:
            # print('del')
            del l[i]
            return l, True
    return l, False


def check_h(in_l):
    l = copy.deepcopy(in_l)
    # 文字数確認
    
    for i in range(len(l[0])):
        line = [ l[j][i:i+1] for j in range(len(l))]
        # print(line)
        if '#' not in line:
            ret = []
            # print(line)
            for j in range(len(l)):
                ret.append(l[j][:i] + l[j][i+1:])
            return ret, True
    return l, False
            
    
def main(in_l):
    l = copy.deepcopy(in_l)
    flg = True
    # print(l)
    
    while flg:
        # print(l)
        ret_l, ret_f = check_w(l)
        if ret_f:
            l = ret_l
            flg = True
            continue
        else:
            flg = False

        ret_l, ret_f = check_h(l)
        if ret_f:
            l = ret_l
            flg = True
            continue
        else:
            flg = False

    # 出力
    for line in l:
        print('{}'.format(line))
    
    
if __name__ == '__main__':
    try:
        h, w = list(map(int,input().strip().split(" ")))
        l = []
        for _ in range(h):
            l.append(input().strip())
        main(l)
    except EOFError:
        pass
