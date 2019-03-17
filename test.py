# this is a test python file, you can modify the content to test some code
#!/usr/bin/python3
"""
# format practise
age = 38
name = "little ming"
print("{0:*<20s} is {1:=>6d} years old now".format(name, age))
"""

# who's birthday is coming
birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}

while True:
    print("Enter a name(blank to quit):")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print("{} is the birthday of {}".format(birthdays[name], name))
    else:
        print("I do not have birthday information for {}".format(name))
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated".center(50,'*'))
    