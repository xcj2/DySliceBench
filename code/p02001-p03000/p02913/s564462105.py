import sys
sys.setrecursionlimit(10**9)


class RollingHash:

    def __init__(self,string):
        base1 = 1007
        mod1 = 10**9+7

        base2 = 2009
        mod2 = 10**9+9

        self.string = string
        n = len(string)
        hash1 = [0]*(n+1)
        power1 = [1]*(n+1)

        hash2 = [0]*(n+1)
        power2 = [1]*(n+1)
        for i,e in enumerate(string):
            hash1[i+1] = (hash1[i]*base1 + ord(e))%mod1
            power1[i+1] = (power1[i]*base1)%mod1
            hash2[i+1] = (hash2[i]*base2 + ord(e))%mod2
            power2[i+1] = (power2[i]*base2)%mod2

        self.hash1 = hash1
        self.power1 = power1
        self.hash2 = hash2
        self.power2 = power2
        self.base1 = base1
        self.mod1 = mod1
        self.base2 = base2
        self.mod2 = mod2

    def calc(self,i,j):
        ans = ((self.hash1[j]-self.hash1[i]*self.power1[j-i]%self.mod1)%self.mod1)*(10**10)
        ans += (self.hash2[j]-self.hash2[i]*self.power2[j-i]%self.mod2)%self.mod2
        return ans

def main():
    N = int(input())
    S = input()

    rh = RollingHash(S)


    ans = 0
    l = 0
    r = N


    while r-l > 1:
        mid = (l+r)//2
        seen = set()
        dic = {}
        found = False
        for i in range(N-mid+1):
            if not i < i+mid-1: continue

            hash = rh.calc(i,i+mid-1)
            # print(hash,i,i+mid-1,mid)
            if hash in seen:
                for _i,j in dic[hash]:
                    if j < i and S[_i:j+1] == S[i:i+mid]:
                        ans = max(ans,mid)
                        found = True
                        break
                else: continue

                dic[hash].append((i,i+mid-1))
                break
            else:
                dic[hash] = [(i,i+mid-1)]
                seen.add(hash)


        if found:
            l = mid
        else:
            r = mid

    print(ans)



if __name__ == "__main__":
  main()