#!/usr/bin/python3
"""Defining rotate function"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
def rotate(lst, x):
    new=lst.copy()
    for i in range(x):
        new.insert(0,new.pop(-1))
    return new

"""Taking Inputs"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
m1,m2,m3 = input().split(" ") #Input m1 m2 and m3
k1 = int(m1)
k2 = int(m2)
k3 = int(m3)
input_string = input("Enter the message to be decrypted : ")

"""Making different groups"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
group1 = "abcdefghi" #Making group1
group2 = "jklmnopqr" #Making group2
group3 = "stuvwxyz_" #Making group3

"""Updating elements from input into different lists."""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
p1,p2,p3=[],[],[]
for i in input_string:
    if i in group1:
        p1.append(i)
    if i in group2:
        p2.append(i)
    if i in group3:
        p3.append(i)
print(p1)
print(p2)
print(p3)
"""Rotate groups by specified amounts."""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
rp1 = rotate(p1,k1) #rotating by specified amounts
rp2 = rotate(p2,k2) #rotating by specified amounts
rp3 = rotate(p3,k3) #rotating by specified amounts

# print(p1,p2,p3)
print(rp1,rp2,rp3)
decrypted_message="" #Taking empty strings

""""~~~~~~~~~~~~~~~Writing the decrypted_message~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
for char in input_string:
    if char in group1:
        for ind,i in enumerate(p1):
            # print(ind,i)
            if i==loop:
                decrypted_message=decrypted_message+rp1[ind]
    if (set(loop) & set(group2)):
        for ind,i in enumerate(p2):
            if i==loop:
                decrypted_message=decrypted_message+rp2[ind]
    if (set(loop) & set(group3)):
        for ind,i in enumerate(p3):
            if i==loop:
                decrypted_message=decrypted_message+rp3[ind]

"""Printing decrypted message"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
print(decrypted_message)
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
