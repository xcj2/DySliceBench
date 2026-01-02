def calc_seq(xs):
    seq = []
    count = 1
    for i in range(0, len(xs)-1):
        if xs[i] == xs[i+1]:
            count += 1
        else:
            seq.append(count)
            count = 1
    seq.append(count)
    return seq

def form_seq(xs):
    seq = calc_seq(xs)
    if xs[0] == 0:
        seq.insert(0, 0)
    if len(seq) % 2 == 0:
        seq.append(0)
    return seq

def main(n, k, xs):
    seq = form_seq(xs)
    m = len(seq)
    i = 1
    if i + 2*k > m:
        print(n)
        return
    j = i - 1
    val = sum(seq[j:j+2*k+1])
    biggest = val
    i += 2
    while i + 2*k <= m:
        j = i - 1
        val += seq[j+2*k-1] + seq[j+2*k] - seq[j-2] - seq[j-1]
        if biggest < val:
            biggest = val
        i += 2
    print(biggest)

n, k = list(map(int, input().split()))
xs = list(map(int, list(input())))

main(n, k, xs)