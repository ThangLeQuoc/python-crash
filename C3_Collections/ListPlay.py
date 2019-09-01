emptyList = list()
# emptyList.
print("Finish")
weekdays = ['Monday','Tuesday','Wednesday','Thursday']
# Get item by offset
x = weekdays[0]
print(x)

## Lists of Lists
small_birds = ['humming bird','finch']
extinct_birds = ['dodo']
carol_birds = [3, 'French Hen']
all_birds = [small_birds, extinct_birds, 12]
print(all_birds) # [['humming bird', 'finch'], ['dodo'], 12]

print(all_birds[0][1]) # finch

maxers = ['Gouncho','Chico','Harpo']
maxers_sliced = maxers[0:2] # slice 2 items from list from 0 : 'Gouncho','Chico'

maxers[::2] # go from start, step = 2

maxers_reversed = maxers[::-1]
print(maxers_reversed)

# append item to the end, using append()
maxers.append('Wrath')

# Combine list using extend()
others = ['Gummo','Karl']
extended_maxers = maxers.extend(others)
# extend is smilar to +=
extended_maxers = maxers + others
print(extended_maxers)

# insert element at offset, if the offset is greater that the list size, element is inserted at the end of the list
maxers.insert(2, 'Goege')
print(maxers)

# delete an item 
del maxers[2]
# delete using remove
maxers.remove('Wrath')

print('Maxers before pop') # ['Gouncho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(maxers)
secondMaxer = maxers.pop(1) # Chico
print(secondMaxer)
print(maxers) 

# Find offset of value
print(maxers.index('Karl'))

# Assert if value in list
print('Gummo' in maxers)

# Commbine value with join

harryPorterCharacters = ['Harry','Hermi','Ron']
delimiterChar = ','
joinedString =  delimiterChar.join(harryPorterCharacters)
print(joinedString)
comeback = joinedString.split(delimiterChar)
print(comeback)

sortedMaxers =  sorted(maxers) # create new copy, does not change order of maxer
print(sortedMaxers)
maxers.sort() # this will also change the order of maxer
print(maxers)

# try to sort list of item with different type => will throw exception
shuffleList = ['Guyz', 12, 0.13, 'Trash']

numbers = [9,12,34,12,41,211]
numbers.sort(reverse= True)
print(numbers)
# get list length
listLength = len(numbers)
print(listLength)

# Shalow copy
a = [0, 1, 2, 3]
b = a.copy() #
a[0] = 12
print(b) # 0,1,2,3 

## All copy technique
b = a.copy()
c = list(a)
d = a[:]

# Applying multiple condition
## 10 < x < 20
x = 15
if 10 < x < 20:
    print("Multiple condition works")
if 10 < x < 20 < 50:
    print("Multiple condition works")

some_list = []
if some_list:
    print("It has content inside")
else:
    print("It's empty")

vowels = 'aeiou'
letter = 'o'
if letter in vowels:
    print(letter, "is a vowel")

# Repeating with while
count = 1
while count < 5:
    print(count)
    count+=1

# continue and break, similar to Java
word = 'cat'
for letter in word:
    print(letter)

# check loop break with else
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else: # no break mean no cheese
    print('This is not much of a cheese shop, is it ?')

# this is useful to check when the loop has run successfully
# Iterate multiple sequences with zip()
# Trick to iterate through multiple sequence, stop when the shortest one end
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['Banana', 'Orange', 'Peach']
drinks = ['Coffee', 'Tea', 'Beer']
desserts = ['Tiramisu', 'Ice Cream', 'Pie', 'Pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercidi'
eng_french = list(zip(english, french))
e2f_dict = dict(eng_french)
print(eng_french)
print(e2f_dict)

# Generate number sequences with range()
# range (start, stop, step)
for x in range (0,3):
    print(x)
list(range(0,3))

# list comprehension
# [expression for item in iterable if condition]
number_list = [number for number in range(1,6)]
print(number_list)

a_list = [number for number in range(1,6) if number % 2 ==1]
print(a_list)

rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
print(cells)



