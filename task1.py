def get_number(line: str):
    if line.isdigit():
        return f"Number has length: {len(line)}"
    return f"Warning: the '{line}' is not a number"


def main():
    exit_command = "exit"
    print("Welcome to task 1! Write your numbers:")
    line = input()
    while line != exit_command:
        print(get_number(line))
        line = input()
    print("Thank you for using task 1!")


main()
