from utils import parse_input
from operations import add, subtract, multiply

def main():
    a, b = parse_input()
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")

if __name__ == "__main__":
    main()