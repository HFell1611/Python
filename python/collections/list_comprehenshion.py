
fruits = ["apple", "pear", "banana", "plum", "cherry"]

# newlist = []
# for fruit in fruits:
#     newlist.append(fruit.capitalize())


newlist = [fruit.capitalize() if fruit == 'pear' else fruit for fruit in fruits]

print(newlist)    