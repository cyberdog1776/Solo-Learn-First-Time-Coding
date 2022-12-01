# def hello():       #define the function
#     print('Hi!')    # action of the function

# hello()             # calling the function
# print(hello)       # print the function  
###### ALTERNATE METHOD ##########
def hello():       #define the function
    print('Hi!')    # action of the function
    return hello()   # calling for a return of the function
            
print(hello)       # print the function  