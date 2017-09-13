#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Chelsea Parlett & Chris Watkins
# Student ID: 2298930 & 1450263
# Email: parlette@chapman.edu & watki115@mail.chapman.edu
# Course: CS520 Fall 2017
# Assignment: Classwork 3
###

def fibonacci(n):
    try:
        int(n)
    except:
        print("this isn't a number")
    if n <= 0:
        print("you put in a negative number or 0")
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
            l = j
            j = k + j
            k = l
    return fibList
        