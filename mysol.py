import re
hand=open('actual.txt')
numlist=[]
for line in hand:
    line=line.rstrip()
    stuff=re.findall(r'\d+',line)
    if len(stuff)==0:continue
    for k in stuff:
        num=int(k)
        numlist.append(num)
num=0
for k in numlist:
    num=num+int(k)
print(num)
