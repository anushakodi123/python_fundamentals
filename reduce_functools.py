from functools import reduce

print(reduce(lambda x,y: x+y, [1,2,3,4,5], 10))

def add_it(x, y):
    return x+y

total = reduce(add_it, [1,2,3,4,5])
print(total)


max_value = reduce(lambda x, y: x if x> y else y, [], 0)
print(max_value)