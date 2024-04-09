from collections import deque

# import modules_06 as fibo

# fibonacci = fibo.fib(10)
# print(fibonacci)

from modules_06 import fib2

print(fib2(10))

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#append
fruits.append('grape')
print(fruits)

#extend

fruits.extend(('cherry', 'pineapple'))
print(fruits)

#insert
fruits.insert(1, 'watermelon')
print(fruits)

#remove
fruits.remove('banana')
print(fruits)
# fruits.remove('hi') #error

#pop
fruits.pop()
print("popppp", fruits)
fruits.pop(4)
print("popp1", fruits)
# fruits.pop(11)

#index
numbers = [1, 2, 3, 4, 5]
index = numbers.index(3)
print(index)

numbers = [1, 2, 3, 4, 3, 2, 1]
index = numbers.index(3, 2, 5)
print(index)

#count
numbers = [1, 2, 3, 4, 3, 2, 1]
print(numbers.count(3))

#sort
fruits.sort()
print(fruits)

#reverse
fruits.reverse()
print(fruits)

#copy
alphabets = ['a', 'b', 'c', 'd']
alpha = alphabets.copy()
print(alpha)
alphabets.pop(1)
print(alphabets)

#clear
alphabets.clear()
print(alphabets)

#List as Queue
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

#List comprehensions
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)


squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])


#zip
print(list(zip(*matrix)))

countries = ["India", "UK", "USA", "Canada"]
capitals = ["Delhi", "London", "Washington DC", "Ottawa"]
hi = "hello"

country_capital = zip(countries, capitals, hi)

print(country_capital)
print(list(country_capital))

#del statement

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[:]
print(a)
# del a

#Tuples and Sequences
t = 12345, 54321, 'hello!'
print(t[0])


#sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a

print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                              # letters in both a and b
print(a ^ b)                              # letters in a or b but not both

#Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))

print(sorted(tel))

print('guido' in tel)

print('jack' not in tel)


print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x**2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))