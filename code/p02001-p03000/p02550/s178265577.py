def readInt():
    return int(input())
def readList():
    return list(map(int,input().split()))
def readMap():
	return map(int,input().split())
def readStr():
    return input()
inf=float('inf')
mod = 10**9+7
import math
def solve(N,X,M):
    seen=set()
    order_seen=[]
    while X not in seen:
        seen.add(X)
        order_seen.append(X)
        X=f(X,M)
    pos=order_seen.index(X)  # Find position of when the cycle begins
    if pos>N:  # If position is greater than N, then we know we are not going to include any values from the cycle.
        return sum(order_seen[:N])
    terms_before_cycle=order_seen[:pos]
    sum_terms_before_cycle=sum(terms_before_cycle)
    ans=sum_terms_before_cycle
    terms_in_cycle=order_seen[pos:]
    sum_cycle=sum(terms_in_cycle)
    length_cycle=len(terms_in_cycle)
    number_remaining_terms=N-pos
    mult_factor=(number_remaining_terms)//length_cycle
    ans+=(sum_cycle*mult_factor)
    numb_remain=(number_remaining_terms)%length_cycle
    ans+=sum(terms_in_cycle[:numb_remain])
    return ans

# The function for the recurrence relation.  A_n+1=A_n^2%M
def f(A,M):
    return pow(A,2,M)

N,X,M=readMap()
print(solve(N,X,M))