# Practice with Tuple
# Tuple are immutable
immutableTuple = ('George','Linda','Ross')

# Assign tuple value to multiple variable
# Technique name: tuple unpacking
# => throw not enough values to unpack exception if the variables number is greater than
# tuple size
george, linda, ross = immutableTuple
print(george)

newTuple = george, linda, ross
print(newTuple)

# use tuple to exchange value without the need of temporary variable
a = 'a'
b = 'b'
b, a = a, b
print(b)

# Convert from List to Tuple
headphones = ['Skullcandy Ink\'d', 'Audio Technica ATH M50x', 'Noble Savant', 'Audeze LCD XC']
headphonesTuple = tuple(headphones)
print(headphones)
print(headphonesTuple)


