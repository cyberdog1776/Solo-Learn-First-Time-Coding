age = int(input())
if (age >= 0 and age <= 11):
    print('Child')
elif (age >= 12 and age <=17):
    print('Teen')
else:
    (age >= 18 and age <= 64) #not sure this line of code is being executed
    print('Adult') #this line is being executed, used debug tool
