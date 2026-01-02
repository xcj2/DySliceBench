def I():return input()
def II():return int(input())
def LI():return list(map(int, input().split()))
def L():return input().split()

def count_num(lis):
    v = {}
    for i in lis:
        if i not in v.keys():
            v[i] = 1
        else:
            v[i] += 1
    return v
def dict_to_list(dic):
    ret = []
    for i in dic.keys():
        ret.append([i,dic[i]])
    return ret

def main():
    n = II()
    e = n//2
    o = e + n%2

    v = LI()
    v_o = count_num(v[::2])
    v_e = count_num(v[1::2])
    cnt_o = dict_to_list(v_o)
    cnt_e = dict_to_list(v_e)
    cnt_o.sort(key=lambda x: x[1], reverse=True)
    cnt_e.sort(key=lambda x: x[1], reverse=True)
    
    cnt_o.append([0,0])
    cnt_e.append([0,0])
    if cnt_e[0][0] != cnt_o[0][0]:
        ans = (e - cnt_e[0][1]) + (o - cnt_o[0][1])
    else:
        ans = min((e-cnt_e[0][1]) + (o-cnt_o[1][1]), (e-cnt_e[1][1]) + (o-cnt_o[0][1]))
    print(ans)

if __name__ == '__main__':
    main()