def with_prev(filt, prev, ad=None):
  def _filt(x):
    nonlocal prev
    if filt(x, prev):
      prev = x
      return ad(x) if ad else True
    return False
  return _filt

def solve():
  N, K, C = map(int, input().split())
  workable = [i for i, s in enumerate(input(), 1) if s=="o"]
  
  if len(workable) == K:
    return workable
  
  filt = with_prev((lambda x,p:p-x>C), workable[-1]+C+1)
  latest = set(filter(filt, reversed(workable)))

  if len(latest) > K:
    return []
  
  filt = with_prev((lambda x,p:x-p>C), -C-1, latest.__contains__)
  return filter(filt, workable)

print("\n".join(map(str, solve())))
