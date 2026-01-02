###############################################################################

from bisect import bisect_left as binl
from copy import copy, deepcopy

def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def modadd(x, y):
    global mod
    return (x + y) % mod


def modmlt(x, y):
    global mod
    return (x * y) % mod


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


def get_divisors(x):
    retlist = []
    for i in range(1, int(x**0.5) + 3):
        if x % i == 0:
            retlist.append(i)
            retlist.append(x // i)
    return retlist


def make_linklist(xylist):
    linklist = {}
    for a, b in xylist:
        linklist.setdefault(a, [])
        linklist.setdefault(b, [])
        linklist[a].append(b)
        linklist[b].append(a)
    return linklist


def calc_longest_distance(linklist, v=1):
    distance_list = {}
    distance_count = 0
    distance = 0
    vlist_previous = []
    vlist = [v]
    nodecount = len(linklist)

    while distance_count < nodecount:
        vlist_next = []
        for v in vlist:
            distance_list[v] = distance
            distance_count += 1
            vlist_next.extend(linklist[v])
        distance += 1
        vlist_to_del = vlist_previous
        vlist_previous = vlist
        vlist = list(set(vlist_next) - set(vlist_to_del))

    max_distance = -1
    max_v = None
    for v, distance in distance_list.items():
        if distance > max_distance:
            max_distance = distance
            max_v = v

    return (max_distance, max_v)


def calc_tree_diameter(linklist, v=1):
    _, u = calc_longest_distance(linklist, v)
    distance, _ = calc_longest_distance(linklist, u)
    return distance


###############################################################################


def make_1st_2nd_list(countlist):
    max_v_list = []
    max_v_list_2nd = []
    max_count = -1
    max_count_2nd = -1

    for i, count in enumerate(countlist):
        if count > max_count:
            max_count_2nd = max_count
            max_v_list_2nd = max_v_list
            max_count = count
            max_v_list = [i]
        elif count == max_count:
            max_v_list.append(i)
        elif count > max_count_2nd:
            max_count_2nd = count
            max_v_list_2nd = [i]
        elif count == max_count_2nd:
            max_v_list_2nd.append(i)

    return (max_v_list, max_v_list_2nd)


def main():
    n = intin()
    vlist = intina()

    countlist0 = [0] * (10**5 + 1)
    countlist1 = [0] * (10**5 + 1)
    for i, v in enumerate(vlist):
        if i % 2 == 0:
            countlist0[v] += 1
        else:
            countlist1[v] += 1

    max_v_list0, max_v_list_2nd0 = make_1st_2nd_list(countlist0)
    max_v_list1, max_v_list_2nd1 = make_1st_2nd_list(countlist1)

    if len(max_v_list0) == 1 and len(max_v_list1) == 1 and \
       max_v_list0[0] == max_v_list1[0]:
        if not max_v_list_2nd0 and not max_v_list_2nd1:
            print(n // 2)
        elif not max_v_list_2nd0:
            print(n - countlist0[max_v_list0[0]]
                  - countlist1[max_v_list_2nd1[0]])
        elif not max_v_list_2nd1:
            print(n - countlist0[max_v_list_2nd0[0]]
                  - countlist1[max_v_list1[0]])
        else:
            c0 = countlist0[max_v_list0[0]]
            c1 = countlist1[max_v_list1[0]]

            ans1 = n - countlist0[max_v_list0[0]] \
                  - countlist1[max_v_list_2nd1[0]]
            ans2 = n - countlist0[max_v_list_2nd0[0]] \
                  - countlist1[max_v_list1[0]]
            print(min(ans1, ans2))

        return

    print(n - countlist0[max_v_list0[0]]
          - countlist1[max_v_list1[0]])


if __name__ == '__main__':
    main()
