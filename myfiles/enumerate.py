print(type(enumerate(['a', 'b', 'c', 'd'], 2)))
print(list(enumerate(['a', 'b', 'c', 'd'])))
print(tuple(enumerate(['a', 'b', 'c', 'd'], 5)))
print(dict(enumerate(['a', 'b', 'c', 'd'], 10)))
print('*'*25)
i = enumerate(['a', 'b', 'c'])
print(next(i))
print(next(i))
print('*'*25)
print(next(i, 0))
print(next(i, 0))
print('*'*25)
def foo(n):
     while 1:
        print('Before:', n)
        yield n + 1
        print('Yielded:', n)
        print('after:', n)

bar = foo(5)
print(bar.__next__())
print(bar.__next__())


print('*'*25)
print(next(bar))
print(next(bar))
print('*'*25)
print('*'*25)
print('*'*25)
print('*'*25)
print('*'*25)
print('*'*25)
