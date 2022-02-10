names = []
while len(names) < 5:
    names.append(input("Enter a name: "))

for name in names:
    print(name.capitalize() + ' is awesome!')