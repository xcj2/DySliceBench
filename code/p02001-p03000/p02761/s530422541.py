def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N,M = input_int()

data = []
for i in range(M):
    s,c = input_int()
    data.append([s,c])

def solve(N, data):
    mins = 100000000000
    for i in range(10**N):

        temp = str(i)
        flg = True
        if len(temp)==N:
            for d in data:
                if temp[d[0]-1] != str(d[1]):
                    flg = False
                    break
            if flg==True:
                return temp
    return -1

output = solve(N,data)
print(output)