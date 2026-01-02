class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


def f(tup1,tup2):
    tot=tup1[1]+tup2[1]
    if tup1[2]==1 and tup2[0]==1:
        tot+=1
    a=tup1[0]
    b=tup2[2]
    return (a,tot,b)



n,q=map(int,input().strip().split(" "))
s=input()
ar=[]
for i in s:
    if i=="A":
        ar.append((0,0,1))
    elif i=="C":
        ar.append((1, 0, 0))
    else:
        ar.append((0,0,0))
defa=(0,0,0)
seg=SegmentTree(ar,defa,f)
for _ in range(q):
    a,b=map(int,input().strip().split(" "))
    k=seg.query(a-1,b)
    print(k[1])




