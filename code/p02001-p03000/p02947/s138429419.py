from collections import Counter

def main():
    N = int(input())
    counter = Counter()
    for i in range(N):
        k = "".join(sorted(input().strip()))
        counter[k] += 1
    answer = 0
    for k, c in counter.items():
        answer += (c * (c-1)) // 2
    print(answer)

def main2():
    N = int(input())
    counter = Counter("".join(sorted(input().strip())) for i in range(N))
    print(sum((c * (c-1)) // 2 for c in counter.values()))

def main3():
    print(sum((c * (c-1)) // 2 for c in Counter("".join(sorted(input().strip())) for i in range(int(input()))).values()))


main3()
