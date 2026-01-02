def INT():
    return int(input())

def LI():
    return list(map(int, input().split()))

def MI():
    return map(int, input().split())

N = INT()
h = [0] + LI() + [0]
ans = 0

while not all([h[i] == 0 for i in range(len(h))]):
    min_idx = [idx for idx, flower in enumerate(h) if flower == 0]
    
    for i in range(len(min_idx) - 1):
        idx_1, idx_2 = min_idx[i], min_idx[i + 1]
        if idx_1 + 1 == idx_2:
            continue
        
        min_tall = min(h[idx_1 + 1 : idx_2])
        ans += min_tall
            
        for j in range(idx_1 + 1, idx_2):
            h[j] -= min_tall
        
print(ans)