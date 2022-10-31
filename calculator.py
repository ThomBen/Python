num1 = input('Gimme a number : ')
operator = input('Gimme an operator (*, +, -, /)')
num2 = input('Gimme another number : ')

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '/': lambda x, y: x / y,
      '*': lambda x, y: x * y}

print(op[operator](int(num1), int(num2)))
