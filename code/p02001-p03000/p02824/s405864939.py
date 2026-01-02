import sys
class IoTool:  # a tool for input redirection 
    DEBUG = 0
    def _reader_dbg():
        with open('./input.txt', 'r') as f:
            lines = f.readlines()
        for l in lines: yield l.strip() 
    def _reader_oj():  
        return iter(sys.stdin.read().split('\n'))
    reader = _reader_dbg() if DEBUG else _reader_oj()
    def read(): return next(IoTool.reader)

input = IoTool.read

def main():
    n, m, v, p = map(int, input().split())
    val = list(map(int, input().split()))
    val.sort(reverse=True)
    ans, presum, v = p, val[p-1], v-p+1
    for i in range(p, n):
        if val[i] + m < val[p-1] or (val[i] + m)*(i-p+1) - presum < m*(v-1-(n-i-1)):
            break
        presum += val[i]
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()
