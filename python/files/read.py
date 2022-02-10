f = open('hello.txt', 'r')
# print(f.readline())
# f.readline()
# print(f.readline())
# f.close()

# lines = f.readlines()
# print(lines[2])
# f.close()

lines = [line.strip() for line in f.readlines()]
print(lines)
f.close()