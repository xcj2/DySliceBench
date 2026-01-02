import sys, os
import collections

MOD = 10 ** 9 + 7


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def solve(input_stream):
  N = read_int(input_stream)
  S = input_stream.readline().strip()

  ans = ""
  for char in S:
    index = alphabet.find(char)
    ans += alphabet[ (index + N) % len(alphabet)]
  return [ans]

def read_ints(input_stream):
  return [i for i in map(int, input_stream.readline().strip().split())]

def read_int(input_stream):
  return int(input_stream.readline().strip())


if __name__ == "__main__":
    outputs = solve(sys.stdin)
    for line in outputs:
      print(line)