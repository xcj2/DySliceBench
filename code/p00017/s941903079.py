import sys

idx2alpha = {idx:s for idx,s in enumerate('abcdefghijklmnopqrstuvwxyz .\n')}
alpha2idx = {s:idx for idx,s in enumerate('abcdefghijklmnopqrstuvwxyz .\n')}

def rotate(s):
    idx = [next_w(alpha2idx.get(w)) for w in s]
    new_s = [idx2alpha.get(i) for i in idx]
    return ''.join(new_s)

def next_w(w_idx):
    if 25 < w_idx:
        return w_idx
    w_idx += 1
    return w_idx % 26

def decrypt(s):
    for _ in range(26):
        if 'the' in s or 'this' in s or 'that' in s:
            return s
        else:
            s = rotate(s)
    return 'Failed to decript!'

def run():
    for line in sys.stdin:
        print(decrypt(line.strip()))

if __name__ == '__main__':
    run()


