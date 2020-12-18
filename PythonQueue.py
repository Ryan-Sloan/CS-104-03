names = []
for i in range(10):
    acceptedName = input('Enter name ')
    names.append(acceptedName)

for i in range(len(names)):
    print(names.pop(0))
