# Queue Management
# Write a program to take an input, add it to the end
# of the queue and output the resulting 
# list for a queue management system.

q=[5, 10, 17, 3, 34]              # made up list of numbers

x = int(input())                       # get input from the user
q.append(x)                         # append the input to list 'q'
print(q)                        # print the newly created list