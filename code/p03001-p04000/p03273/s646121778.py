def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

import numpy as np

H,W=two_int()



output = []
for i in range(H):
    row = list(one_str())

    temp = list(set(row))
    if temp[0]=="." and len(temp)==1:
        continue
    
    output.append(row)

output = np.asarray(output).T



fin=[]
for row in output:
    temp = list(set(row))
    if temp[0]=="." and len(temp)==1:
        continue
    
    fin.append(row)
output = np.asarray(fin).T


for row in output:
    print("".join(row))