print("list comprension......................")
c=[i for i in [1, 2, 3, 4]]
print(c)
c=list(i for i in [1, 2, 3, 4])
print(c)
print("dict  comprension......................")
d={i:j for i, j in {1: 'a', 2: 'b'}.items()}
print(d)
print("tuple  comprension......................")
f=tuple(i for i in (1, 2, 3))
print(f)

print("iterators......................")
c=iter(i for i in (1, 2, 3))
print(next(c))
print(c.__next__())
print(c.__next__())

print("list iterators......................")
list1=[1,2,3,4,5,6,7]
list_iter=iter(list1)
for k in list_iter:
    print(k)

print("tuple iterators......................")
tuple1=(1,2,34,45,56,67,78)
tuple_iter=iter(tuple1)
for k in tuple_iter:
    print(k)

print("dictionary iterators......................")

mydict = {1:"apple",'a':"banana",'c':"cherry"}
myit = iter(mydict)

print(next(myit))
print(next(myit))
print(next(myit))

print("string iterators......................")

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("class MyNumbers **************************")
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("class MyNumbers StopIteration**************************")
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
