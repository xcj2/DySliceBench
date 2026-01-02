###############################################################################

from bisect import bisect_left as binl

def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def modadd(x, y):
    global mod
    return (x + y) % mod


def modmlt(x, y):
    global mod
    return (x * sy) % mod


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


###############################################################################


counts_3 = {
  "CAA": 1,
  "CTT": 1,
  "TTT": 1,
  "GGC": 1,
  "CGT": 1,
  "GTG": 1,
  "ACC": 1,
  "GCA": 1,
  "TTC": 1,
  "TCA": 1,
  "GGT": 1,
  "GTT": 1,
  "CAG": 1,
  "AAT": 1,
  "TAA": 1,
  "TAG": 1,
  "CCA": 1,
  "GCT": 1,
  "CTA": 1,
  "TCT": 1,
  "TTG": 1,
  "ATT": 1,
  "CAT": 1,
  "GAA": 1,
  "ATA": 1,
  "CCC": 1,
  "GCG": 1,
  "TTA": 1,
  "ACA": 1,
  "AGT": 1,
  "AGG": 1,
  "AGA": 1,
  "CCG": 1,
  "ATG": 1,
  "GAG": 1,
  "AAA": 1,
  "TCC": 1,
  "AAG": 1,
  "GCC": 1,
  "ACT": 1,
  "TGG": 1,
  "CTC": 1,
  "TCG": 1,
  "TGT": 1,
  "CGC": 1,
  "TAC": 1,
  "TAT": 1,
  "CGG": 1,
  "GGG": 1,
  "TGA": 1,
  "CCT": 1,
  "AAC": 1,
  "CGA": 1,
  "GTC": 1,
  "ATC": 1,
  "GGA": 1,
  "CAC": 1,
  "CTG": 1,
  "GAT": 1,
  "TGC": 1,
  "GTA": 1
}


mod = 10**9 + 7


def main():
    n = intin()

    all_ok = []
    not_c = []
    not_g = []
    for suffix in counts_3:
        if suffix == 'ATG' or suffix == 'AGG' or suffix == 'AAG':
            not_c.append(suffix)
        elif suffix == 'AGT':
            not_c.append(suffix)
        elif 'T' in suffix[1:]:
            all_ok.append(suffix)
        elif suffix[1:] == 'AA' or suffix[1:] == 'GG' or suffix[1:] == 'CC':
            all_ok.append(suffix)
        elif suffix[1:] == 'AG' or suffix[1:] == 'GA':
            not_c.append(suffix)
        elif suffix[1:] == 'AC':
            not_g.append(suffix)
        else:
            all_ok.append(suffix)

    suffix_counts = {3: counts_3}

    for i in range(4, 101):
        prev_count = suffix_counts[i-1]
        suffix_count = {}
        for suffix, count in prev_count.items():
            if suffix in all_ok:
                charlist = ['A', 'C', 'G', 'T']
            if suffix in not_c:
                charlist = ['A', 'G', 'T']
            if suffix in not_g:
                charlist = ['A', 'C', 'T']
            for c in charlist:
                new_suffix = suffix[1:] + c
                suffix_count.setdefault(new_suffix, 0)
                suffix_count[new_suffix] = modadd(suffix_count[new_suffix], count)
        suffix_counts[i] = suffix_count

    suffix_count = suffix_counts[n]

    ans = 0
    for i, count in suffix_count.items():
        ans = modadd(ans, count)

    print(ans)


if __name__ == '__main__':
    main()
