#!/usr/bin/python3

"""Taking Inputs"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
row, column = list(map(int , input().split()))

l = []

for i in range(row):
    s = list(input())
    l = l + [s]
print(l)
# for index,item in enumerate(l):
