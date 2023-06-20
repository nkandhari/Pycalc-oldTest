# The script takes in expression in the form: `a + b` and returns sum of a and b.
# To run the script:
# In the terminal, enter python IDE:
# $ python3
# $ from pycalc import compute  --> from the pycalc.py script, import compute function
# example:
# $ compute('2 + 2')
def compute(expression):
    values = expression.split(' ')
    num0 = int(values[0])
    operator = values[1]
    num1 = int(values[2])
    if operator == '+':
        return num0 + num1
    else:
        print('unknown operator!')
        return 0
