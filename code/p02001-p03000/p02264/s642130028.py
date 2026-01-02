from collections import deque

def print_dict_multi_low(a_dict):
    for k, v in a_dict.items():
        print("{0} {1}".format(k, v))
        
def calc_round_robin(A, q):
    t = 0
    B = {}
    queue = deque([])
    for k, v in A.items():
        queue.append((k, v))
    
    while queue:
        k, v = queue.popleft()
        residual = int(v) - q
        if residual > 0:
            queue.append((k, residual))
            t += q
        else:
            t += (q + residual)
            B[k] = t
    print_dict_multi_low(B)

def read_n_lows_dict_input(n):
    a_dict = dict(input().split() for _ in range(n))
    return a_dict

n, q = (map(int,input().split()))
A = read_n_lows_dict_input(n)

calc_round_robin(A, q)
