#как насчёт использования pydantic?
class Command:
    def __init__(self, first_number, second_number, operand):
        self.first_number = first_number
        self.second_number = second_number
        self.operand = operand

    def get_params(self):
        return self.first_number, self.operand, self.second_number


def get_command_params(line: str) -> Command:
    params = line.split()
    if len(params) != 3:
        raise ValueError(f"Count of parameters is 3, but given {len(params)}")
    first_number = float(params[0])
    operand = params[1]
    second_number = float(params[-1])
    return Command(first_number, second_number, operand)


def minus(a, b):
    return a - b


def plus(a, b):
    return a + b


def power(a, b):
    return a ** b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(command: Command) -> str:
    if command.operand == '+':
        return plus(command.first_number, command.second_number)
    if command.operand == '-':
        return minus(command.first_number, command.second_number)
    if command.operand == '*':
        return multiply(command.first_number, command.second_number)
    if command.operand == '/':
        return divide(command.first_number, command.second_number)
    if command.operand == '**':
        return power(command.first_number, command.second_number)


def main():
    print("splitter is space or ' '")
    line = ''
    while line != 'exit':
        line = input('write your command: ')
        try:
            command = get_command_params(line)
            result = calculate(command)
            print("result:", result)
        except ValueError as e:
            print(e)


main()
