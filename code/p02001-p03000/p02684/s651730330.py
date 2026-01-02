# import sys
# input = sys.stdin.readline

def main():
    n, k = input_list()
    a = input_list()
    d = {1: 0}
    pre = 1
    loop_start = 0
    loop_end = 0
    loop_pos = 0
    for i in range(1, n+1):
        new = a[pre - 1]
        if d.get(new):
            loop_start = d[new]
            loop_end = i
            loop_pos = new
            break
        if i == k:
            print(new)
            exit()
        d[new] = i
        pre = new
    k -= loop_start
    k %= loop_end - loop_start
    pre = loop_pos
    for i in range(k):
        pre = a[pre - 1]
    print(pre)

    # goto = [a[0]]
    # index = 0
    # looped = []
    # g = 0
    # for i in range(k):
    #     g = goto[index]
    #     # print(goto)
    #     if a[g-1] in goto:
    #         # print("goto!", a[g-1], goto)
    #         break
    #     goto.append(a[g-1])
    #     index += 1
    #
    # s = goto.index(a[g-1])
    # looped = goto[s:]
    #
    # if k % len(looped) == 0:
    #     print(goto[-1])
    # else:
    #     k -= len(goto) - len(looped)
    #     amari = k % len(looped)
    #     print(looped[amari-1])

#6 5 2 5 3 2
#1 2 3 4 5 6

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
