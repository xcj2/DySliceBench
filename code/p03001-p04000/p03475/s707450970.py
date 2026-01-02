def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N=one_int()

sum_time=0
query = []
for i in range(N-1):
    query.append(many_int())

for i in range(N-1):
    C,S,F=query[i]
    sum_time = C+S

    for j in range(i+1,N-1):
        
        C, S, F =query[j]
        sum_time = max(S, sum_time)
        temp = (sum_time-S)/F
        if temp.is_integer():
            pass
        else:
            temp = int((sum_time-S)//F + 1)
            sum_time = S +temp * F
        sum_time += C
    print(int(sum_time))
print(0)