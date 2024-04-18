def range_2(stop):
    for i in range(stop):
        yield i
    return 10

print(list(range_2(6)))

