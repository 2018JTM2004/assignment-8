#!/usr/bin/python3
def rotate(lst, x):
    lst[:] =  lst[-x:] + lst[:-x]


k1,k2,k3 = input().split(" ") #Taking input values of k1, k2 and k3
input_string = input("Enter the message to be decrypted : ")
# list_input = list(input_string)
# print(input_character)

group1 = "abcdefghi"
group2 = "jklmnopqr"
group3 = "stuvwxyz_"

p1,p2,p3=[],[],[]

for loop in group1:
    if( set(loop) & set(input_string)):
        p1.append(loop)
for loop in group2:
    if( set(loop) & set(input_string)):
        p2.append(loop)
for loop in group3:
    if( set(loop) & set(input_string)):
        p3.append(loop)
print(p1)
print(p2)
print(p3)

rotate(p1,k1)
rotate(p2,k2)
rotate(p3,k3)

print(p1)
print(p2)
print(p3)
