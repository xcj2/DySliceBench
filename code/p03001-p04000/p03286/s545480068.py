#import sys
#input = sys.stdin.readline
#template input
import bisect

def IT():
    return int(input())
def IL():
    return [int(_) for _ in input().split()]
def SL():
    return [int(_) for _ in input().split()]
def ILS(n):
    return [int(input()) for _ in range(n)]
def SLS(n):
    return [input() for _ in range(n)]
def ILSS(n):
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
    return value


"""ここからメインコード"""
def main():
    n = IT()
    #それぞれ半分全列挙
    list1 = [(-2) **  i for i in range(16)]
    list2 = [(-2) ** (i + 16) for i in range(16)]

    list1 = bit_full_search2(list1)
    list1.sort(key=lambda x:x[1])
    list1_bin = [list1[i][0] for i in range(len(list1))]
    list1_val = [list1[i][1] for i in range(len(list1))]

    list2 = bit_full_search2(list2)
    list2.sort(key=lambda x:x[1])
    list2_bin = [list2[i][0] for i in range(len(list2))]
    list2_val = [list2[i][1] for i in range(len(list2))]
    ans = 0
    for i in range(len(list1_val)):
        j = bisect.bisect_left(list2_val, n - list1_val[i])
        if j < len(list2_val):
            if list1_val[i] + list2_val[j] == n:
                ans = list2_bin[j] +list1_bin[i]
                break
    print(int(ans))
main()

