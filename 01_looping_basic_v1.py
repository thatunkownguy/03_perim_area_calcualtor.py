

# cheak  input is a number more than zero
from turtle import width


def num_check(question):


    valid = False
    while not valid:

        error = "please enter a number that is more than zero"

        try:

                response = float(input(question))

                if response > 0:
                    return response
                else:
                    print("please enter a number that is more than zero")
                    print()
        except ValueError:
            print(error)






#main routine goes here
width = num_check("width: ")
height = num_check("height: ")
print()
print("width", width)
print("height", height)
print()