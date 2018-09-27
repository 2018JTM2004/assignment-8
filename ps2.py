#!/usr/bin/python3
def rotate(lst, x):
    for i in range(x):
        lst.insert(0,lst.pop(-1))
    return lst


m1,m2,m3 = input().split(" ") #Taking input values of k1, k2 and k3
k1 = int(m1)
k2 = int(m2)
k3 = int(m3)
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

rp1,rp2,rp3 = rotate(p1,k1),rotate(p2,k2),rotate(p3,k3)

decrypted_message=""
for loop in input_string:
    if (set(loop) & set(group1)):
        for ind,i in enumerate(p1):
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


print(decrypted_message)
# print(rp1)
# print(rp2)
# print(rp3)
