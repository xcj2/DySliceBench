D=int(input())
count=0
while D%10==0:
    count+=1
    D//=10
if not count:
    ans=0
    for i in range(1,1000):
        val=str(i)
        val=val[::-1]
        rev=int(val)
        if rev-i==D:
            ans+=1

    for d in range(4,18):
        dic1={}
        dic2={}
        if d%2==0:
            k=d//2
            l=k//2
            def dfs(n,a):
                if n==l:
                    val=0
                    res=1
                    for i in range(len(a)):
                        val+=a[i]*(10**(d-1-i)-10**i)
                        if i!=0:
                            res*=10-abs(a[i])
                        else:
                            res*=9-abs(a[i])
                    if val not in dic1:
                        dic1[val]=0
                    dic1[val]+=res
                    return 0

                for i in range(-9,10):
                    dfs(n+1,a+[i])

            dfs(0,[])

            def dfs2(n,a):
                if n==k:
                    val=0
                    res=1
                    for i in range(len(a)):
                        val+=a[i]*(10**(d-1-l-i)-10**(i+l))
                        if i!=0:
                            res*=10-abs(a[i])
                        else:
                            res*=10-abs(a[i])
                    if val not in dic2:
                        dic2[val]=0
                    dic2[val]+=res
                    return 0

                for i in range(-9,10):
                    dfs2(n+1,a+[i])

            dfs2(l,[])
            for i in dic1:
                if D-i in dic2:
                    ans+=dic1[i]*dic2[D-i]

        else:
            k=d//2
            l=k//2
            def dfs(n,a):
                if n==l:
                    val=0
                    res=1
                    for i in range(len(a)):
                        val+=a[i]*(10**(d-1-i)-10**i)
                        if i!=0:
                            res*=10-abs(a[i])
                        else:
                            res*=9-abs(a[i])
                    if val not in dic1:
                        dic1[val]=0
                    dic1[val]+=res
                    return 0

                for i in range(-9,10):
                    dfs(n+1,a+[i])

            dfs(0,[])

            def dfs2(n,a):
                if n==k:
                    val=0
                    res=1
                    for i in range(len(a)):
                        val+=a[i]*(10**(d-1-l-i)-10**(i+l))
                        if i!=0:
                            res*=10-abs(a[i])
                        else:
                            res*=10-abs(a[i])
                    if val not in dic2:
                        dic2[val]=0
                    dic2[val]+=res
                    return 0

                for i in range(-9,10):
                    dfs2(n+1,a+[i])

            dfs2(l,[])

            for i in dic1:
                if D-i in dic2:
                    ans+=dic1[i]*dic2[D-i]*10

    print(ans)
else:
    ans=0
    for d in range(1,18):
        dic1={}
        dic2={}
        if d%2==0:
            k=d//2
            l=k//2
            def dfs(n,a):
                if n==l:
                    val=0
                    res=1
                    for i in range(len(a)):
                        val+=a[i]*(10**(d-1-i)-10**i)
                        if i!=0:
                            res*=10-abs(a[i])
                        else:
                            res*=10-abs(a[i])
                    if val not in dic1:
                        dic1[val]=0
                    dic1[val]+=res
                    return 0

                for i in range(-9,10):
                    dfs(n+1,a+[i])

            dfs(0,[])

            def dfs2(n,a):
                if n==k:
                    val=0
                    res=1
                    for i in range(len(a)):
                        val+=a[i]*(10**(d-1-l-i)-10**(i+l))
                        if i!=0:
                            res*=10-abs(a[i])
                        else:
                            res*=10-abs(a[i])
                    if val not in dic2:
                        dic2[val]=0
                    dic2[val]+=res
                    return 0

                for i in range(-9,10):
                    dfs2(n+1,a+[i])

            dfs2(l,[])
            for i in dic1:
                if D-i in dic2:
                    ans+=dic1[i]*dic2[D-i]

        else:
            k=d//2
            l=k//2
            def dfs(n,a):
                if n==l:
                    val=0
                    res=1
                    for i in range(len(a)):
                        val+=a[i]*(10**(d-1-i)-10**i)
                        if i!=0:
                            res*=10-abs(a[i])
                        else:
                            res*=10-abs(a[i])
                    if val not in dic1:
                        dic1[val]=0
                    dic1[val]+=res
                    return 0

                for i in range(-9,10):
                    dfs(n+1,a+[i])

            dfs(0,[])

            def dfs2(n,a):
                if n==k:
                    val=0
                    res=1
                    for i in range(len(a)):
                        val+=a[i]*(10**(d-1-l-i)-10**(i+l))
                        if i!=0:
                            res*=10-abs(a[i])
                        else:
                            res*=10-abs(a[i])
                    if val not in dic2:
                        dic2[val]=0
                    dic2[val]+=res
                    return 0

                for i in range(-9,10):
                    dfs2(n+1,a+[i])

            dfs2(l,[])

            for i in dic1:
                if D-i in dic2:
                    ans+=dic1[i]*dic2[D-i]*10

    print(ans*9*10**(count-1))