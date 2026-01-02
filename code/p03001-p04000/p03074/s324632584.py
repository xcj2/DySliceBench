
import queue

def read_input():
    n, k = map(int, input().split())
    s = list(map(int, list(str(input()))))

    return n, k, s


# 0, 1, ....を(0, n1), (1, n2)みたいな形にする
def convert_01(s):
    result = []

    result.append([s[0], 1])
    for ss in s[1:]:
        if result[-1][0] == ss:
            result[-1][1] += 1
        else:
            result.append([ss, 1])

    return result


# index以降の要素、かつ0の数がKを下回るサブリストにある要素をカウントする
def get_count(r,k):
    count = 0
    max_count = 0
    zeros = 0

    q = queue.Queue()

    for e in r:
        if e[0] == 0 and zeros >= k:
        # すでにk回0を操作した
            while True:
                t = q.get()
                count -= t[1]

                if t[0] == 0:
                    zeros -= 1
                    break

        q.put(e)
        count += e[1]

        if e[0] == 0:
            zeros += 1

        if max_count < count:
            max_count = count

    return max_count






if __name__ == '__main__':
    n, k, s = read_input()
    r = convert_01(s)

    print(get_count(r, k))

