f = open('teams.txt', 'w')
f.write('West Brom\nLeicester\nChelsea\nTottenham\nCambridge United')

f = open('teams.txt', 'r')
lines = f.readlines()
print(lines[0])
print(lines[3])
f.close()