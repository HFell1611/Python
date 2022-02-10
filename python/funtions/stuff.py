def greet(*names, **greetings):
    return '\n'.join([f'{greetings.get(name, "Hello")}, {name}!' for name in names])

print(greet('Alice', 'Bob','Clarie', 'Derek', 'Eve', Alice='Hola', Bob='Bonjour', Derek='Hi', Eve='Howdy'))