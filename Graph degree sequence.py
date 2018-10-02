# -*- coding: utf-8 -*-
#This code checks if your entered graph degree sequence is valid
#d= [3,2,2,2]
print("Enter degree sequence as numbers separated by commas")
d = [int(x) for x in input().split(",")]
print(d)
#print(len(d))
d.sort()
degseq=1
while len(d)>0:
    d.sort()
    last=d.pop()
    #print(last)
    #print(degseq)
    if last>len(d):
        degseq=0
        break
    for i in range(len(d)-1,len(d)-last-1,-1):
        if d[i]>0:
            d[i]=d[i]-1
        else:
            degseq=0
if degseq==1:
    print("Is a valid degree sequence")
else:
    print("Not a valid degree sequence")
