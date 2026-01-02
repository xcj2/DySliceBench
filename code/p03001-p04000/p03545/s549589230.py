from sys import stdin 

ABCD = stdin.readline().rstrip()
A = int(ABCD[0])
B = int(ABCD[1])
C = int(ABCD[2])
D = int(ABCD[3])

def func1(ABCD,k):
    if k==len(ABCD)-1:
        return [[ABCD[k]],["-"+ABCD[k]]]
    prev_output = func1(ABCD,k+1)
    output = []
    if k==0:
        for ele in prev_output:
            temp = [ABCD[k]]
            temp.extend(ele)
            output.append(temp)
        return output

    for ele in prev_output:
        temp = [ABCD[k]]
        temp.extend(ele)
        output.append(temp)

        temp = ["-"+ABCD[k]]
        temp.extend(ele)
        output.append(temp)
    return output

def search_combi(combinations):
    for combi in combinations:
        tot_sum = 0
        for ele in combi:
            tot_sum+=int(ele)
        if tot_sum==7:
            return combi

combinations = func1(ABCD,0)
#print("search_copmbi:",search_combi(combinations))
def make_answer(numbers):
    output_string=""
    for i,num in enumerate(numbers):
        num_int = int(num)
        if i==0:
            output_string += num
        else:
            if num_int<0:
                output_string += "-"+num[1]
            else:
                output_string += "+"+num
    return output_string+"=7"


print(make_answer(search_combi(combinations)))

        