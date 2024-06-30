from contextlib import contextmanager  

 # Using a built-in context manager for file operations
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

# No need to explicitly close the file
    

class MyContextManager:
    def __enter__(self):
        # Setup code, executed when entering the context
        print('Entering the context')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Teardown code, executed when exiting the context
        print('Exiting the context')
        if exc_type:
            print(f'An exception occurred: {exc_value}')
        return True  # Suppress exceptions, if necessary

# Using the custom context manager
with MyContextManager() as manager:
    print('Inside the context')


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('samplee.txt', 'w') as f:
    f.write('Hi.. Hello World!')

print(f.closed)