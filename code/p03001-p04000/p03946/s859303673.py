import functools

def calc_reward(seq):    
    def f(m_r, e):
        return min(m_r[0], e), max(m_r[1], e - m_r[0])
    return functools.reduce(f, seq, (seq[0], 0))[1]

def calc_cost(seq: list):
    mi, ma = min(seq), max(seq)
    if mi == ma:
        return 0
    rev_seq = seq[::-1] 
    return min(seq[seq.index(mi):].count(ma), rev_seq[rev_seq.index(ma):].count(mi))
        
def divide_iter(seq):
    s = [seq[0]]
    for e in seq[1:]:
        if e < s[0]:
            yield s
            s = []
        s.append(e)
    yield s

def solve(seq):
    divided = list(divide_iter(seq))    
    rewards = list(map(calc_reward, divided))
    costs = list(map(calc_cost, divided))
    max_reward = max(rewards)
    return sum(map(lambda r_c: r_c[1], 
            filter(lambda r_c: r_c[0] == max_reward, zip(rewards, costs))))

def main():
    _ = input()
    A = list(map(int, input().split()))
    print(solve(A))

if __name__ == "__main__":
    main()    