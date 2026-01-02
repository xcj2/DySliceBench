#coding: utf-8
# C: String Coloering
from collections import Counter
from itertools import product

def getLeft(in_string, N):
    return in_string[:N]

def getRight(in_string, N):
    return in_string[2*N-1:N-1:-1]

def getDict(left_seq):
    tmp_n = len(left_seq)
    r_dict = Counter()
    for bit in product(range(2), repeat=tmp_n):
        red_left = ""
        blue_left = ""
        for i in range(tmp_n):
            if bit[i]:
                red_left += left_seq[i]
            else:
                blue_left += left_seq[i]
        r_dict[red_left + "-" + blue_left] += 1
    return r_dict

def getMatch(left, right):
    res = 0
    for i in left.keys():
        res += left[i]*right[i]
        
    return res

if __name__ == "__main__":
    N = int(input())
    Seq = input()
    print(getMatch(getDict(getLeft(Seq, N)), getDict(getRight(Seq, N))))
       
