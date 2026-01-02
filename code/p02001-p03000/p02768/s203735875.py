#binary exponentiation for 2^big number -1
#sum of n choose. ... 2^n -1
# how to compute n choose a
# euler's quotient theorem
# special case fermats little theoreom


#n kinds of flowers, 1 of each kind
# choose 1 more of each to make bouquet
# a b, total num of flowers cannot be a or b
# how many diff ouquets can she make?
# find the count modulo (10^9 + 7)

#two bouquets are considered different

# (x^y)%p
def powerMod(x,y,p):
    #initialize result
    res = 1
    #update x if it is more than or equal to p
    x = x%p
    
    while (y>0):
        #if y is odd, multiply x with result
        if ((y&1)==1):
            res = (res*x)%p
        
        #y must be even now
        y = y >> 1 #y = y/2
        x = (x*x)%p
    return res

def power(x,y):
    #initialize result
    res = 1
    while (y>0):
        #if y is odd, multiple x with result
        if((y&1)==1):
            res = res*x
        
        #y is even
        y = y >> 1 #divide y by 2
        x = x*x
    return res


input = [int(x) for x in input().split()]
numFlowers = input[0]
a = input[1]
b = input[2]

tenToNine = power(10,9)
allchoices = powerMod(2,numFlowers,tenToNine+7)-1

#compute n choose k in O(k) time and O(1) space
def binomial(n,k):
    #since C(n,k) = C(n,n-k)
    if(k>n-k):
        k = n=k
    
    #initialize result
    res = 1
    #calculate value of simplified n choose k expansion
    for i in range(k):
        res = res*(n-i)
        res = res/ (i+1)
    return res

aX = 1
aY = 1

#need to compute x and y for a and b, clearly separate them
for i in range(a):
    aX = aX*(numFlowers-i)%(tenToNine+7)
    aY = aY*(i+1)%(tenToNine+7)

bX = 1
bY = 1

#need to compute x and y for a and b, clearly separate them
for i in range(b):
    bX = bX*(numFlowers-i)%(tenToNine+7)
    bY = bY*(i+1)%(tenToNine+7)

#subtract and we're done

# countA = aX*powerMod(aY,tenToNine+7-2,tenToNine+7)
# countB = bX*powerMod(bY,tenToNine+7-2,tenToNine+7)
countA = aX*powerMod(aY,tenToNine+7-2,tenToNine+7)
countB = bX*powerMod(bY,tenToNine+7-2,tenToNine+7)
numBouquet = (allchoices-countA-countB)%(tenToNine+7)

print(numBouquet)
