def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N=one_int()

alpha =list("abcdefghij")

def dfs(string, counter, N):
    if N==counter:
        lists.append(string)
        return 
    
    for i in range(counter):
        if i==0:
            dfs(string + alpha[i], counter+1, N)
        elif alpha[i-1] in string:
            dfs(string + alpha[i], counter+1, N)

lists = []

dfs("a", 2, N+1)

for i in sorted(lists):
    print(i)