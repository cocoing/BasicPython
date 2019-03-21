# who's birthday is coming, enter his/her name, I will tell you.
# learn: while loop; break; format.

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}
while True:
    name = input("Enter a name(enter straight to quit):")
    if name == '':
        break
    if name in birthdays:
        print("{} is the birthday of {}".format(birthdays[name], name))
    else:
        print("I do not have birthday information for {}".format(name))
        bday = input("What's their birthday ?")
        birthdays[name] = bday
        print("Birthday database updated".center(50,'*'))
        print(birthdays)

