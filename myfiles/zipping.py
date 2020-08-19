from zipfile import ZipFile
with ZipFile("myfiles.zip", 'r') as zip:
    print(zip.printdir())
    data = zip.read("myfiles/examples3_dict_display.py")
    zip.extract("myfiles/examples3_dict_display.py",path='..//')

dict1={}
str1="the quick brown fox jumps on the lazy lazy brown brown fox"
list1=str1.split()
for k in list1:
    if k in dict1:
        dict1[k]+=1
    else:
        dict1[k]=1
print(dict1)


loc=5
def funnny():
    global loc
    loc=loc+1
    return(loc)


print(funnny())
