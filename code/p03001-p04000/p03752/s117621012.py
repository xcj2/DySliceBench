

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

def checker(A,group,K):
    if len(group) < K:
        return 10**20

    tbl = [False for i in A]
    for i in group:
        tbl[i]=True
    mx = 0
    count = 0
    for i in range(len(A)):
        if not tbl[i]:
            mx = max(mx,A[i])
            continue
        
        if mx < A[i]:
            mx = A[i]
        else:
            count += mx - A[i] +1
            mx +=1
    return count






def resolve():
    N,K = map(int,input().split())
    A= list(map(int,input().split()))
    mn = 10**20
    for group in BitSeacher(N):
        group.sort()
        mn = min(mn,checker(A,group,K))

    print(mn)



if __name__ == "__main__":
    resolve()