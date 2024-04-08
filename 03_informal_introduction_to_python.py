cubes = [1, 8, 27, 65, 125]
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes


rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # they reference the same object

rgba.append("Alph")
rgb


correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
correct_rgba

rgba


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# replace some values
letters[2:5] = ['C', 'D', 'E']
letters

# now remove them
letters[2:5] = []
letters

# clear the list by replacing all the elements with an empty list
letters[:] = []
letters

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

