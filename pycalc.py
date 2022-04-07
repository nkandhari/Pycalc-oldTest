# The script takes in expression in the form: `a + b` and returns sum of a and b.
# To run the script:
# In the terminal, enter python IDE:
# $ python3
# $ from pycalc import compute  --> from the pycalc.py script, import compute function
def compute(expression):# function name: compute
    num0, operator, num1 = expression.split(' ')
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1

    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1

    else:
        print('unknown operator!')
        return None
