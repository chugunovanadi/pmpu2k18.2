def calc(a, operation, b):
    try:
        if operation == '/':
            return a / b
        elif operation == '*':
            return a * b
        elif operation == '-':
            return a - b
        elif operation == '+':
            return a + b
        else:
            raise NameError('Неизвестная операция')
    except NameError as e:
        print(e)


a, b = [int(item) for item in input().split()]
#temp = input()
#temp2 = temp.split()
#a = int(temp2[0])
#b = int(temp2[1])
#op = temp[2]
op = input()
print(calc(a, op, b))
