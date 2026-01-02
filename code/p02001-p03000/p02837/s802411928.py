def readinput():
    n=int(input())
    shogensList=[]
    for i in range(n):
        a=int(input())
        shogens=[]
        for _ in range(a):
            shogen=list(map(int,input().split()))
            shogens.append(shogen)
        shogensList.append(shogens)
    return n, shogensList

def isMujun(shogensList, shojikiList):
    for shojiki in shojikiList:
        shogens=shogensList[shojiki]
        #print('shogens: {}'.format(shogens))
        #print('shojikiList: {}'.format(shojikiList))
        for x,y in shogens:
            if(y==1):
                if not (x-1 in shojikiList):
                    return True
            else:
                if x-1 in shojikiList:
                    return True
    return False

def main(n,shogensList):
    maxShojiki=0
    for x in range(2**n):
        shojikiList=[]
        b=1
        for i in range(n):
            if (x&b==b):
                shojikiList.append(i)
            b=b*2
        #print('shojikiList: {}'.format(shojikiList))
        #print(isMujun(shogensList, shojikiList))
        if not isMujun(shogensList, shojikiList):
            maxShojiki=max(maxShojiki, len(shojikiList))
    return maxShojiki

if __name__=='__main__':
    n,shogensList=readinput()
    ans=main(n,shogensList)
    print(ans)
 