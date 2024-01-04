#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == '+':
        print("{} + {} = {}".format(a, b, a + b))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, a - b))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, a * b))
    elif operator == '/':
        if b == 0:
            print("Error: Cannot divide by 0")
            sys.exit(1)
        print("{} / {} = {}".format(a, b, a / b))
    else:
        print("Unknown operator: {}".format(operator))
        sys.exit(1)
    sys.exit(0)
