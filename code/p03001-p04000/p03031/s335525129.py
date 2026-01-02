n,m=map(int,input().split())
l=[]
for _ in range(m):
    kari=list(map(int,input().split()))
    l.append(kari)
p=list(map(int,input().split()))
num2=[]
def deal1():
    ans=0
    for a in range(2):
        w=[a]
        all=0
        for k in range(m):
            cnt==0
            for q in range(l[k][0]):
                if w[l[k][q+1]-1]==1:
                    cnt+=1
            if p[k]==cnt%2:
                all+=1
        if all==m:
            ans+=1
    return ans
def deal2():
    ans=0
    for a in range(2):
        for b in range(2):
            w=[a,b]
            all=0
            for k in range(m):
                cnt=0
                for q in range(l[k][0]):
                    if w[l[k][q+1]-1]==1:
                        cnt+=1
                if p[k]==cnt%2:
                    all+=1
            if all==m:
                ans+=1
    return ans
def deal3():
    ans=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                w=[a,b,c]
                all=0
                for k in range(m):
                    cnt=0
                    for q in range(l[k][0]):
                        if w[l[k][q+1]-1]==1:
                            cnt+=1
                    if p[k]==cnt%2:
                        all+=1
                if all==m:
                    ans+=1
    return ans
def deal4():
    ans=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    w=[a,b,c,d]
                    all=0
                    for k in range(m):
                        cnt=0
                        for q in range(l[k][0]):
                            if w[l[k][q+1]-1]==1:
                                cnt+=1
                        if p[k]==cnt%2:
                            all+=1
                    if all==m:
                        ans+=1
    return ans
def deal5():
    ans=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        w=[a,b,c,d,e]
                        all=0
                        for k in range(m):
                            cnt=0
                            for q in range(l[k][0]):
                                if w[l[k][q+1]-1]==1:
                                    cnt+=1
                            if p[k]==cnt%2:
                                all+=1
                        if all==m:
                            ans+=1
    return ans
def deal6():
    ans=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            w=[a,b,c,d,e,f]
                            all=0
                            for k in range(m):
                                cnt=0
                                for q in range(l[k][0]):
                                    if w[l[k][q+1]-1]==1:
                                        cnt+=1
                                if p[k]==cnt%2:
                                    all+=1
                            if all==m:
                                ans+=1
    return ans
def deal7():
    ans=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                w=[a,b,c,d,e,f,g]
                                all=0
                                for k in range(m):
                                    cnt=0
                                    for q in range(l[k][0]):
                                        if w[l[k][q+1]-1]==1:
                                            cnt+=1
                                    if p[k]==cnt%2:
                                        all+=1
                                if all==m:
                                    ans+=1
    return ans
def deal8():
    ans=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    w=[a,b,c,d,e,f,g,h]
                                    all=0
                                    for k in range(m):
                                        cnt=0
                                        for q in range(l[k][0]):
                                            if w[l[k][q+1]-1]==1:
                                                cnt+=1
                                        if p[k]==cnt%2:
                                            all+=1
                                    if all==m:
                                        ans+=1
    return ans
def deal9():
    ans=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    for i in range(2):
                                        w=[a,b,c,d,e,f,g,h,i]
                                        all=0
                                        for k in range(m):
                                            cnt=0
                                            for q in range(l[k][0]):
                                                if w[l[k][q+1]-1]==1:
                                                    cnt+=1
                                            if p[k]==cnt%2:
                                                all+=1
                                        if all==m:
                                            ans+=1
    return ans

def deal10():
    ans=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    for i in range(2):
                                        for j in range(2):
                                            w=[a,b,c,d,e,f,g,h,i,j]
                                            all=0
                                            for k in range(m):
                                                cnt=0
                                                for q in range(l[k][0]):
                                                    if w[l[k][q+1]-1]==1:
                                                        cnt+=1
                                                if p[k]==cnt%2:
                                                    all+=1
                                            if all==m:
                                                ans+=1
    return ans
if n==1:
    print(deal1())
if n==2:
    print(deal2())
if n==3:
    print(deal3())
if n==4:
    print(deal4())
if n==5:
    print(deal5())
if n==6:
    print(deal6())
if n==7:
    print(deal7())
if n==8:
    print(deal8())
if n==9:
    print(deal9())
if n==10:
    print(deal10())
