from utilities import Operations

perform_calculation = True

print("Welcome to the Simple Calculator!")


def perform_calculation():
    numbers = []
    options = ["a", "b", "c", "d"]

    def get_num(position):
        while True:
            number = input(
                f"Please enter the {position} number for your calculation: "
            ).strip()
            try:
                number = float(number)
                break
            except ValueError:
                print(
                    f"{position.title()} input is not a number, Input only valid numbers.\n"
                )
        return number

    positions = ["first", "second"]
    for position in positions:
        numbers.append(get_num(position))
    print("Great the two numbers gotten.\n")

    while True:
        print(
            "Operation Choices\na Addition(+)\nb Subtraction(-)\nc Multiplication(x)\nd division\n"
        )
        operation_choice = (
            input(
                "Enter the letter corresponding to your operation as seen above (eg: a): "
            )
            .strip()
            .lower()
        )
        if operation_choice in options:
            break
        else:
            print(
                "\nInvalid Choice. Please enter one of the letters (a, b, c, or d).\n"
            )

    result = Operations(numbers[0], numbers[1], operation_choice)
    print(result.calculate())


perform_calculation()
