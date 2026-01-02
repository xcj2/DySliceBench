
import time
import random
import collections
import bisect  

start = time.time()

def insert(list, n): 
    bisect.insort(list, n)  
    return list

def read_input():
  D = int(input())
  c = list(map(int, input().split()))
  s = [list(map(int, input().split())) for _ in range(D)]
  return D, c, s
D, c, s = read_input()

tests = [int(input()) - 1 for _ in range(D)]
M = int(input())
d = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]

#c = np.array(c)
#s = np.array(s)
#tests = np.argmax(s, axis=1)

def get_dates_for_tests(tests):
  dates_for_tests = [list([-1]) for _ in range(26)]
  for i, t in enumerate(tests):
    dates_for_tests[t].append(i)
  for t in range(26):
    dates_for_tests[t].append(D)
  return dates_for_tests

dates_for_tests = get_dates_for_tests(tests)

def get_score(tests):
  dates_for_tests = get_dates_for_tests(tests)
  score = 0
  d = [0]*26 #np.zeros(26, dtype=np.int64)
  for selected, S in zip(tests, s):
    d = [x+1 for x in d]#d += 1
    d[selected] = 0
    score += S[selected]
    for ct, dt in zip(c,d):
      score -= ct*dt# - (c * d).sum()
  return score

def score_diff(date, test):
  #print(date, test)
  before = tests[date]
  if test == before:
    return 0, None, None
  pos_diff = s[date][test] - s[date][before]
  new_index = bisect.bisect_left(dates_for_tests[test], date, 1)
  new_diff = c[test] * (dates_for_tests[test][new_index] - date) * (date - dates_for_tests[test][new_index-1])

  old_index = bisect.bisect_left(dates_for_tests[before], date, 1)
  #print(c[test], dates_for_tests[test])
  #print(c[before], dates_for_tests[before])
  old_diff = c[before] * (dates_for_tests[before][old_index+1] - date) * (date - dates_for_tests[before][old_index-1])
  
  total_diff = pos_diff + new_diff - old_diff
  #print(test, total_diff, pos_diff, new_diff, -old_diff)
  return total_diff, new_index, old_index

current_score = get_score(tests)
#print(d)
for date, test in d:
  total_diff, new_index, old_index= score_diff(date, test)
  current_score += total_diff
  del dates_for_tests[tests[date]][old_index]
  insert(dates_for_tests[test], date)
  tests[date] = test
  
  print(current_score)