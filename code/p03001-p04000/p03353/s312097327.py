

def read_input():
    s = input()
    k = int(input())
    return s, k


# sから、candsの間に挟まる文字列(長さl)を探す
def search_insertion(s, cands, l):
    result = []

    for i in range(len(s)):
        for c in cands:
            if s[i:i+l].startswith(c):
                result.append(s[i:i+l])

    cands.extend(result)
    cands = list(set(cands))
    return cands


def sort_s(cands):
    t = [[c for c in s] for s in cands]
    t.sort()
    return [''.join(s) for s in t]


def submit():
    s, k = read_input()

    cands = list(set([c for c in s]))
    precands = None
    for i in range(2, len(s) + 1):
        cands = search_insertion(s, cands, i)
        cands = sort_s(cands)
        cands = cands[:k]

        if precands == cands:
            break
        precands = cands[:]

    print(cands[-1])

if __name__ == '__main__':
    submit()
