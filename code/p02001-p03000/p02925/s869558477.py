from collections import deque


def make_state(N):
    state = [[-1 for j in range(N+1)] for i in range(N+1)]
    min_state = 0
    s = min_state
    for i in range(1, N+1):
        for j in range(1, i):
            state[i][j] = s
            state[j][i] = s
            s += 1
    return state


def solve(N, A):
    state = make_state(N)
    max_state = N * (N-1) // 2
    n_prev_states = [0 for i in range(max_state)]
    next_states = [set() for i in range(max_state)]
    for i in range(1, N+1):
        for k in range(N-2):
            ps = state[i][A[i][k]]
            ns = state[i][A[i][k+1]]
            n_prev_states[ns] += 1
            next_states[ps].add(ns)
    
    today_states = deque()
    for s in range(max_state):
        if n_prev_states[s] == 0:
            today_states.appendleft(s)
    
    n_days = 0
    n_states_left = max_state
    while len(today_states) > 0:
        n_days += 1
        if len(today_states) == 0:
            break
        n_states_left -= len(today_states)
        for _ in range(len(today_states)):
            s = today_states.pop()
            for ns in next_states[s]:
                n_prev_states[ns] -= 1
                if n_prev_states[ns] == 0:
                    today_states.appendleft(ns)
    return n_days if n_states_left == 0 else -1


def main():
    N = int(input())
    A = list()
    A.append([])
    for i in range(N):
        a = list(map(int, input().strip().split()))
        A.append(a)
    print(solve(N, A))


if __name__ == "__main__":
    main()
