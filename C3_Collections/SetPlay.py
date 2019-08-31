# Set like dictionary with its values thrown away, leaving only the keys.
emptySet = set()
even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7}

# {} will create an empty dictionary, use set() to create empty set
# because dictionaries were first in Python

# Create set from list
even_numbers = set([0, 2, 4, 6, 8])

# Create set from tuple
odd_numbers = set((1, 3, 5, 7))

# set will only retain key of dictionary
even_numbers_dict = {
    0: 'zero',
    1: 'one',
    2: 'two'
}

ordinalSet = set(even_numbers_dict)
print(ordinalSet)

drinks = {
    'martini': {'vodka','vermouth'},
    'black_russian': {'vodka', 'kahlua'},
    'white_russian': {'cream', 'kahlua', 'vodka'},
    'screwdiver': {'orange juice', 'apple juice'}
}

# Check which drink contain vodka
for name, content in drinks.items():
    if ('vodka' in content):
        print(name)

# Let's try with more complicated condition
for name, content in drinks.items():
    if ('vodka' in content) and not ('kahlua' in content):
        print(name)
