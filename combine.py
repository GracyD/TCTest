#!/usr/bin/python
import sys
import copy

n = int(raw_input("Please enter the number scope: "))
m = int(raw_input("Please enter how many numbers you want to choose from the pool: "))

a = []

for i in range(1,n+1):
    a.append(i)


def combine(l, n): 
    answers = []
    one = [0] * n 
    def next_c(li = 0, ni = 0): 
        if ni == n:
            answers.append(copy.copy(one))
            return
        for lj in xrange(li, len(l)):
            one[ni] = l[lj]
            next_c(lj + 1, ni + 1)
    next_c()
    return answers

print combine(a, m)
