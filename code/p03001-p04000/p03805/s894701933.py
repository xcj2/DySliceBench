#import time
N, M = map(int, input().split())

#動くことのできる経路とその逆向きの移動をリストにし、それをリストにしたもの
lst = []
for i in range(M):
    a = list(map(int, input().split()))
    lst += [a] + [a[::-1]]

def next_permutation(L): #リストを順列で並び替える部分
    i = N - 2
    while i >= 0 and L[i] > L[i+1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < N and L[i] < L[j]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = N - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True

#1-->Nまでの整数が順に並んでいるリスト、このリストの順番にたどるとする
L = [i+1 for i in range(N)]
#print ('作成したL', L)

def judge(L): #ある経路Lが与えられたときに、その移動がリスト内の移動法で可能かどうかを判定、可能-->True 不可-->Falseを返す
    for i in range(N-1):
        if not L[i:i+2] in lst:
#            print ('L[i:i+2]=', L[i:i+2])
            return False
    return True


def roop(L): #全判定する部分
    count = 0
    while True:
        #順路が条件を満たすか判定する部分
#        print ('ループ内L', L)
#        time.sleep(3)
        if L[0] != 1: #並び替えた後に最初が1ではない-->パスが1から始まらず条件を満たさない
            print (count)
            break
        if judge(L):
            count += 1
        if not next_permutation(L):
            print (count)
            break
    return 'error'
#print ('lst = ',lst)
roop(L)