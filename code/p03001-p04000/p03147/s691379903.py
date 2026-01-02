def recur(heights):
    global ans
    if heights == [0]:
        return 1
    ans += 1
    new_heights = []
    for h in heights:
        new_heights.append(h - 1)
    for splitted_new_heights in split_heights(new_heights):
        recur(splitted_new_heights)


def split_heights(heights):
    splitted_heights = []
    partial_heights = []
    for h in heights:
        if h == 0 and len(partial_heights) > 0:
            splitted_heights.append(partial_heights)
            partial_heights = []
        elif h != 0:
            partial_heights.append(h)
    if len(partial_heights) > 0:
        splitted_heights.append(partial_heights)
    return splitted_heights


def main():
    global ans
    ans = 0
    N = int(input())
    h = list(map(int, input().split()))
    for splitted_heights in split_heights(h):
        recur(splitted_heights)
    print(ans)


if __name__ == '__main__':
    main()
