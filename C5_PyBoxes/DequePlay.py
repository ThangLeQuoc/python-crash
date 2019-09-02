# stack + queue = deque
# useful when you want to add and delete items from either end of a sequence
from collections import deque

def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True


print(palindrome('thaht'))

# Checking with reverse
def shorter_palindrome(word):
    reverse_word = word[::-1]
    return reverse_word == word
    