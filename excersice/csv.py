# x, y, z = [2, 6, 78]

# print(y)


from shlex import join


# name = 'Ali Pakzad'
# c = name.split(' ')
# print(c)
# new_name = join(c)
# print(new_name)


# x = open('text.txt', 'w')
# x.write(name)
# x.close()

persons = [
    ['name', 'family'],
    ['ali', 'pakzad'],
    ['mmd', 'mmdi'],
    ['reza', 'resaee']
]

f = open('person.txt', 'w')
# f.write('name family')
# f.write('\n')
for person in persons:
    x = join(person)
    f.write(x)
    f.write('\n')

f.close()