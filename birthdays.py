birthdays = {'Alice': 'Apr 1', 'Freddie': 'Feb 24', 'Frankie': 'Feb 24'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name])
    else:
        print("I do not have a birthday for {}.".format(name))
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

