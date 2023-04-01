import random,os,sys,time

Nums = 1234567890
Computed_nums = []


#      0   1   2   3   4   5   6   7   8   9
l1 = ["a","b","c","d","e","f","g","h","i","j"]
l2 = ["K","L","M","N","O","P","Q","R","S","T"]
l3 = ["!","@","#","$","%","^","&","*","-","~"]

Encoder_value = random.randint(0,9)


for i in str(Nums):
    pointer = int(i)+Encoder_value
    if pointer >= 10:
        pointer = pointer - 10

    Hash = random.randint(1,3)

    if Hash == 1:
        Computed_nums.append(l1[pointer])
    if Hash == 2:
        Computed_nums.append(l2[pointer])
    if Hash == 3:
        Computed_nums.append(l3[pointer])

print(Encoder_value)

for j in Computed_nums:print(j,end="")


