#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check(dif, B):
    cnt_dif = 0
    for i in B:
        if(int(i) >= dif):
            cnt_dif += 1
    return cnt_dif
    
def check2(A, B, K):
    for i in A:
        amin = min(A)
        cnt = A.count(amin)
        dif = K - int(amin)
        for j in range(cnt):
            A.remove(amin)
        if(check(dif, B) < cnt):
            return False
    return True

T = int(input())

for i in range(T):
    line1 = input().split()
    N = int(line1[0])
    K = int(line1[1])
    A = input().split()
    B = input().split()
    
    if(check2(A,B,K)):
        print("YES")
    else:
        print("NO")