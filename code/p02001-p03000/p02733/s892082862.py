from collections import defaultdict
h,w,k = map(int,input().split())

s = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    s[i] = [int(s) for s in list(input())]

#入力終了

def num_to_g(num):
    #10進数から2進数に変換し、縦向きのグループ分けをする(num < 2**(h-1))
    g_index = {}
    index = 1
    for i in range(h+1):
        g_index[i] = index
        bl = (num>>i)%2
        if(bl == 1):
            index += 1
    
    return g_index
    


def get_white(choco_tmp,w,group_num):
    
    for i in range(h):
        if(s[i][w]==1):
            choco_tmp[group_num[i]] += 1
    
    return choco_tmp


def greedy(num):
    div = num_to_g(i)
    res = max(div.values())-1
    choco = defaultdict(int)
    for j in range(w):
        choco = get_white(choco,j,div)
        
        if any(c>k for c in choco.values()):
            choco = defaultdict(int)
            choco = get_white(choco,j,div)
            
            if any(c>k for c in choco.values()):
                return 10**9 + 1
            else:
                res += 1
       
    return res        
            
                
        
#print(greedy(2))

mx = 2**(h-1)                
ans = h+w-1
for i in range(mx):
    ans = min(ans,greedy(i))

print(ans)
