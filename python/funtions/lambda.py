# def greet(name):
#     return f"Hello, {name}!"

def add(x):
    return lambda y: x + y

print(add(2)(3))