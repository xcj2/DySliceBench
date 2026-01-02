def v2i(v):
        v = list(v)
        n = 0
        for i,c in enumerate(v):
            if c == 'A':
                n += 0 + 4 * i
            elif c == 'C':
                n += 1 + 4 * i
            elif c == 'G':
                n += 2 + 4 * i
            elif c == 'T':
                n += 3 + 4 * i
            n *= 4
        n /= 4
        return int(n)



class Dict():

    def __init__(self):
        self.tree = [False] * 4**12

    def find(self,key):
        if self.tree[key] == True:
            print("yes")
        else:
            print("no")
    
    def insert(self,key):
        self.tree[key] = True

    
N = int(input())
D = Dict()
for i in range(N):
    Q,V = input().split()
    if Q == "insert":
        D.insert(v2i(V))
    else:
        D.find(v2i(V))
    #print(D.tree[:60])






