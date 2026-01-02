# E
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def SumArea(r, l, a2):
    return a2[l]-a2[r]

def judge(cand, a, k):
    m_list = [i%cand for i in a]
    m_list.sort()
    p_list = [cand-r for r in m_list]
    
    # 累積和
    b=list(range(1,30))
    m2=[0]
    p2=[0]
    for i in m_list:m2.append(m2[-1]+i)
    for i in p_list:p2.append(p2[-1]+i)
        
    length = len(a)
    for i in range(length):
        m_total  = SumArea(0, i, m2)
        p_total = SumArea(i, length, p2)
        if m_total == p_total and p_total <= k:
            return True
    return False
    
        
n,k = map(int, input().split())
a = list(map(int, input().split()))
pflag = True
# 候補はsum(a)の正約数。
total = sum(a)
length = len(a)
candidate = make_divisors(total)
candidate.sort(reverse = True)
for cand in candidate:
    if judge(cand, a, k):
        print(cand)
        pflag = False
        break
if pflag:
    print(1)