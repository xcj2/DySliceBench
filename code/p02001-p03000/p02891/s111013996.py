def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))



S=one_str()
K=one_int()

before = S[0]
count=1
ranrength = []
for i in S[1:]:
    if before==i:
        count+=1
    else:
        ranrength.append(count)
        count=1
    before=i

ranrength.append(count)

output_count=0
for r in ranrength:
    if r>1:
        output_count += r//2
output_count *= K

if S[0]==S[-1]:
    head=ranrength[0]
    tail=ranrength[-1]
    
    if head>1 and head%2==1 and tail>1 and tail%2==1:
        output_count += (K-1)

if len(ranrength)==1:
    print(ranrength[0]*K//2)
else:
    print(output_count)