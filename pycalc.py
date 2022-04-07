# create function to add two numbers:
def compute(expression):
    values = expression.split(' ')
    num0 = int(values[0])
    operator = values[1]
    num1 = int(value[2])
    if operator == '+':
        return num0 + num1
    else:
        print('unknown operator!')
        return 0
