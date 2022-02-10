def mark(name, fscore):
    return f"{name}, you got a {fscore}"

n = input("Enter your name: ")
h = int(input("Homework score (out of 25): "))
a = int(input("Assignment score( out of 50): "))
e = int(input("Exam score (out of 100): "))

# if h > 25:
#     print('Homework score too high')
# if a > 50:
#     print('Assignment score too high')
# if e > 100:
#     print('Exam score too high')

f = int((h / 25) * 25) + ((a / 50) * 25) + ((e / 100) * 50)

if f >= 70:
    f = 'A'
elif f < 70 and f >= 60:
    f = 'B'
elif f < 60 and f >= 50:
    f = 'C'
elif f < 50 and f >= 40:
    f = 'D'
elif f < 40 and f >= 30:
    f = 'E'
else:
    f = 'F'

print(mark(n, f))