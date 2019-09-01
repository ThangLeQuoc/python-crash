short_list = [1,2,3]
position:int = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list) - 1, 'but got', position)

# Keyword difference
# Java: catch | Python: except
# Java: throw | Python: raise


# Make your own exceptions
class UppercaseException(Exception):
    pass
words = ['eenie','meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
