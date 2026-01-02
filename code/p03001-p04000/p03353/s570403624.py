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
    # 1行 1つの文字列
    return input()
def LCS(): # Line CharacterS
    # 1行 nつの文字列
    return [x for x in input().split()]
def MLCS(n): # Multi Line CharacterS
    # n行 mつの文字列
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

def unqlst(lst):
    return list(set(lst))

def A():
    a = LC()
    if a[0] == a[2]:
        print('Yes')
    else:
        print('No')

def B():
    a, b, c, d = LIS()
    s = max(a, c)
    e = min(b, d)
    if s < e:
        p(e-s)
    else:
        p(0)

def C():
    N = LI()
    reds = sorted(MLIS(N), key=lambda x:x[0])
    blues = sorted(MLIS(N), key=lambda x:x[0])

    blueF = [False for x in range(N)]

    count = 0

    for i in range(N):
        for j in range(N):
            if blueF[j] == False and reds[i] < blues[j]:
                blueF[j] = True
                count += 1
                break
    print(count)

def D():
    pass

def E():
    s = LC()
    k = LI()
    words = []
    for b in range(len(s)):
        for e in range(1, 6):
            if s[b:b+e] != '':
                words.append(s[b:b+e])
    words = sorted(unqlst(words))
    print(words[k-1])
def F():
    pass

def G():
    pass

def H():
    pass

E()
