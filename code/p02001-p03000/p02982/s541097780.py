def get_distance(x, y, d):
    result = 0
    for i in range(d):
        result += (x[i] - y[i]) ** 2
    return result

def is_2jou(i):
    ii = i ** 0.5
    if ii == float(round(ii)):
        return True
    else:
        return False

def main():
    n, d = map(int, input().split())
    x = []
    for _ in range(n):
        x.append([int(i) for i in input().split()])

    cnt = 0
    for _ in range(len(x)):
        head = x.pop(0)
        for j in x:
            distance = get_distance(head, j, d)
            flag = is_2jou(distance)
            if flag:
                cnt += 1

    print(cnt)

main()