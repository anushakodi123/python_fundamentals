import math
import json
#formating string literals

print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'S': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:2} ==> {phone:10d}')

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

#str.format()

yes_votes = 42_5
no_votes = 43
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

#str() and repr()
s = 'Hello, world.'
print(str(s))
print(repr(s))
a =1/2
print(str(a))
print(repr(a))

#!s,!r,!a

animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')

#=specifier
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

#str.format() with position
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
# f = open('sample_text_file', 'w', encoding="utf-8")
# print(f)

# with open('sample_text_file', encoding="utf-8") as f:
#     read_data = f.read()
#     print(read_data)
#     # print(f.readline())

# f = open('sample_text_file', 'r+', encoding="utf-8")
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line, end='')

# f.write('This is a test\n')
# print(f.read())

# value = ('the answer', 42)
# s = str(value)  # convert the tuple to string
# f.write(s)
# print(f.read())




# Using r+ mode to read and write text data
with open("new_file.txt", "r+") as file:
    # Read the content of the file
    content = file.read()
    print("Content of the file:", content)

    # Move the file cursor to the beginning
    file.seek(0)

    # Write new content to the file
    file.write("New line added using r+ mode.")

    # Move the file cursor to the beginning again
    file.seek(0)

    # Read the updated content of the file
    updated_content = file.read()
    print("Updated content of the file:", updated_content)

    # print(file.seek(-3, 2))
    print(file.read())


# Using rb+ mode to read and write binary data
with open("binary_file.bin", "rb+") as file:
    # Read the content of the file
    content = file.read()
    print("Content of the file:", content)

    # Move the file cursor to the beginning
    file.seek(0)

    # Write new content to the file
    file.write(b"New line added using rb+ mode.")

    # Move the file cursor to the beginning again
    file.seek(0)

    # Read the updated content of the file
    updated_content = file.read()
    print("Updated content of the file:", updated_content)

    print(file.seek(-3, 2))
    print(file.read())

f = open('sample_text_file', 'rb+')
print(f.read())
# x = [1, 'simple', 'list']
# # json.dumps(x)

# json.dump(x, f)


# Open the file in rb+ mode
with open('sample_text_file', 'rb+') as f:
    # Read the content of the file
    content = f.read()
    print("Content of the file before writing JSON:", content)

    # Rewind the file pointer to the beginning
    f.seek(0)

    # Create some sample data
    x = [1, 'simple', 'list']

    # Convert the data to JSON
    json_data = json.dumps(x)

    # Write the JSON data to the file
    f.write(json_data.encode('utf-8'))

    # Rewind the file pointer to the beginning again
    f.seek(0)

    # Read the updated content of the file
    updated_content = f.read()
    print("Updated content of the file after writing JSON:", updated_content.decode('utf-8'))

# At this point, the file will be automatically closed due to the usage of 'with' statement
