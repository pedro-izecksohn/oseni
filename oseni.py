#!/usr/bin/python3
import random
seed=int(input("Enter the seed: "))
random.seed(seed)
l1=[]
l2=[]
lt=[]
while len(l1)<16:
    n=random.randint(0,255)
    if n in lt:
        continue
    lt.append(n)
    l1.append(n)
#print(l1)
while len(l2)<16:
    n=random.randint(0,255)
    if n in lt:
        continue
    lt.append(n)
    l2.append(n)
#print(l2)
text=input("Enter the text: ")
ba=bytearray(text,encoding="UTF-8")
#print(ba)
output=[]
for c in ba:
    lower=c&15
    #print("lower=",lower)
    upper=(c&240)>>4
    #print("upper=",upper)
    o=c^l1[lower]^l2[upper]
    output.append(o)
print(output)
