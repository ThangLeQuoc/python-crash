# Various helper functions
def print_header(section: str):
    print('--------------------------')
    print('Start of section ' + section)


def print_footer(section: str):
    print('End of section ' + section)


# 4.1 Assign the value 7 to the variable guess_me. Then, write the conditional tests (if,
# else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if
# greater than 7, and 'just right' if equal to 7.
section = '4.1'
print_header(section)
guess_me = 7
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else:
    print("just right")
print_footer(section)


# 4.2 Assign the value 7 to the variable guess_me and the value 1 to the variable start.
# Write a while loop that compares start with guess_me. Print too low if start is less
# than guess me. If start equals guess_me, print 'found it!' and exit the loop. If
# start is greater than guess_me, print 'oops' and exit the loop. Increment start at
# the end of the loop
section = '4.2'
print_header(section)
guess_me = 7
start = 1

while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1
print_footer(section)


# 4.3 Use a for loop to print the values of the list [3, 2, 1, 0].
section = '4.3'
print_header(section)
numbers = [3, 2, 1, 0]
for num in numbers:
    print(num)
print_footer(section)


# 4.4 Use a list comprehension to make a list of the even numbers in range(10).
section = '4.4'
print_header(section)
even_numbers = [num for num in range(10) if num % 2 == 0]
print(even_numbers)
print_footer(section)


# 4.5 Use a dictionary comprehension to create the dictionary squares. Use range(10)
# to return the keys, and use the square of each key as its value.
section = '4.5'
print_header(section)
limit = 10
squares = {num: num * num for num in range(limit)}
print(squares)
print_footer(section)


# 4.6 Use a set comprehension to create the set odd from the odd numbers in
# range(10)
section = '4.6'
print_header(section)
limit = 10
odd = {num for num in range(limit) if num % 2 == 1}
print(odd)
print_footer(section)


# 4.7 Use a generator comprehension to return the string 'Got ' and a number for the
# numbers in range(10). Iterate through this by using a for loop.
section = '4.7'
print_header(section)
limit = 10
string_generator = ('Got ' + str(num) for num in range(limit))
for item in string_generator:
    print(item)
print_footer(section)


# 4.8 Define a function called good that returns the list ['Harry', 'Ron', 'Her
# mione']
section = '4.8'
print_header(section)


def good():
    return ['Harry', 'Ron', 'Hermione']


print(good())
print_footer(section)


# 4.9 Define a generator function called get_odds that returns the odd numbers from
# range(10). Use a for loop to find and print the third value returned.
section = '4.9'
print_header(section)
limit = 10
get_odds = (num for num in range(limit) if not num % 2 == 0)
count = 0
for num in get_odds:
    if count == 2:
        print(num)
        break
    count += 1
print_footer(section)


# def get_odds():
#     for number in range(1, 10, 2):
#         yield number

# count = 1
# for number in get_odds():
#     if count == 3:
#         print("The third odd number is", number)
#         break
#     count += 1


# 4.10 Define a decorator called test that prints 'start' when a function is called and
# 'end' when it finishes.
# section = '4.10'
# print_header(section)

def test(func):
    def nested_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return nested_function

@test
def add(a, b):
    print(a + b)

add(12,4)


# 4.11 Define an exception called OopsException. Raise this exception to see what hap‐
# pens. Then write the code to catch this exception and print 'Caught an oops'.
section = '4.11'
print_header(section)


class OopsException(Exception):
    pass


def with_exception(a):
    if a < 0:
        raise OopsException(a)


try:
    with_exception(-1)
except OopsException as err:
    print('Caught an oops')

print_footer(section)


# 4.12 Use zip() to make a dictionary called movies that pairs these lists: titles =
# ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a mon
# ster', 'A haunted yarn shop'].
section = '4.12'
print_header(section)

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movies = {}
for title, plot in zip(titles, plots):
    movies[title] = plot
# or movies = dict(zip(titles, plots))
print(movies)
print_footer(section)
