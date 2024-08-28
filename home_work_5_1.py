my_list = input('Ведіть рядок: ')

import string
import keyword

is_valid = True

if my_list[0].isdigit() == True:
    is_valid = False

for i in my_list:
    if i.isupper() == True:
        is_valid = False
        break

for i in my_list:
    if i in string.punctuation:
        if i == '_':
            if my_list.count('_') > 1:
                is_valid = False
                break
        else:
            is_valid = False
    if i == ' ':
        is_valid = False
        break

kwlist = keyword.kwlist
if my_list in kwlist:
    is_valid = False

print(is_valid)
