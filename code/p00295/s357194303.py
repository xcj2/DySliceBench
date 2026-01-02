from collections import deque

def is_solved(puzzle):
  check1 = puzzle[0]
  for i in range(1, 9):
    if puzzle[i] != check1:
      return False

  check2 = puzzle[9]
  if puzzle[10] != check2 or puzzle[11] != check2:
    return False

  check3 = puzzle[12]
  if puzzle[13] != check3 or puzzle[14] != check3:
    return False

  return True


def myhash(p):
  ret = 0
  for i in range(len(p)):
    ret += 200 ** i * p[i]
  return ret

def spin1(p):
  r = [i for i in p]
  r[0], r[3], r[6], r[23], r[26], r[29] = p[23], p[26], p[29], p[0], p[3], p[6]
  r[9], r[20] = p[20], p[9]
  r[15], r[17] = p[17], p[15]
  return r

def spin2(p):
  r = [i for i in p]
  r[2], r[5], r[8], r[21], r[24], r[27] = p[21], p[24], p[27], p[2], p[5], p[8]
  r[11], r[18] = p[18], p[11]
  r[12], r[14] = p[14], p[12]
  return r

def spin3(p):
  r = [i for i in p]
  r[0], r[1], r[2], r[27], r[28], r[29] = p[27], p[28], p[29], p[0], p[1], p[2]
  r[14], r[15] = p[15], p[14]
  r[18], r[20] = p[20], p[18]
  return r

def spin4(p):
  r = [i for i in p]
  r[6], r[7], r[8], r[21], r[22], r[23] = p[21], p[22], p[23], p[6], p[7], p[8]
  r[12], r[17] = p[17], p[12]
  r[9], r[11] = p[11], p[9]
  return r

def main():
  
  spin_lst = [spin1, spin2, spin3, spin4]
  
  n = int(input())
  
  for i in range(n):
    puz = list(map(int, input().split()))
    
    dic = {}
    dic[myhash(puz)] = 0
  
    que = deque()
    que.append((puz, 0))
  
    while que:
      p, score = que.popleft()
      
      if is_solved(p):
        print(score)
        break
  
      for spin in spin_lst:
        spined = spin(p)
        h = myhash(spined)
        if not h in dic:
          dic[h] = score + 1
          que.append((spined, score + 1))

main()
