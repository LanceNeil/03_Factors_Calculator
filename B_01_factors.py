# Generates heading (e.g., ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instruction", "'")
    print("This program will find the factors of a given number between 1 and 200 inclusive.")


# Ask user for an integer between 1 and 200
def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:
        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            response = int(response)
            if 1 <= response <= 200:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Function to find factors
def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


# Main Routine Goes here
statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instruction = input("\nPress <enter> to read the instructions "
                         "or any key to continue: ")

if want_instruction == "":
    instructions()

while True:
    comment = ""

    # Ask the user for number to be factorised
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break

    # Get factors for integer that are 2 or more
    elif to_factor != 1:
        all_factors = find_factors(to_factor)

    # Set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # Comments for squares/primes

    # Prime numbers have only two factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number."

    # check if the list has an odd number of factors
    elif len(all_factors) % 2 ==1:
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    # Output factors and comment
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator.")
