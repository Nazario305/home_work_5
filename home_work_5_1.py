my_string = input('Ведіть рядок: ')

import string
import keyword

is_valid = True

if my_string[0].isdigit():
    is_valid = False

for i in my_string:
    if i.isupper():
        is_valid = False
        break

for i in my_string:
    if i in string.punctuation:
        if i == '_':
            if my_string.count('_') > 1:
                is_valid = False
                break
        else:
            is_valid = False
    if i == ' ':
        is_valid = False
        break

kwlist = keyword.kwlist
if my_string in kwlist:
    is_valid = False

print(is_valid)
