# from https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2019/0106_educational_dp_2
def solve(n,hhh,aaa):
    n2=1<<n.bit_length()
    offset=n2-1
    data=[0]*((n2<<1)-1)

    def update(k,x):
        i=k+offset
        while i>=0:
            if data[i]<x:
                data[i]=x
            else:
                break
            i=(i-1)//2

    def get_max(k):
        i=k+offset
        ret=data[i]
        while i:
            if i%2==0:
                ret=max(ret,data[i-1])
            i=(i-1)//2
        return ret

    srt=sorted((h,i) for i,h in enumerate(hhh))
    for h,i in srt:
        update(i,get_max(i)+aaa[i])

    return data[0]



n=int(input())
hhh=[int(i) for i in input().split()]
aaa=[int(i) for i in input().split()]
print(solve(n,hhh,aaa))
