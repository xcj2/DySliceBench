#coding:utf-8
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

def search_banpei(array, target, cnt):
    tmp = array[len(array)-1]
    array[len(array)-1] = target

    n = 0
    while array[n] != target:
        n += 1

    array[len(array)-1] = tmp
    if n < len(array) - 1 or target == tmp:
        cnt += 1
    return cnt        

def linear_search():  
    cnt = 0
    for t in T:
        for s in S:
            if t == s:
                cnt += 1
                break

def linear_banpei_search():
    cnt = 0
    for target in T:
        cnt = search_banpei(S, target, cnt)
    return cnt

cnt = linear_banpei_search()

print(cnt)

