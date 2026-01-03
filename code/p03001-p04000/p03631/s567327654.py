import math
def p(d): print(d)
def i(): return input()

def LI():  # Line Integer
    # 1行 1つの数字
    return int(input())
def LIS():  # Line IntegerS
    # 1行 mつの数字
    return [int(x) for x in input().split()]
def MLIS(n):  # Multi Line IntegerS
    # n行 mつの数字
    return [[int(x) for x in input().split()] for y in range(n)]
def LC():  # Line Character
    # 1行 1つの文字
    return input()
def LCS(): # Line CharacterS
    # 1行 nつの文字
    return [x for x in input().split()]
def MLCS(n): # Multi Line CharacterS
    # n行 mつの数字
    return [[x for x in input().split()] for y in range(n)]

def alp2int(alphabet):
    # アルファベットの番号を返す
    return ord(alphabet) - ord('a')
def int2alp(num):
    # 番号からアルファベットを返す
    return chr(num + ord('a'))
def cnt2dic(lst, dic={}):
    # 同じものをカウントして辞書型にする
    for x in lst:
        key = str(x)
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
    return dic
def dic2lst(dic, key=lambda x:x[1]):
    # 辞書をタプルの配列にする
    return sorted(list(dic.items()), key=key);

def A():
    a = LC()
    if a[0] == a[2]:
        print('Yes')
    else:
        print('No')

def B():
    pass

def C():
    pass

def D():
    pass

def E():
    pass

def F():
    pass

def G():
    pass

def H():
    pass

A()
