# generate headings (eg: -----Heading-----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator(statement="instructions", decoration="-")

    print('''
Instructions go here.
- instruction 1
- instruction 2  
- etc
    ''')


# asks users for file type (integer / image / test/ xxx)
def get_filetype():
    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for an image...
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

            # check for an text...
        elif response in ["text", 'txt', 't']:
            return "text"

        # if response is invalid output an error
        else:
            print("please neter a valid file type")


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


# calculates how many bits are needed to represent an integer
def image_calc():
    # Get image dimensions
    width = int_check(question="width: ", low=1)
    height = int_check(question="Height: ", low=1)

    # calculate the number of pixels and multiplying by 24 to get to the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up an answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# calculates how many bits are needed to represent an integer
def integer_calc():
    # Ask the user to enter integer (more than / equal to 0)
    integer = int_check(question="integer: ", low=0)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # set up an answer and return it
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it"

    return answer


# Calculate number of bits needed to represent test in ascii
def calc_text_bits():
    # Get text from user
    response = input("Enter some text: ")

    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\nWe need {num_chars} x bit to represent it "
              f"\nwhich is {num_bits} bits")

    return answer



# Main routine goes here

# Display instructions if requested
want_instructions = input("press <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()


while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break


    # if user chose 'i' ask if they want image / integer
    if file_type == 'i':

        want_image = input("press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer" :
        image_ans = integer_calc()
        print(image_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)