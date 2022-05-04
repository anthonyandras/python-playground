catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or nothing to stop)')
    name = input()
    if name.strip() == '':
        break
    catNames.append(name)

print('The cat names are:')
for name in catNames:
    print(name)
