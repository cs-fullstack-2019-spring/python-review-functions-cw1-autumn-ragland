# FUNCTION REVIEW
def main():
    # prob1()
    prob2()

def prob1():
    # counter set to 0 outside of loop
    counter = 0
    # user input defined outside of loop
    userInput =""
    # while loop to iterate as long as condition is true
    while userInput != "q":
        # prompt user for number
        userInput = input("Enter another number: ").lower()

        # if user does not enter q add to counter
        if userInput != "q":
            counter = counter + int(userInput)
        # if the user does not equal a number break
        # try:
        #     val = int(userInput)
        # except ValueError:
        #     print("That's not an int!")
    # print the running total
    print(counter)

# Create a function problem2()
# In this function prompt the user for 2 numbers
# Create a second function called do_the_math that accepts 2 parameters (the 2 entered numbers)
# In the do_the_math calculate the SUM, DIFFERENCE, PRODUCT, and QUOTIENT (division result) and
# return them as a dictionary to the calling function
# In your problem2() function, print the dictionary result returned
# from your do_the_math function using string literal formatting
def prob2():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    math(num1,num2)
def math(n1,n2):
    mathObj = {}
    mathObj["sum"] = (n1+n2)
    mathObj["diffrence"] = (n1-n2)
    mathObj["product"] = (n1*n2)
    mathObj["quotient"] = (n1//n2)
    print(f'Results:')
    for key, value in mathObj.items():
        print(f'The {key} of {n1} and {n2} is {value}')






if __name__ == '__main__':
    main()