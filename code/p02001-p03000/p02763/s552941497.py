def update(BIT,index,letter,value):
    while index < len(BIT):
        BIT[index][letter] += value
        index += index&-index

def sumQuery(BIT,index):
    letters = [0]*26
    while index > 0:
        for i in range(26):
            letters[i] += BIT[index][i]

        index -= index&-index

    return letters

def rangeQuery(BIT,l,r,ans):
    right = sumQuery(BIT,r)
    left = sumQuery(BIT,l-1)
    count = 0
    for i in range(26):
        right[i] -= left[i]
        if right[i] > 0:
            count += 1

    ans.append(count)

def main():
    n = int(input())
    s = list(input())
    q = int(input())
    BIT = [[0 for i in range(26)] for j in range(n+1)]
    ans = []

    for i in range(n):
        update(BIT,i+1,ord(s[i])-ord('a'),1)

    for i in range(q):
        query,index,c = map(str,input().split())
        query = int(query)
        if query == 1:
            index = int(index)
            update(BIT,index,ord(s[index-1])-ord('a'),-1)
            s[index-1] = c
            update(BIT,index,ord(s[index-1])-ord('a'),1)
        else:
            l,r = int(index),int(c)
            rangeQuery(BIT,l,r,ans)

    for i in ans:
        print(i)


main()
