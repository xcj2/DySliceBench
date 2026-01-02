n, k = map(int, input().split())

W = []
for _ in range(n):
    w = int(input())
    W.append(w)
    
Baggages = W[:]
        
def _check(tmp_P):
    num_track = 1
    tmp_sum = 0
    for b in Baggages:
        if tmp_sum+b <= tmp_P:
            tmp_sum += b
        else:
            num_track += 1
            tmp_sum = b
            if num_track > k:
                return False
    return True
    

def check(P):
    i = 0
    for _ in range(k):
        s = 0
        while s+Baggages[i] <= P:
            s += Baggages[i]
            i += 1
            if i >= n:
                return True
    if i == n:
        return True
    else:
        return False

    
def binary_search(max_r):
    left = 0
    right = max_r
    
    while right-left > 1:
        mid = (left+right)//2
        if check(mid) == True:
            right = mid
        else:
            left = mid
    return right
            
max_p = sum(Baggages)+1
ans = binary_search(max_p)
print(ans)

#print(check(4))
#print(check(5))
#print(check(6))
#print(check(7))
    
    

    

    

