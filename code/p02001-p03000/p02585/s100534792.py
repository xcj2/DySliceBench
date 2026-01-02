import copy

def cost_val(visit_list, P, C):
    maxval = [-10**10] * (len(P) + 1)
    for start_idx in visit_list:
        cost = 0
        now_id = start_idx
        for i in range(len(visit_list)):
            now_id = P[now_id]
            cost += C[now_id]
            maxval[i + 1] = max(maxval[i + 1], cost)
    return maxval[1:len(visit_list) + 1]

def cycles(P):
    cycle_list = []
    visit_list = [False] * len(P)
    for i in range(len(P)):
        if visit_list[i]:
            continue
        now_id = i
        cycle = []
        for j in range(len(P)):
            if visit_list[now_id]:
                break
            cycle.append(now_id)
            visit_list[now_id] = True
            now_id = P[now_id]
        cycle_list.append(cycle)
    return cycle_list

def main():
    N, K = map(int, input().split())
    P = list(map(lambda x: int(x) - 1, input().split()))
    C = list(map(int, input().split()))
    cycle_list = cycles(P)
    ans = max(C)
    for cycle in cycle_list:
        maxval = cost_val(cycle, P, C)
        if len(cycle) > K:
            ans = max(ans, max(maxval[:K]))
        else:
            if K % len(cycle) == 0:
                ans = max(ans, max(maxval), max(map(lambda x: x + maxval[-1] * (K // len(cycle) - 1), maxval)), maxval[-1] * (K // len(cycle)))
            else:
                ans = max(ans, max(maxval), max(map(lambda x: x + maxval[-1] * (K // len(cycle) - 1), maxval)), maxval[-1] * (K // len(cycle)) + max(maxval[:(K % len(cycle))]))
    return ans

if __name__ == '__main__':
    print(main())