#data_classes------------
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
print(john.dept)

print(john.salary)


@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0  # Default value

# Creating instances of the Point class
p1 = Point(1.5, 2.5)
p2 = Point(3.0, 4.0)

# Accessing attributes
print(p1.x, p1.y, p1.z)  # Output: 1.5 2.5 0.0
print(p2.x, p2.y, p2.z)  # Output: 3.0 4.0 0.0

# Automatically generated methods
print(repr(p1))  # Output: Point(x=1.5, y=2.5, z=0.0)
print(p1 == p2)  # Output: False


#iterators-----------

# Define a list
my_list = [1, 2, 3, 4, 5]

# Get an iterator object from the list
my_iterator = iter(my_list)

# Iterate through the iterator
while True:
    try:
        # Get the next item
        item = next(my_iterator)
        print(item)
    except StopIteration:
        # If StopIteration is raised, break the loop
        break

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
rev = Reverse('spam')
iter(rev)

for char in rev:
    print(char)



#Generators-----------

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)


def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create a generator object
counter = countdown(5)

# Iterate over the generator
for value in counter:
    print(value)

#Generator Expressions --------------
    
sum(i*i for i in range(10))                 # sum of squares


xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product


data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))

# Generator expression to generate a sequence of squares
square_generator = (x ** 2 for x in range(1, 6))

# Iterate over the generator
for square in square_generator:
    print(square)
