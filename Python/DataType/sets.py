#!/usr/bin/env python
# -*- coding: utf-8 -*-

n1 = int(input())
set1 = set(input().split())
n2 = int(input())
set2 = set(input().split())

dif = set1.symmetric_difference(set2)
dif_list = map(int, list(dif))


for num in sorted(dif_list):
    print(num)