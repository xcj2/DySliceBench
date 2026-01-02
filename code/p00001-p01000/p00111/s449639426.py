# Aizu Problem 0111: Doctor's Memorable Code
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


def bin5(k):
    b = bin(k)[2:]
    while len(b) < 5:
        b = '0' + b
    return b


CODE1 = {' ': '101', "'": '000000', ",": '000011', '-': '10010001',
         '.': '010001', '?': '000001',
         'A': '100101', 'B': '10011010', 'C': '0101', 'D': '0001',
         'E': '110', 'F': '01001', 'G': '10011011', 'H': '010000',
         'I': '0111', 'J': '10011000', 'K': '0110', 'L': '00100',
         'M': '10011001', 'N': '10011110', 'O': '00101', 'P': '111',
         'Q': '10011111', 'R': '1000', 'S': '00110', 'T': '00111',
         'U': '10011100', 'V': '10011101', 'W': '000010',
         'X': '10010010', 'Y': '10010011', 'Z': '10010000'}
CODE1_rev = {value: key for key, value in CODE1.items()}

CODE2 = {bin5(k): chr(65+k) for k in range(26)}
symbols = [' ', '.', ',', '-', "'", '?']
for k in range(len(symbols)):
    CODE2[bin5(26+k)] = symbols[k]
CODE2_rev = {value: key for key, value in CODE2.items()}


def encode(string):
    enc = ''.join([CODE1[char] for char in string])
    while len(enc) % 5 != 0:
        enc += '0'
    return ''.join([CODE2[enc[5*k:5*k+5]] for k in range(len(enc) // 5)])

def decode(string):
    bitstring = ''.join([CODE2_rev[char] for char in string])
    decoded = ""
    while len(bitstring) > 0:
        k = 0
        while True:
            k += 1
            cand = bitstring[:k]
            if cand in CODE1_rev:
                decoded += CODE1_rev[cand]
                bitstring = bitstring[k:]
                break
            if k >= len(bitstring):
                return decoded
    return decoded


for line in sys.stdin:
    print(decode(line.replace('\n', '')))