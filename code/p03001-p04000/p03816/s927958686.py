from collections import Counter
def main():
    N = int(input())
    cards = list(map(int, input().split()))

    counter = Counter(cards)
    # print(counter)

    A = list(map(lambda x: x%2, counter.values()))

    pure= sum(1 for x in A if x == 1)
    needpairs = sum(1 for x in A if x == 0)
    # print(pure)
    # print(needpairs)

    answer = pure + needpairs - (1 if needpairs%2==1 else 0)
    print(answer)

def intifp(x):# {{{
    try:
        return int(x)
    except:
        return x# }}}

def strifp(x):# {{{
    try:
        return str(x)
    except:
        return x# }}}

if __name__ == "__main__":
    main()
