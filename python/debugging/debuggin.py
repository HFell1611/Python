# Debugging
# Static analysis: Reading the code
# Dynamic analysis: Executing code
import pdb

pdb.set_trace()


def double(x):
    res = x * 2
    return res

print(double(2))
print(double(3))