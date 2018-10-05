def calc(a, operation, b):
        if operation == '/':
            return a / b
        elif operation == '*':
            return a * b
        elif operation == '-':
            return a - b
        elif operation == '+':
            return a + b
        else:
            print('Неизвестная операция')

a, b = [int(item) for item in input().split()]
op = input()
print(calc(a, op, b))