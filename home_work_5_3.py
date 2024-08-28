
my_list = input('Ведіть рядок: ')

import string

for i in my_list:
    if i in string.punctuation:
        my_list = my_list.replace(i, '')

my_list = my_list.title()
my_list = my_list.replace(' ', '')
my_list = my_list.rjust(len(my_list) + 1,'#')

if len(my_list) >= 140:
    print(my_list[:140])
else:
    print(my_list)



