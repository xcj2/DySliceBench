def print_ab(sent, a, b):
    res = sent[a:b + 1]
    return res

def reverse_ab(sent, a, b):
    top = sent[:a]
    las = sent[b+1:]
    tag = sent[a:b+1]
    n = len(tag)
    rev = ""
    for i in range(n):
        rev = rev + tag[n - i - 1]
    rev = top + rev + las
    return rev

def replace_abp(sent, a, b, p):
    top = sent[:a]
    las = sent[b+1:]
    rep = top + p + las
    return rep

#print(print_ab("xyz", 0, 2))
#print(reverse_ab("abcde", 1, 3))
#print(replace_abp("xyz", 0, 2, "abc"))

sent = input()
op = int(input())
results = []
for i in range(op):
    oder = list(map(str, input().split()))
    if oder[0] == "print":
        res = print_ab(sent, int(oder[1]), int(oder[2]))
        results.append(res)
    elif oder[0] == "reverse":
        sent = reverse_ab(sent, int(oder[1]), int(oder[2]))
    else:
        sent = replace_abp(sent, int(oder[1]), int(oder[2]), oder[3])

for s in results:
    print(s)
