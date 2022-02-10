f = open('teams.txt', 'r+')

line = (f.readlines)
for line in range(1):
    f.write('This is a new line')

print(f.read())
f.close()

with open('teams.txt', 'r') as teams:
    lines = teams.readlines()
    lines[0] = "This is a new line\n"

with open('teams.txt', 'w') as teams:
    teams.writelines(lines)

with open('teams.txt', 'r') as teams:
    for line in teams.readline():
        print(line)