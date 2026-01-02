n=int(input())
num_list1=list(map(str,input().split()))
num_list2=[]
input_list=[]

for k in num_list1:
    num_list2.append(k)
    input_list.append(k)


def bubble(num_list):
    i=0
    flag=True
    while flag:
        flag=False
        for j in range(len(num_list)-1,i,-1):
            if int(num_list[j-1][1])>int(num_list[j][1]):
                tmp=num_list[j-1]
                num_list[j-1]=num_list[j]
                num_list[j]=tmp
                flag=True
    return num_list 

def select(num_list):
    for i in range(0,len(num_list)):
        min=i
        for j in range(min+1,len(num_list)):
            if int(num_list[min][1])>int(num_list[j][1]):
                min=j
        tmp=num_list[i]
        num_list[i]=num_list[min]
        num_list[min]=tmp
    return num_list



def stable(input_list,output_list):
    for i in range(0,len(input_list)):
        for j in range(i+1,len(output_list)):
            for k in range(0,len(output_list)):
                for l in range(k+1,len(output_list)):
                    if input_list[i][1]==input_list[j][1] and input_list[i]==output_list[l] and input_list[j]==output_list[k]:
                        return "Not stable"
    return "Stable"

bubble=bubble(num_list1)
select=select(num_list2)


print(" ".join(bubble))
print(stable(input_list,bubble))
print(" ".join(select))
print(stable(input_list,select))
