# coding: utf-8
def main():
    N,Q = map(int, input().split())
    s = input()
    ans = N
    command = []

    # print(char_list)

    for i in range(Q):
        t,d = input().split()
        command.append([t,d])

    r = binary_serch_R(command,s,N)
    #print(r)
    l = binary_serch_L(command,s,N)
    #print(l)
    ans = ans - (N-r) - (l+1)
    if ans < 0:
        ans = 0
    print(ans)

def simulation_R(command,s,now,N):
    for pair in command:
        if pair[0] == s[now]:
            if pair[1] == 'L':
                now -= 1
            elif pair[1] == 'R':
                now += 1
        if now < 0:
            return False
        elif now >= N:
            return True
    return False

def simulation_L(command,s,now,N):
    for pair in command:
        if pair[0] == s[now]:
            if pair[1] == 'L':
                now -= 1
            elif pair[1] == 'R':
                now += 1
        if now < 0:
            return True
        elif now >= N:
            return False
    return False


def binary_serch_R(command,s,N):
    left = 0
    right = N-1
    if simulation_R(command,s,left,N) :
        return -1
    if simulation_R(command,s,right,N) == False:
        return N

    while abs(right - left) > 1:
        mid = int((left+right)/2)
        # print(mid)
        if simulation_R(command,s,mid,N) :
            right = mid
        else :
            left = mid 
    return right

def binary_serch_L(command,s,N):
    left = 0
    right = N-1
    if simulation_L(command,s,left,N) == False :
        return -1
    if simulation_L(command,s,right,N):
        return N
        
    while abs(right-left) > 1:
        mid = int((left+right)/2)
        if simulation_L(command,s,mid,N) :
            left = mid
        else :
            right = mid 
    return left

if __name__ == "__main__":
    main()