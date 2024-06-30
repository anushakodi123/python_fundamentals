import itertools
from operator import pow

counter = itertools.count(10, 2)

for i in counter:
    print(i)

    if i == 20:
        break



l = ['A', 'B', 'C']
cycler = itertools.cycle(l)


for i, letter in enumerate(cycler):
    print(i, letter, sep=': ')

    if i ==20:
        break


string = "String"
repeater = itertools.repeat(string, 10)

# print(list(repeater))

for string in repeater:
    print(string)


numbers = [1, 2, 3, 4, 5]
accumulation = itertools.accumulate(numbers)

print(list(accumulation))



a = [1,2,3]
b = ['a', 'b', 'c']

combined = itertools.chain(a, b, a, b)

print(list(combined))


l = ['a', 'b', 'c', 'd']
selectors = [0, 1, 1, 0]

compressed = itertools.compress(l, selectors)
print(list(compressed))


l = [1, 2, 3, 4, 5, 6, 7, 1, 1, 2]

remaining = itertools.dropwhile(lambda n: n<3, l)
print(list(remaining))


l = range(100)
filtered = itertools.filterfalse(lambda n: n%10, l)
print(list(filtered))
l = [0, 1, False, True]
filtered = itertools.filterfalse(None, l)
print(list(filtered))


l = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('b', 5), ('c', 6)]

grouped = itertools.groupby(l, lambda k: k[0])

for key, values in grouped:
    print(key, list(values), sep=': ')


l = [1, 1, 2, 2, 2, 2, 3, 3, 3, 2, 2]

example = [list(g) for k, g in itertools.groupby(l)]
print(example)


l = ['a', 'b', 'c', 'd', 'e', 'f']
sliced = itertools.islice(l, 2)
sliced1 = itertools.islice(l, 2, None)
print(list(sliced))
print(list(sliced1))

# l = 'abcde'
# paired = itertools.pairwise(l)
# print(list(paired))

l = [(2,3), (2,4), (2,5)]
star_mapped = itertools.starmap(pow, l)
print(list(star_mapped))


l = [(1,2,3,4), (4,5), (6,7)]

def example(*args):
    temp = []
    for arg in args:
        temp.append(f'{arg}X')
    return temp

star_mapped = itertools.starmap(example, l)

print(list(star_mapped))


l = [1, 2, 3, 4, 5, 6, 1]
taken = itertools.takewhile(lambda a: a<4, l)
print(list(taken))


l = [1, 2, 3, 'a', 'b', 'c']

tee = itertools.tee(l, 3)

for it in tee:
    print(list(it))


a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [True, False]

zipped = itertools.zip_longest(a, b, c)

for a, b, c in zipped:
    print(a, b, c, sep=' : ')


a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [True, False]

zipped = zip(a, b, c)

for a, b, c in zipped:
    print(a, b, c, sep=' : ')



a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [True, False]

zipped = itertools.zip_longest(a, b, c, fillvalue= 'X')

for a, b, c in zipped:
    print(a, b, c, sep=' : ')



a=[1, 2, 3]
b=['a', 'b', 'c']

output = itertools.product(a, b)

for t in list(output):
    print(t)



a=[1, 2, 3]
b=['a', 'b', 'c']

output = itertools.product(a, b, repeat=2)

for t in list(output):
    print(t)



l = ['A', 'B', 'C']

permutations = itertools.permutations(l)
for g in list(permutations):
    print(*g, sep=' ')



l = ['A', 'B', 'C']

permutations = itertools.permutations(l)
for g in list(permutations):
    print(g, sep=' ')


l = ['A', 'B', 'C']

permutations = itertools.permutations(l, 2)
for g in list(permutations):
    print(g, sep=' ')


l=[0,1,2,3]
combinations = itertools.combinations(l, 2)

for g in list(combinations):
    print(g)


l=[0,1,2,3]
combinations = itertools.combinations_with_replacement(l, 3)

for g in list(combinations):
    print(g)