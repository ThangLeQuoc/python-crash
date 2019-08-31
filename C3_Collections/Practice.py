# Various helper functions
def print_header(section: str):
    print('--------------------------')
    print('Start of section ' + section)


def print_footer(section: str):
    print('End of section ' + section)


# Things to do section

# 3.1. Create a list called years_list, starting with the year of your birth, and each year
# thereafter until the year of your fifth birthday. For example, if you were born in 1980.
# the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985]
section = '3.1'
print_header(section)
year_of_birth = 1980
years_list = list()
years_count = 6
for i in range(0, years_count):
    new_year = year_of_birth + i
    years_list.append(new_year)
print(years_list)  # [1980, 1981, 1982, 1983, 1984, 1985]
print_footer(section)
#####


# 3.2. In which year in years_list was your third birthday? Remember, you were 0
# years of age for your first year.
section = '3.2'
print_header(section)
age_wanted = 3
year_with_age_wanted = year_of_birth + age_wanted
that_year_with_age = years_list[years_list.index(year_with_age_wanted)]
print(that_year_with_age)
print_footer(section)
#####


# 3.3. In which year in years_list were you the oldest?
section = '3.3'
print_header(section)
years_list.sort()  # sort year incorrect order first
years_with_max_age = years_list[-1]
print(years_with_max_age)  # 1985
print_footer(section)
#####


# 3.4. Make a list called things with these three strings as elements: "mozzarella",
# "cinderella", "salmonella"
section = '3.4'
print_header(section)
things = ["mozzarella", "cinderella", "salmonella"]
print(things)
print_footer(section)
#####


# 3.5. Capitalize the element in things that refers to a person and then print the list.
# Did it change the element in the list?
section = '3.5'
print_header(section)
person_name = 'cinderella'
things[things.index(person_name)] = things[things.index(
    person_name)].capitalize()
print(things)
print_footer(section)

# post execution, restore things state
things = ["mozzarella", "cinderella", "salmonella"]
#####


# 3.6. Make the cheesy element of things all uppercase and then print the list.
section = '3.6'
print_header(section)
chessyElements = {'mozzarella'}
for i in range(len(things) - 1):
    if things[i] in chessyElements:
        things[i] = things[i].capitalize()
print(things)
print_footer(section)
#####


# 3.7. Delete the disease element from things, collect your Nobel Prize, and print the
# list
section = '3.7'
print_header(section)
disease_element = {'salmonella'}
for element in things:
    if (element in disease_element):
        things.remove(element)
print('Collecting my Nobel Prize')
print(things)
print_footer(section)
#####


# 3.8. Create a list called surprise with the elements "Groucho", "Chico", and "Harpo"
section = '3.8'
print_header(section)
surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)
print_footer(section)
#####


# 3.9. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
section = '3.9'
print_header(section)
last_element = surprise[-1].lower()
last_element_chars_list = list(last_element)  # ['h', 'a', 'r', 'p', 'o']
# .reverse() will print None, the order of the list is changed internally
last_element_chars_list.reverse()
last_element = ''.join(last_element_chars_list)
surprise[-1] = last_element.capitalize()
print('Now, surprise !')
print(surprise)
print_footer(section)
#####


# 3.10. Make an English-to-French dictionary called e2f and print it. Here are your
# starter words: dog is chien, cat is chat, and walrus is morse.
section = '3.10'
print_header(section)
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
print(e2f)
print_footer(section)
#####


# 3.11. Using your three-word dictionary e2f, print the French word for walrus.
section = '3.11'
print_header(section)
word_to_find = 'walrus'
word_in_french = e2f.get(word_to_find, 'Not Found')
print(word_to_find + ' in French is ' + word_in_french)
print_footer(section)
#####


# 3.12. Make a French-to-English dictionary called f2e from e2f. Use the items
# method.
section = '3.12'
print_header(section)
f2e = {}
for w_eng, w_french in e2f.items():
    f2e[w_french] = w_eng
print('My French-to-English dictionary')
print(f2e)
print_footer(section)
#####


# 3.13. Using f2e, print the English equivalent of the French word chien.
section = '3.13'
print_header(section)
word_to_find = 'chien'
word_in_eng = f2e.get(word_to_find, 'Not Found')
print(word_to_find + ' in English is ' + word_in_eng)
print_footer(section)
#####


# 3.14. Make and print a set of English words from the keys in e2f
section = '3.14'
print_header(section)
list_eng_words = list(f2e.values())
print(list_eng_words)
print_footer(section)
#####


# 3.15. Make a multilevel dictionary called life. Use these strings for the topmost keys:
# 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictio‐
# nary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list
# of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys
# refer to empty dictionaries
section = '3.15'
print_header(section)
animals_dict = {
    'cats': ['Henri', 'Grumpy', 'Lucy'],
    'octopi': [],
    'emus': []
}
plants_dict = dict()
other_dict = dict()

life = {
    'animals': animals_dict,
    'plants': plants_dict,
    'other': other_dict
}
print(life)
print_footer(section)
#####


# 3.16. Print the top-level keys of life.
section = '3.16'
print_header(section)
print('Top Level key')
for key in life.keys():
    print(key)
    break
print_footer(section)
#####

# 3.17. Print the keys for life['animals'].
section = '3.17'
print_header(section)
animals_dict = life.get('animals')
print(list(animals_dict.keys()))
print_footer(section)
#####

# 3.18. Print the values for life['animals']['cats']
section = '3.18'
print_header(section)
print('Cat values')
print(life['animals']['cats'])
print_footer(section)
#####
