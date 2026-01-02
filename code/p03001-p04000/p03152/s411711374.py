def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b

m,n = getMN()
MOD = 1000000007
anums = getlist()
bnums = getlist()

anums.sort(reverse=True)
bnums.sort(reverse=True)
ans = 1
r_index = 0
d_index = 0
flag = True
for i in range(m*n):
    ans = ans % MOD
    num = m * n - i
    if r_index == m and d_index == n:
        ans *= num
        flag = False
    if flag:

        #print("num = {}, ans = {}".format(num,ans))
        #print("r = {}, d = {}, i = {}".format(r_index, d_index,i))
        in_r = num in anums
        in_d = num in bnums
        if in_r:
            if in_d:
                r_index += 1
                d_index += 1
            else:
                ans = ans * d_index
                r_index += 1
        else:
            if in_d:
                ans = ans * r_index
                d_index += 1
            else:
                if r_index * d_index < i:
                    import sys

                    ans = 0
                    flag = False
                else:
                    import sys
                    #print("koko", i, file=sys.stderr)
                    andayo = (ans * (r_index*d_index -i ))
                    #ans = ans * (r_index*d_index -i )
                    ans = andayo
                    #print("ans", ans)
ans = ans%MOD

print(ans)