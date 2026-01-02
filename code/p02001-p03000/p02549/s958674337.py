def getsum(BITTree, i):
    s = 0  # initialize result

    # index in BITree[] is 1 more than the index in arr[]
    i = i + 1

    # Traverse ancestors of BITree[index]
    while i > 0:
        # Add current element of BITree to sum
        s += BITTree[i]

        # Move index to parent node in getSum View
        i -= i & (-i)
    return s


# Updates a node in Binary Index Tree (BITree) at given index
# in BITree. The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(BITTree, n, i, v):
    # index in BITree[] is 1 more than the index in arr[]
    i += 1

    # Traverse all ancestors and add 'val'
    while i <= n:
        # Add 'val' to current node of BI Tree
        BITTree[i] += v

        # Update index to that of parent in update View
        i += i & (-i)

    # Constructs and returns a Binary Indexed Tree for given


# array of size n.
def construct(arr, n):
    # Create and initialize BITree[] as 0
    BITTree = [0] * (n + 1)

    # Store the actual values in BITree[] using update()
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])

        # Uncomment below lines to see contents of BITree[]
    # for i in range(1,n+1):
    #     print BITTree[i],
    return BITTree


n,k=map(int,input().split())
c=[]
a=[0]*(n+1)
a[1]=1
BITTree = construct(a,len(a))
mod=998244353
for i in range(k):
    x,y=map(int,input().split())
    c.append([x,y])

for i in range(2,n+1):
    for j in range(len(c)):
        p,q=c[j][0],c[j][1]
        if i-q>0:
            l,r=i-p,i-q

            z=(getsum(BITTree,l)-getsum(BITTree,r-1))%mod

            a[i]+=z
            updatebit(BITTree, len(a), i,z)

        else:
            q=i-1
            if i-q>0 and i-p>0:
                l, r = i - p, i - q

                z = (getsum(BITTree, l) - getsum(BITTree, r - 1))%mod
                ##z= getsum(BITTree, q) - getsum(BITTree, p - 1)
                ##print(z)
                a[i]+=z
                updatebit(BITTree, len(a), i, z)
                ##print(BITTree)

##print(a)
print(a[n]%mod)






