class segtree:
  def __init__(self, initArr, segfunc, idele):
    n = len(initArr)
    stn = 2**((n - 1).bit_length() + 1) - 1
    arr =  [idele for i in range(stn)]
    arr[stn//2:stn//2+n] = initArr
    for i in range(stn-1, 1, -2):
      arr[(i-1)//2] = segfunc(arr[i-1], arr[i])
  
    self.arr = arr
    self.segfunc = segfunc
    self.idele = idele
  
  def update(self, idx, val):
    idx += len(self.arr)//2
    self.arr[idx] = val
    while idx > 0:
      idx = (idx-1)//2
      self.arr[idx] = self.segfunc(self.arr[idx*2+1], self.arr[idx*2+2])
    return None

  def query(self, x, y, i=0, l=0, r=-1): # [x, y)の半開区間を探索
    if r < 0: r = len(self.arr)//2 + 1
    if r <= x or y <= l: return self.idele
    if x <= l and r <= y: return self.arr[i]
    return self.segfunc(
      self.query(x, y, 2*i+1, l, (l+r)//2),
      self.query(x, y, 2*i+2, (l+r)//2, r)
    )
N, Q = map(int, input().split())
st = segtree(list([2**31-1]*N), min, 2**31-1)

for q in range(Q):
  com, x, y = map(int, input().split())
  if com:
    print(st.query(x, y+1))
  else:
    st.update(x, y)
