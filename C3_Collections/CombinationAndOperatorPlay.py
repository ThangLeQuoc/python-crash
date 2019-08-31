# Let's reuse drinks dictionary
drinks = {
    'martini': {'vodka','vermouth'},
    'black_russian': {'vodka', 'kahlua'},
    'white_russian': {'cream', 'kahlua', 'vodka'},
    'screwdiver': {'orange juice', 'apple juice'}
}

# Check for combination of set value
# use Set intersection operator
for name, content in drinks.items():
    if content & {'vodka', 'kahlua'}: # find any drink that contain vodka OR kahlua
        print(name)

blackRussianKey = 'black_russian'
bruss = drinks.get(blackRussianKey)
bruss = {'kacua', 'toush'}
print(drinks.get(blackRussianKey))

# use of intersection
a = {1, 2}
b = {2, 3}

# Get intersection of a and b
print(a & b)
# or use intersection function
print(a.intersection(b))

# union
print(a | b)
# or use union
print(a.union(b))

# get difference
print (a - b)
# or use difference
print(a.difference(b))

# get exclusive item (in only one single set)
print(a ^ b)
# ... or use symmetric_difference
print(a.symmetric_difference(b))

# check if a set is a subset of other
print(a <= b)
# or use issubset function
print(a.issubset(b))

# oposite to subset is super set
print(a.issuperset(b))




