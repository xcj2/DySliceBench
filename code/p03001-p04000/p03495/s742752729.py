N, K = map(int, input().split())
A = [int(a) for a in input().split()]

def make_group(list):
    list.sort()
    group = []
    g_count = 0
    prev = list[0]
    for i in range(N):
        current = list[i]
        if prev != current:
            group.append(g_count)
            g_count = 0
        g_count += 1
        prev = current
        if i == N - 1:
            group.append(g_count)
    return sorted(group)

def calc_moving_count(group):
    group_length = len(group)
    length = max(group_length - K, 0)
    should_move_group = group[:length]
    count = sum(should_move_group)
    return count

def main():
    group = make_group(A)
    count = calc_moving_count(group)
    print(count)

if __name__  == '__main__':
    main()