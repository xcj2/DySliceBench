n = int(input())
a = [int(aa) for aa in input().split()]

def add_entry(hist, aa):
    if aa in hist:
        hist[aa] += 1
    else:
        hist[aa] = 1


def make_hist(a):
    even_hist = {}
    odd_hist = {}

    for i in range(len(a)//2):
        add_entry(even_hist, a[2*i])
        add_entry(odd_hist, a[2*i+1])

    return even_hist, odd_hist


def get_sorted_hist(hist):
    return sorted(hist.items(), key=lambda x: -x[1])

eh, oh = make_hist(a)
seh = get_sorted_hist(eh)
soh = get_sorted_hist(oh)


if seh[0][0] != soh[0][0]:
    print(len(a) - seh[0][1] - soh[0][1])
else:
    if len(seh) == 1 and len(soh) == 1:
        print(len(a)//2)
    elif len(seh) == 1:
        print(len(a) - seh[0][1] - soh[1][1])
    elif len(soh) == 1:
        print(len(a) - soh[0][1] - seh[1][1])
    else:
        print(min(len(a) - seh[0][1] - soh[1][1], len(a) - soh[0][1] - seh[1][1]))
