#import sys
#input = sys.stdin.readline
import random
import bisect
#from statistics import mean, median, variance, stdev

#template input

def IT(): #整数1個
    return int(input())
def IL(): #整数複数
    return [int(_) for _ in input().split()]
def IS(): #文字列複数
    return [_ for _ in input().split()]
def ILS(n): #整数1つ　縦にズラーってなってるやつ
    return [int(input()) for _ in range(n)]
def SLS(n): #文字列　縦にズラーってなってるやつ
    return [input() for _ in range(n)]
def ILSS(n): #整数複数　縦にズラーってなってるやつ
    return [[int(_) for _ in input().split()] for j in range(n)]

#template technique
def bit_full_search(ss):
    n = len(ss)
    for i in range(1 << n):
        s = ""
        for j in range(n + 1):
            if ((1 & i >> j) == 1):
                s += ss[j]
        print(s)
def bit_full_search2(A):
    #https://blog.rossywhite.com/2018/08/06/bit-search/
    value = []
    for i in range(1 << len(A)):
        output = []

        for j in range(len(A)):
            if ((i >> j) & 1) == 1:
                #output.append(A[j])
                output.append(A[j])
        value.append([format(i, 'b').zfill(16), sum(output)])

    value.sort(key=lambda x:x[1])
    bin = [value[k][0] for k in range(len(value))]
    val = [value[k][1] for k in range(len(value))]
    return bin, val
def matching_bisect(list1_val, list2_val, n):
    #2分探索
    j = 0
    for i in range(len(list1_val)):
        j = bisect.bisect_left(list2_val, n - list1_val[i])
        if j < len(list2_val):
            if list1_val[i] + list2_val[j] == n:
                #ans = list2_bin[j] + list1_bin[i]
                break
    return j

"""ここからメインコード"""

def main():

    a,b,k = IL()
    c = 0
    for i in range(101, 0, -1):
        if (a)%i == 0 and (b)%i == 0:
            #print(i)
            c += 1
            if c == k:
                print(i)
                break








main()
