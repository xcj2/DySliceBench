from functools import reduce
p = 1000000007  #ここを変える
ccache = []
inv_ccache = []
N = 1000000
def powmod(a, n):
    global p
    res = 1
    tmp=a
    while n>0:
        if n & 1 == 1:
            res = (res * tmp) % p
        n=n//2
        tmp = tmp * tmp % p
    return res
def invmod(n):
    return powmod(n, p - 2)
def cmod(n, r):
    global p
    global ccache
    global inv_ccache
    global N
    if len(ccache) == 0:
      ccache.append(1)
      inv_ccache.append(1)
      for i in range(N):
        ccache.append(ccache[i]*(i+1)%p)
        inv_ccache.append(1)
      inv_ccache[N]=invmod(ccache[N])
      for i in range(N-1):
        inv_ccache[N-1-i]=inv_ccache[N-i]*(N-i)%p
    if r > n or r < 0:
        return 0
    if r > n // 2:
        return cmod(n, n - r)
    return ccache[n]*inv_ccache[r]%p*inv_ccache[n-r]%p
 
n = int(input())
adj_of = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj_of[a - 1].append(b - 1)
    adj_of[b - 1].append(a - 1)
stack = [(0, -1)] # root, excludee
course = []
while len(stack) > 0:
    popped = stack.pop()
    course.append(popped)
    for adj in adj_of[popped[0]]:
        if adj != popped[1]:
            stack.append((adj, popped[0]))
sizes = [{} for _ in range(n)] #size, pattern_num
pattern_nums = [{} for _ in range(n)]
for step in reversed(course):
    size = 1
    pattern_num = 1
    for adj in adj_of[step[0]]:
        if adj != step[1]:
            size += sizes[adj][step[0]]
            pattern_num *= pattern_nums[adj][step[0]] * cmod(size - 1, sizes[adj][step[0]]) % p
            pattern_num %= p
    sizes[step[0]][step[1]] = size
    pattern_nums[step[0]][step[1]] = pattern_num
 
#print(course)
#print(sizes)
#print(pattern_nums)
 
ans = [None] * n
for step in course:
    if step[0] == 0:
        ans[0] = pattern_nums[0][-1]
        continue
    #ans[step[0]] = pattern_nums[step[0]][step[1]] * pattern_nums[step[1]][step[0]]\
    #             * cmod(sizes[step[0]][step[1]] + sizes[step[1]][step[0]], sizes[step[0]][step[1]]) % p
    pattern_nums_step1_step0 = ans[step[1]] * invmod(cmod(n - 1, sizes[step[0]][step[1]]) % p * pattern_nums[step[0]][step[1]]) % p
    ans[step[0]] = pattern_nums[step[0]][step[1]] * pattern_nums_step1_step0 % p\
                 * cmod(n - 1, sizes[step[0]][step[1]] - 1) % p
 
for a in ans:
    print(a)
