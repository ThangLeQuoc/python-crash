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