# Files
# Avoid presets, import data from file, higher throughput
# Persisting sata, reading data back
# Analysis - import data from file to analyse
# recording data/logging

f = open('hello.txt', 'w')
lines = [f"Line{n}" for n in range (5)]
f.writelines([line + '\n' for line in lines])
f.write
f.close()