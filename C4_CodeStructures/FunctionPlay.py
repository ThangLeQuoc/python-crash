# do nothing function
def do_nothing():
    pass


# When you call a function with arguments, the values of those arguments are copied to their
# corresponding parameters inside the function. 

# None is useful
thing = None
if thing is None:
    print("It's nothing")


def positional_word(drink, meat):
    print("Meat is", meat)
    print("Drink is", drink)


positional_word(meat="beef", drink="coke")


# Specify default parament value
def positional_key(meat, drink='coke'):
    print(drink)


def print_kwargs(**kwargs):
    print('Keyword args', kwargs)


# docstrings
def echo(anything):
    'echo returns its input'
    return anything


def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
    1. Check whether the *second* argument is true.
    2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)


help(print_if_true)  # this will print the help


# anonymous functions
def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):  # give that prose more punch
    return word.capitalize() + '!'


edit_story(stairs, enliven)


def amazing():
    """
    This is the amazing function, want to see it again ?
    """
    print("This function is named:", amazing.__name__)
    print('And its docstring is:', amazing.__doc__)


amazing()
