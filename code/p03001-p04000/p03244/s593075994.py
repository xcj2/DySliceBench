from collections import Counter

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    n = ii()
    v = list(mi())
    ve = [v[i] for i in range(n) if i%2==0]
    vo = [v[i] for i in range(n) if i%2==1]

    ce = Counter(ve)
    co = Counter(vo)

    if ce.most_common()[0][0] == co.most_common()[0][0]:
        if len(ce.most_common()) > 1 and len(co.most_common()) > 1:
            if ce.most_common()[1][1] > co.most_common()[1][1]:
                ne = ce.most_common()[1][1]
                no = ce.most_common()[0][1]
            else:
                ne = ce.most_common()[0][1]
                no = co.most_common()[1][1]
        else:
            ne = ce.most_common()[0][1]
            no = 0
    else:
        ne = ce.most_common()[0][1]
        no = co.most_common()[0][1]

    print(n-ne-no)

if __name__ == '__main__':
    main()