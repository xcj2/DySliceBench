N = int(input())
S = input()
# . = しろ
# # = 黒
# #の横に.がないようにしたい
# #の横に.があったら#を.に変える
# or #の横に.があったら.を#に変える

# when do you replace now char to .
# 

# テストケース
"""
3
#..

3
##.
"""
# => .....# = 2

def inorderReplace(S , N): 
    S = list(S)
    cnt = 0
    for i in range(N - 1) : 
        nowChar = S[i]
        nextChar = S[i + 1]
        if nowChar == "#" and nextChar == "." : 
            cnt += 1
            S[i + 1] = "#"
    return cnt

def calcCount(S , N) : 
    countingChar = S[0]
    rst = []
    count = 1
    for s in S[1:] :
        if countingChar == s : 
            count += 1
        else : 
            rst.append((countingChar , count))
            count = 1
            countingChar = s
    rst.append((countingChar , count))
    return rst

def countRightChange(countingList) : 
    #全部を.に変えるコスト
    cnt = 0
    for elem in countingList : 
        if elem[0] == "#" : 
            cnt += elem[1]
    return cnt

def countLeftChange(countingList) : 
    # 全部を#に変えるコスト
    cnt = 0
    for elem in countingList : 
        if elem[0] == "." : 
            cnt += elem[1]
    return cnt

def calcPoint(countingList) : 
    a = 0
    b = countLeftChange(countingList)
    minVal = a + b
    for i in range(len(countingList)) : 
        elem = countingList[i]
        if elem[0] == "." : 
            a += 0
            b -= elem[1]
        elif elem[0] == "#" : 
            a += elem[1]
            b -= 0
        if minVal > a + b : 
            minVal = a + b
    return minVal

countingList = calcCount(S , N)
cnt2 = calcPoint(countingList)

print(cnt2)