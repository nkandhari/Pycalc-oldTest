# The script takes in expression in the form: `a + b` and returns sum of a and b.
# To run the script:
# In the terminal, enter python IDE:
# $ python3
# $ from pycalc import compute  --> from the pycalc.py script, import compute function
# example:
# $ compute('2 + 2')
# $ compute('12 / 6') test
#test2 test 3
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    num0, num1 = int(num0), int(num1)
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
