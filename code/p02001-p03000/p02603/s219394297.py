import sys

def input():
    return sys.stdin.readline()[:-1]

class M_Kun:
    def __init__(self):
        self.money = 1000
        self.stock = 0
        
    def buy(self, value):
        num = self.money // value
        self.money -= value * num
        self.stock += num
        
    def sell(self, value):
        self.money += value * self.stock
        self.stock = 0


def main():
    N = int(input())
    A = list(map(int, input().split()))

    local_min = [False]*N
    local_max = [False]*N

    is_ascending = False
    for a in A[1:]:
        if a > A[0]:
            is_ascending = True
            break
        elif a < A[0]:
            break

    if is_ascending:
        local_min[0] = True
    else:
        local_max[0] = True

    for i in range(N-1):
        if A[i] == A[i+1]:
            continue
        elif is_ascending and A[i] > A[i+1]:
            local_max[i] = True
            is_ascending = False
        elif (not is_ascending) and A[i] < A[i+1]:
            local_min[i] = True
            is_ascending = True

    if is_ascending:
        local_max[-1] = True


    m_kun = M_Kun()

    for i in range(N):
        if local_min[i]:
            m_kun.buy(A[i])
        if local_max[i]:
            m_kun.sell(A[i])

    print(m_kun.money)
    
main()