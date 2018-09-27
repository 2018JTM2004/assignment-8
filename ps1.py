#!/usr/bin/python3

"""Taking Inputs"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
row, column = list(map(int,input().split()))
# print(row,column)
"""Declaring empty lists"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

given = []
findings=[]
count = 0

"""Choosing one element and then findings number of S at its top,
   bottom, left and right"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

for i in range(row):
    s = list(input())
    given = given + [s]
# print(given)


for i in range(row):
    for j in range(column):
        if given[i][j]=="S":
                find_size=[]
                l,r,t,b=0,0,0,0
                x,y,w,z=1,1,1,1
                while j+y<column:
                    if given[i][j+y]!='S':
                        break
                    else:
                        r+=1
                        y+=1
                find_size.append(r)
                while j-x>0:
                    if given[i][j-x]!='S':
                        break
                    else:
                        l+=1
                        x+=1
                find_size.append(l)
                while i+w<row:
                    if given[i+w][j]!='S':
                        break
                    else:
                        t+=1
                        w+=1
                find_size.append(t)
                while i-w>0:
                    if given[i-w][j]!='S':
                        break
                    else:
                        b+=1
                        z+=1
                find_size.append(b)

                findings.append(min(find_size))
# count+=1
# print(count)

print(findings)
max_size = (max(findings)*4)+1
print(max_size,"1")
