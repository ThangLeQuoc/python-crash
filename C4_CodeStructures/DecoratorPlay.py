def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b
add_ints(3, 5)

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

@document_it
def minus_ints(a, b):
    return a - b

minus_ints(10, 2)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints_v2(a, b):
    return a + b

add_ints_v2(3, 5)

similar_add_ints_v2_decorated = document_it(square_it(add_ints_v2))
similar_add_ints_v2_decorated(3, 5)

# The decorator that’s used closest to the function (just above the def) runs first and
# then the one above it. Either order gives the same end result, but you can see how the
# intermediate steps change:

