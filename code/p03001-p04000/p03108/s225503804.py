
def get_parent(num, parent):
    if parent[num] == num:
        return num
    else:
        return get_parent(parent[num], parent)

def calc_change_data(ans, parent, a_parent, b_parent, island_count):
    big_parent = max(a_parent, b_parent)
    min_parent = min(a_parent, b_parent)
    parent[big_parent] = min_parent
    ans -= island_count[big_parent] * island_count[min_parent]
    island_count[min_parent] += island_count[big_parent]
    return ans, parent, island_count

def main():
    island_num, bridge_num = map(int, input().split())
    bridge_data = [list(map(int, input().split())) for i in range(bridge_num)]
    parent = [i for i in range(island_num)]
    island_count = [1 for i in range(island_num)]

    ans = island_num * (island_num - 1) // 2
    ans_data = [ans]

    for num_a, num_b in bridge_data[::-1]:
        num_a -= 1
        num_b -= 1

        a_parent = get_parent(num_a, parent)
        b_parent = get_parent(num_b, parent)

        if a_parent != b_parent:
            ans, parent, island_count = calc_change_data(ans, parent, a_parent, b_parent, island_count)
        ans_data.append(ans)

    for i in range(bridge_num)[::-1]:
        print(ans_data[i])

if __name__ == '__main__':
    main()