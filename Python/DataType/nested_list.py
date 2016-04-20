#!/usr/bin/env python
# -*- coding: utf-8 -*-


n = int(input())

arr = [[]]

for i in range(n):
    name = str(input())
    score = int(input())
    carr = [name, score]
    arr.append(carr)
    

del arr[0]
print(arr)