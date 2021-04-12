calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units}{name_of_unit}"
    elif num_of_days == 0:
        return 'you entered a 0, please return a positive number'


def validate_and_execute() -> object:
    try:
        user_input_number = int(num_of_days_element)

        # DJ wants the integer to be a positive number
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter a positive number")
        else:
            print("you entered a negative number, no conversion for you")
    except ValueError:
        print("your input is not a number, Don't Break D.J.'s Program!")


user_input = ""
while user_input != "exit":
    user_input = input("D.J. says, enter a comma separated number list and I will convert into a number hours!\n")
    num_of_days = user_input.split(" ")

    for num_of_days_element in set(num_of_days):
        validate_and_execute()
