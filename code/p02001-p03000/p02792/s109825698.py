N = int(input())


def extract_first(i):
    return str(i)[0]

def extract_last(i):
    return str(i)[-1]

def get_key(first, last):
    return "{}-{}".format(first, last)

combi_map = {}
for i in range(0, 10):
    for j in range(0,10):
        combi_map[get_key(i, j)] = 0


for i in range(1, N+1):
    first = extract_first(i)
    last = extract_last(i)
    combi_map[get_key(first, last)] += 1

ans = 0
for i in range(1, 10):
    for j in range(i, 10):
        if i == j:
            ans += combi_map[get_key(i, j)] * combi_map[get_key(j, i)]
        else:
            ans += combi_map[get_key(i, j)] * combi_map[get_key(j, i)] * 2
print(ans)