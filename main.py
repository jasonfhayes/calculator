from compute_function import compute_two_numbers
from parse_function import get_two_numbers
from select_function import numerical_choice_selector

print("Welcome to Jason's calculator!\n"
      "\n"
      "Instructions:\n"
      "- Enter data when prompted.\n"
      "- Enter a \"Q\" at any time to Quit.\n")

while True:
    valid_inputs = ["y", "n", "q"]
    quit_program = None
    debug_mode = None
    debug_prompt = input("Run in \"Extra Verbose\" mode?\n"
                        "(This enables extra PASS/FAIL printouts.)\n\n"
                        "Y or N? ")
    if debug_prompt.lower() in valid_inputs:
        if debug_prompt.lower() == "y":
            quit_program = False
            debug_mode = True
            print("\n"
                  "\"Extra Verbose\" mode: ON"
                  "\n")
            break
        if debug_prompt.lower() == "n":
            quit_program = False
            debug_mode = False
            print("\n"
                  "\"Extra Verbose\" mode: ON"
                  "\n")
            break
        if debug_prompt.lower() == "q":
            quit_program = True
            print()
            break
    else:
        print("\n"
              "Please enter a \"Y\" or an \"N\"."
              "\n")


if quit_program == False:
    calculation_history = []
    while True:
        mode_selection = numerical_choice_selector(
            "Main Menu:",
            [
            "Use Calculator",
            "View Calculation History",
            "Clear History",
            "Quit"
            ],
            "Please enter a number from the list above to proceed: ",
            debug_mode)

        if mode_selection == 1:
        # Step 1: Get two numbers from the user:
            number_pair = get_two_numbers(2, debug_mode)
            if number_pair == -1:
                quit_program = True
                break

        # Step 2: Repeat back to the user what numbers they entered:
            print("You entered " + str(number_pair[0]) + " and " + str(number_pair[1]) + ".\n")

        # Step 3: Ask the user to choose an operation:
            operation_choice = numerical_choice_selector(
                "Operation Selection Menu:",
                [
                "Addition",
                "Subtraction",
                "Multiplication",
                "Division"
                ],
                "Please enter a number from the list above to select an operator: ",
                debug_mode)
            if operation_choice == -1:
                quit_program = True
                break

        # Step 4: Give the result to the user.
            print("Result:")
            new_calcualtion = compute_two_numbers(number_pair, operation_choice)
            calculation_history.append(new_calcualtion)

        if mode_selection == 2:
            print("History:")
            if calculation_history == []:
                print("The calulator history is currently empty.")
                print("Please perform a calculation first.")
            else:    
                for history_entry in calculation_history:
                    print(history_entry)
            print()

        if mode_selection == 3:
            clear_history = numerical_choice_selector(
                "Confirm clear history:",
                [
                "Yes",
                "No"
                ],
                "Are you sure? Please select a number from the choices above. \
                This cannot be undone: ",
                debug_mode)
            if clear_history == 1:
                calculation_history = []
                print("History cleared.")
                print()
            if clear_history == 2:
                print("History was not cleared.")
                print()
            if clear_history == -1:
                quit_program = True
                break

        if mode_selection == 4:
            quit_program = True
            break

        if mode_selection == -1:
            quit_program = True
            break

if quit_program == True:
    print("Thank you for using the calculator.\n\nGoodbye.")
