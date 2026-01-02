# coding: utf-8
# Here your code !

def operate_string():

    (method, i_first, i_last, str_new) = ("method", "i_first", "i_last", "replace string")

    #load data
    operations = []
    try:
        string = input().rstrip()
        _ = input()
        while(True):
            line = input().rstrip().split()
            operations.append({method : line[0], i_first : int(line[1]), i_last : int(line[2])})
            if len(line) > 3 :
                operations[-1].update({str_new : line[3]})
    except EOFError:
        pass
    except:
        return __inputError()

    #operate string
    for ope in operations:
        if ope[method] == "print" :
            print(string[ope[i_first]:ope[i_last]+1])
        elif ope[method] == "reverse" :
            string = reverse_string_by_index (string, ope[i_first], ope[i_last])
        elif ope[method] == "replace" :
            string = replace_string_by_index (string, ope[str_new], ope[i_first], ope[i_last])
        else :
            return __inputError()


def replace_string_by_index (str_raw, str_new, i_first, i_last):
    pre_post_info = __set_pre_post_string(str_raw, i_first, i_last)
    if pre_post_info["invalid index"] :
        return str_raw

    return pre_post_info["pre"] + str_new + pre_post_info["post"]

def reverse_string_by_index (str_raw, i_first, i_last):
    pre_post_info = __set_pre_post_string(str_raw, i_first, i_last)
    if pre_post_info["invalid index"] :
        return str_raw

    str_reversed = str_raw[i_last:i_first-1:-1]
    if i_first == 0 :
        str_reversed = str_raw[i_last::-1]

    return pre_post_info["pre"] + str_reversed + pre_post_info["post"]

def __set_pre_post_string (str_raw, i_first, i_last):

    info = {"pre" : "", "post" : "", "invalid index" : False}
    info["pre"]  = str_raw[:i_first]
    info["post"] = "" if (i_last == -1) else str_raw[i_last+1:]
    info["invalid index"] = ( len(info["pre"]) + len(info["post"]) >= len(str_raw) )
    
    return info

def __inputError():
    print("input Error")
    return -1

def __Test_reverse_string_by_index (lists):
    #list[index] = [str_raw, i_first, i_last]
    for item in lists:
        print(reverse_string_by_index(item[0], item[1], item[2]))

def __Test_replace_string_by_index (lists):
    #list[index] = [str_raw, str_new, i_first, i_last]
    for item in lists:
        print(replace_string_by_index(item[0], item[1], item[2], item[3]))


#test
if __name__ == "__main__" :
    
    operate_string()
    
    '''
    __Test_replace_string_by_index ([ ["abc","A",0,1], ["abc","A",-5,-1], ["abc","",1,1], ["","A",0,0],      ["abc","A",5,6] ])
    #expected results:                 "Ac",            "A",               "ac",           ""(string error),  "abc"(index error)
    
    __Test_reverse_string_by_index ([ ["abc",0,2], ["abc",-5,-1], ["abc",3,3] ])
    #expected results:                 "cba",       "cba",         "abc"(index error)
    '''
        