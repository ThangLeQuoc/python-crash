# Dictionary
# Similar to map in Java

# create empty dictionary
empty_dict = {}
a = 12
print(12)
bio_dict = {
    "apple": "to be fall",
    "banana": "thick, and sexy",
    "orange": "lovely juice"
}
print(bio_dict)
keys = bio_dict.keys();

# Add new key
bio_dict['grape'] = 'too many'
print(bio_dict)
# Replace value with same key
bio_dict['banana'] = 'long, sleek'
print(bio_dict)

# if two key is used, the last one will win
# Combine dictionary with update

extraFruits = {
    'mango': 'delicious',
    'mangosteen': 'not a mango'
}
bio_dict.update(extraFruits)
print(bio_dict)

# delete item by key with del
del bio_dict['mango']
print(bio_dict)

# Assert key in dictionary
print('apple' in bio_dict)

# Retrive item by key
bananaDescription = bio_dict['banana']
print(bananaDescription)

# Retrieve item using get function, with default value if no key found
bananaDescription = bio_dict.get('banana', 'no description')
print(bananaDescription)

# Get all key
dict_keys = bio_dict.keys();
print(dict_keys) # dict_keys(['apple', 'banana', 'orange', 'grape', 'mangosteen'])
convert_keys = list(dict_keys)
print(convert_keys)

# Get all values
myDict_values = bio_dict.values()
print(myDict_values)
myDict_values_converted = list(myDict_values)
print(myDict_values_converted)

# Get all key-value pair
dict_items =  bio_dict.items();
print(dict_items)





