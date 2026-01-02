from itertools import chain

alph = "abcdefghijklmnopqrstuvwxyz"
# s = input()

def solve1(s):
    cands = [s]
    for c in reversed(alph[:-1]):
        cands = chain.from_iterable(
            [candidates(s, c) for s in cands]
        )

    cands = list(cands)
    cands.sort()
    print(len(cands))
    if len(cands) > 10:
        for s in cands[:5]:
            print(s)
        for s in cands[-5:]:
            print(s)
    else:
        for s in cands:
            print(s)
            
            
def next_char(c):
    return chr(ord(c)+1)

def candidates(string, key):
    nex = next_char(key)
    flag = False
    for i, c  in enumerate(string):
        if c == nex:
            flag = True
            break

        if c != key:
            continue

        yield string[:i] + nex + string[i+1:]

    if not flag:
        yield string
            



while True:
    s = input()
    if s == "#":
        break
    solve1(s)