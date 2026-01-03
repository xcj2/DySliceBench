def cin():
	return map(int,input().split())

def cino(test=False):
    if not test:
        return int(input())
    else:
        return input()
def cina():
  return list(map(int,input().split()))

def hashing(my_list):   
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1  
    return freq

a = cino(True)
a = list(a)
h = hashing(a)
check = False
for key, value in h.items():
    if value%2!=0:
        check = True
        break
if check:
    print("No")
else:
    print("Yes")

# print(ans)
# a = list(a)
# has = {}
# x,y = -1,-1
# for i in range(len(a)):
#     has[a[i]]=[0,0]

# for i in range(len(a)):
#     has[a[i]][0] += 1
#     if has[a[i]][0]==1:
#         has[a[i]][1] = i
#     temp1 = has[a[i]][0]
#     # print(temp1)
#     if i>2 and temp1>2:
#         temp = has[a[i]][1]
#         if temp1>(i-temp)//2:
#             x,y = temp+1,i+1
#             break
# print(x,y)


