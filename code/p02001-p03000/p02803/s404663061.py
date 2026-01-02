from collections import deque

def main():
    h, w = map(int, input().split())
    ls = [input() for _ in range(h)]

    def trans(a, b):
        return a * w + b

    ls2 = [[] for _ in range(h * w)]

    for i in range(h):
        for j in range(w):
            # check ij
            if ls[i][j] == '#':
                continue
            if i >= 1 and ls[i-1][j] != '#':
                ls2[trans(i, j)].append(trans(i-1, j))
            if i <= h-2 and ls[i+1][j] != '#':
                ls2[trans(i, j)].append(trans(i + 1, j))
            if j <= w-2 and ls[i][j+1] != '#':
                ls2[trans(i, j)].append(trans(i, j + 1))
            if j >= 1 and ls[i][j-1] != '#':
                ls2[trans(i, j)].append(trans(i, j - 1))


    #print(ls2)


    def route(i):
        count = 1
        ss = deque(ls2[i])
        next = deque()
        explored = {i}
        while ss or next:
            if not ss:
                count +=1
                ss = next
                next = deque()
            now =ss.popleft()
            if now in explored:
                continue
            else:
                explored.add(now)
                next.extend(ls2[now])
        return count-1
    ans = 0
    for i in range(h * w - 1):
        if ls2[i] == []:
            continue
        ans = max(ans, route(i))

    print(ans)
if __name__ == '__main__':
    main()