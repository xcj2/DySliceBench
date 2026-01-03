# すべてを str型として読み込み、Kのみ int型に変換
N, Kstr = map(str, input().split()) # N: 元の数, K: NG数の数
K = int(Kstr)
D = list(map(str, input().split())) # D: NG数のリスト

# N = str(1000)
# K = 8
# D = ('1', '3', '4', '5', '6', '7', '8', '9')

def getMinimumOK():
# NGではない最小の数字を求める
    for i in range(0, 9):
        for j in range(1, K):
            if D[j - 1] == str(i):
                break
            else:
                return str(i)

def getFirstNG():
# Nの中の最初のNG数までの文字数を返す
# getFirstNG()を呼ぶ前にisOK(N)を呼んでいるので N の中に NG数 が必ず有る
    for i in range(0, len(N)):
        for ng in D:
            if ng == N[i]:
                return i + 1

def isOK(number):
# NG数が含まれなければ True, 含まれていれば False を返す
    strNumber = str(number)
    strlen = len(strNumber)
    for i in range(strlen):
        if strNumber[i] in D: # i桁目の数が D の中にあれば
            return False      # number に NG数 が含まれる
    return True

def makeUpperHalf(upperHalf_org):
# 引数：最初のNG数より上位の桁の数（str型）
# 戻り値：NG数を含まない上位の数（str型）
    numUpper = int(upperHalf_org)
    while True:
        numUpper += 1
        if isOK(numUpper): # NG数が無くなるまで numUpper を増やしていく
            break
    return str(numUpper)

if isOK(int(N)): # N に　NG数 が含まれていなければ
    print(N)     # N を表示して終了
else:
    minimumOK = getMinimumOK() # 最小のOK数字（文字列型）
    firstNG = getFirstNG()     # 上位から数えて最初のNG数が出てくる桁

    upperHalf = N[:firstNG] # 先頭から最初のNG数まで
    lowerHalf = N[firstNG:] # 最初のNG数の次から末尾まで
    upper = makeUpperHalf(upperHalf)
    lower = minimumOK * len(lowerHalf) # 下半分はNGでない最小の数を桁数分、並べる
    print(upper + lower)
