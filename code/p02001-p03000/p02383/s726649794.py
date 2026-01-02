#!/usr/bin/python3
# -*- coding: utf-8 -*-

def rotate_n(p):
    temp = p['top']
    p['top'] = p['south']
    p['south'] = p['bot']
    p['bot'] = p['north']
    p['north'] = temp

def rotate_s(p):
    temp = p['top']
    p['top'] = p['north']
    p['north'] = p['bot']
    p['bot'] = p['south']
    p['south'] = temp

def rotate_e(p):
    temp = p['top']
    p['top'] = p['west']
    p['west'] = p['bot']
    p['bot'] = p['east']
    p['east'] = temp

def rotate_w(p):
    temp = p['top']
    p['top'] = p['east']
    p['east'] = p['bot']
    p['bot'] = p['west']
    p['west'] = temp

import sys

face = sys.stdin.readline().split()
command = sys.stdin.readline().strip()

position = {'top':face[0], 'bot':face[5], 'east':face[2],
            'west':face[3], 'south':face[1], 'north': face[4]}

for roll in command:
    if roll == 'N':
        rotate_n(position)
    elif roll == 'S':
        rotate_s(position)
    elif roll == 'E':
        rotate_e(position)
    elif roll == 'W':
        rotate_w(position)
    else:
        raise ValueError

print(position['top'])

