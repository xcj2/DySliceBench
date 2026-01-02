#D
N, X = [int(x) for x in input().split()]

def make(lv):
    if lv==0: return 'P'
    else: return 'B' + make(lv-1) + 'P' + make(lv-1) + 'B'

def countBurg(lv):
    if lv==0: return 1, 1
    else: #return 'B' + make(lv-1) + 'P' + make(lv-1) + 'B'
        c1 = countBurg(lv-1)
        return 1+c1[0]+1+c1[0]+1, c1[1]+1+c1[1]

def countBurg2(lv):
    count = [(1,1) for i in range(lv+1)]
    for i in range(1,lv+1):
        count[i] = count[i-1][0]*2+3, count[i-1][1]*2+1
    return count

BurgCount = countBurg2(50) #[(bc, pc),...]

def countPate(lv, x):
    #print(lv, x) #
    if lv<=0: return 1

    ec = 1 # Eat Count   B
    epc = 0 # Eat Pate Count
    #print(ec, epc) #
    if ec>=x: return epc
    
    if ec+BurgCount[lv-1][0]>x:
        epc += countPate(lv-1, x-ec)
        ec = x #lv-1
    else:
        ec += BurgCount[lv-1][0]#lv-1
        epc += BurgCount[lv-1][1]
    #print(ec, epc) #
    if ec>=x: return epc
    
    ec += 1 #P
    epc += 1 
    #print(ec, epc) #
    if ec>=x: return epc
    
    if ec+BurgCount[lv-1][0]>x:
        epc += countPate(lv-1, x-ec)
        ec = x #lv-1
    else:
        ec += BurgCount[lv-1][0]#lv-1
        epc += BurgCount[lv-1][1]
    #print(ec, epc) #
    if ec>=x: return epc
    
    ec += 1 #B
    #print(ec, epc) #
    return epc
            
#burg = make(N)
#print(burg)#
#for i in range(X):
#    if burg[i]=='P': count += 1

#print(BCount)#

print(countPate(N,X))

