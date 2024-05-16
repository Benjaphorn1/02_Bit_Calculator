# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):
    error = "please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print("please enter a number that is more than zero")

        except ValueError:
            print(error)


# main routine goes here
for item in range(0, 2):
    integer = int_check(question= "integer: ",low=1)
    print(integer)

print()

for item in range(0, 2):
    Width = int_check(question= "width: ",low=1)
    print(Width)

print()

for item in range(0, 2):
    height = int_check(question= "Height: ",low=1)
    print(height)