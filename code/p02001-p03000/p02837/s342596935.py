# -*- coding: utf-8 -*-
    
################ DANGER ################
test = ""
#test = \
"""
3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0
ans 0
"""

"""
3
1
2 1
1
1 1
1
2 0
ans 2
"""

"""
2
1
2 0
1
1 0
ans 1
"""
########################################
test = list(reversed(test.strip().splitlines()))
if test:
    def input2():
        return test.pop()
else:
    def input2():
        return input()
########################################

n = int(input2())
a = [None] * (n+1)
for i in range(1, n+1):
    ai = int(input2())
    a[i] = [tuple(map(int, input2().split())) for i in range(ai)]
    

def bitsearch(bit, *, start=0):
    end = 2 ** bit
    len0 = len(format(end, "b"))
    return [format(i, "b").zfill(len0) for i in range(start, end)] 


cand = [0]
for b in bitsearch(n):
    lie, i = 0, 1
    while (not lie) and i < n+1:
        for c in a[i]:
            if int(b[i]) and c[1] ^ int(b[c[0]]):
                lie += 1            
        i += 1
        
    if not lie:
        cand.append(b.count("1"))
        
print(max(cand))
        