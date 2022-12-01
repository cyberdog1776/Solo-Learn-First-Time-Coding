# Call The Function
# Arguments
# The given program defines a function printBill(), 
# which takes one string argument and 
# outputs formatted text.

# You need to take the user input and call the function
#  by passing the input as its argument.

#  You need to only call the function, as 
#  it will take care of the output.

def printBill(text):    # defines function
        print("======")     # what function will execute
        print(text)
        print("======")

text = input()          # get input from User
printBill(text)         # call function (which prints out return)