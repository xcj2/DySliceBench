a = int(input())
b = list(map(str, input().split()))
# print(b)

# print(b[1][1])
# print(type(int(b[1][1])))

# for k in range(len(b)):
#     c.append(b[k][1])
# print(c)

c = b[:] #リストで参照渡しをせずに、値のみを渡す方法。
d = b[:]

# print(id(b))
# print(id(c))
# print(id(d))

def BubleSort(c):
    for i in range(len(c)):
        for j in range(len(c)-1,i,-1):
            if int(c[j][1])<int(c[j-1][1]):
                c[j],c[j-1]= c[j-1],c[j]
    return c

def isStable(In, Out):
    for m in range(0,len(Out)):
        for n in range(m+1,len(Out)):
            for x in range(0,len(Out)):
                for y in range(x+1,len(Out)):
                    if int(In[m][1])==int(In[n][1]) and In[m] == Out[y] and In[n] == Out[x]:
                        return print('Not stable')
    return print('Stable')

def SelectSort(d):
    for i in range(len(d)-1):
        mini = i
        for j in range(i+1,len(d)):
            if int(d[mini][1])>int(d[j][1]):
                mini=j
        if int(d[mini][1])!=int(d[i][1]):
            d[i],d[mini]=d[mini],d[i]
    return d


print(*BubleSort(c))
isStable(c,b)
# print(d)
# print(b)
print(*SelectSort(d))
isStable(d,b)
