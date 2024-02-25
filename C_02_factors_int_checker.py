# Functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
To use this program simply enter an integer between 1 and 200.
The program will show the factors of your chose integer.

It will also tell you if your chosen number...
- is a prime number (ie: it has two factors) 
-is a perfect square

To exit the program, please type 'xxx'.
    ''')

# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")

# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True :

        response = input(question).lower()
        if response =="xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1 <= response <= 200:
               return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main routine Goes Here
while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break