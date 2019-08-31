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