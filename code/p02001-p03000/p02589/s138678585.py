import sys

sys.setrecursionlimit(10**7)

N = int(input())
S = []
a = ord('a')
for _ in range(N):
  S.append([ord(c) - a for c in input()][::-1])

_end = -1  #'_'
_count = -2 #'#'
def get_count(root):
  to_visit = [root]
  while to_visit:
    current = to_visit[-1]
    if _count in current:
      to_visit.pop()
      continue
    else:
      done = True
      c = [0] * 26 + [1 if _end in current else 0]
      for k, n in current.items():
        if k in (_end, _count):
          continue
        if _count not in n:
          done = False
          break
        if k not in (_end, _count):
          cc = n[_count]
          #print(k, cc)
          for i, v in enumerate(cc):
            if i == k:
              c[k] += cc[-1]
            else:
              c[i] += v
      if done:
        current[_count] = c
        to_visit.pop()
      else:
        for k, v in current.items():
          if k not in (_end, _count):
            to_visit.append(v)
  return current[_count]
        
  
  
  if _count in root:
    return root[_count]
  else:
    c = [0] * 26 + [1 if _end in root else 0]
    for k, n in root.items():
      if k not in (_end, _count):
        cc = get_count(n)
        #print(k, cc)
        for i, v in enumerate(cc):
          if i == k:
            c[k] += cc[-1]
          else:
            c[i] += v
    root[_count] = c
    return c
    
def make_trie(words):
  root = dict()
  for word in words:
    current_dict = root
    for letter in word:
      #letter = ord(letter)
      current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end
 
  return root

def get_subtree(trie, word):
  current_dict = trie
  for letter in word:
    #letter = ord(letter)
    if letter not in current_dict:
      return {}
    current_dict = current_dict[letter]
  return current_dict
  
def in_trie(trie, word):
  return _end in get_subtree(trie, word)

trie = make_trie(S)
#print(trie)
#print(get_subtree(trie, 'cy'))
#print(in_trie(trie, 'cy'))
#print(in_trie(trie, 'cyx'))

ans = 0
for s in S:
  count = get_count(get_subtree(trie, s[:-1]))
  #print(s, '#', count[s[-1]], count)
  ans += count[s[-1]]

print((ans - N))
                  
