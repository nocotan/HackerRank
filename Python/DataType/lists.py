#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
arr = []

for i in range(n):
    line = input().split()
    cmd = line[0]

    if(cmd == "append"):
        arr.append(int(line[1]))
    elif(cmd == "insert"):
        arr.insert(int(line[1]), int(line[2]))
    elif(cmd == "remove"):
        arr.remove(int(line[1]))
    elif(cmd == "pop"):
        if(len(line) == 1):
            arr.pop()
        else:
            arr.pop(int(line[1]))
    elif(cmd == "sort"):
        arr.sort()
    elif(cmd == "reverse"):
        arr.reverse()
    elif(cmd == "print"):
        print(arr)
