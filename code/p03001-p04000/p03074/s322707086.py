# -*- coding: utf-8 -*-

from sys import stdin

def indexing(s):
    index = []
    one_counter = 0
    zero_counter = 0

    for x in s:
        if x == '1':
            one_counter += 1
            if zero_counter > 0:
                index.append(zero_counter)
                zero_counter = 0
        else:
            zero_counter += 1
            if one_counter > 0:
                index.append(one_counter)
                one_counter = 0

    if zero_counter > 0:
        index.append(zero_counter)
    elif one_counter > 0:
        index.append(one_counter)

    return index

def calc(k, s):
    nums = indexing(s)
    _max = -1
    first = 0

    if s[0] == '0':
        _max = sum(nums[:k*2])
        nums = nums[1:]
    
    if s[-1] == '0':
        last = sum(nums[-k*2:])
        _max = max(last, _max)
        nums = nums[:-1]

    _range = k*2+1

    last = sum(nums[:_range])
    _max = max(last, _max)

    for i in range(_range, len(nums), 2):
        delete = sum(nums[i-_range:i+2-_range])
        add    = sum(nums[i:i+2])
        curr = last + add - delete

        _max = max(_max, curr, last)
        last = curr

    return _max

def main():
    n,k = [int(x) for x in stdin.readline().split()]
    s = stdin.readline().rstrip()
    ans = calc(k, s)
    print(ans)
    
if __name__=='__main__':
    main()