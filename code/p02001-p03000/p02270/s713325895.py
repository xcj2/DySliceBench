import math
def min_sufficient_load(w, k):
    return check(w, k, 0, sum(w))

def check(w, k, p1, p2):
    if k==1:
        return p2
    if p2 - p1 == 1:
        if get_trunk_No(w, p1) == k:
            return max(p1,max(w))
        else:
            return max(p2,max(w))
    m = math.ceil((p1+p2)/2)
    trunk_no = get_trunk_No(w,m)
    if trunk_no > k:
        return check(w, k, m, p2)
    else:
        return check(w, k, p1, m)
def get_trunk_No(w,m):
    temp = 0
    trunk_no = 1
    for i in w:
        if temp + i <= m:
            temp += i
            if temp == m:
                trunk_no += 1
                temp = 0
        else:
            trunk_no += 1
            temp = i
    if temp==0:
        trunk_no-=1
    return trunk_no
if __name__=="__main__":
    n,k = map(int,input().split(" "))
    w = []
    for i in range(n):
        w.append(int(input()))
    print(min_sufficient_load(w,k))
