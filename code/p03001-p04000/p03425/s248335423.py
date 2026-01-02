# ABC 089
def getInt(): return int(input())
def zeros(n): return [0]*n
def db(x): 
    global debug
    if debug: print(x)
debug = False
def genCombi(n, k): # nからk個を選ぶの0/1のリストを生成　[0]から変化
    bits = zeros(n)
    for i in range(2**n):
        cnt = 0
        for j in range(n):
            bits[j] = i%2
            if bits[j]==1: cnt+=1
            i //= 2
        if cnt==k: yield bits
            
N = getInt()
S = []
march = ['M','A','R','C','H']
dc = {'M':0,'A':0,'R':0,'C':0,'H':0,}
for i in range(N): 
    S.append(input())
    if S[i][0] in march:   dc[S[i][0]]+=1
db(S);db(dc)
cnt = 0
for c in genCombi(5,3):
    prod = 1
    for i in range(5): 
        if c[i]==1: prod *= c[i]*list(dc.values())[i]
    db(prod)
    cnt += prod
print(cnt)