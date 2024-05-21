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
    answer = (f"number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# MAin routine goes here
image_ans = image_calc()
print (image_ans)