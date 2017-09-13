#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibonacci(n):
    k = 1
    j = 1
    fibList = []
    if n == 1:
       # print([1])
        return [1]
    elif n == 2:
       # print([1,1])
        return [1,1]
    else:
        fibList.append(1)
        fibList.append(1)
        for i in range(3,n+1):
            fibList.append(k+j)
            k = j
            j = j+k
    return fibList

        