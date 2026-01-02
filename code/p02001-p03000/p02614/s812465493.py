from copy import deepcopy
def toCount(L):
    return [ 1 if i == "#" else 0 for i in L]
    
def resolve():
    H,W,K = map(int,input().split())
    C=[toCount(input()) for i in range(H)]
    count = 0

    rc = list(BitSeacher(H))

    for rows in rc:
        for cc in range(2**W):
            
            cols = bst(cc,W)

            TC = deepcopy(C)
            for i in rows:
                TC[i]=[0]*W
            for i in cols:
                for j in range(H):
                    TC[j][i]=0

            if K==sum(map(sum,TC)):
                count +=1

    print(count)

def bst(val,bitcount):
        ans =[]
        flg =1
        for i in range(bitcount):
            if flg & val != 0:
                ans.append(i)
            flg = flg.__lshift__(1)
        return ans


class BitSeacher:
    def __init__(self,bitcount):
        self.counter =0
        self.bitcount = bitcount
        self.mx = 2**bitcount-1
    
    def __next__(self):
        if self.counter > self.mx:
            raise StopIteration()
        ans =[]
        flg =1
        for i in range(self.bitcount):
            if flg & self.counter != 0:
                ans.append(i)
            flg = flg.__lshift__(1)
        self.counter+=1
        return ans

    def __iter__(self):
        return self

resolve()