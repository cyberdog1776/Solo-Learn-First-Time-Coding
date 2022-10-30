

passenger = 0  #starting number of passengers
ticket_total = 0  #beginning total of all tickets for 5 passengers
while passenger < 5:  #while the number of passengers input is less than or = 5
    age = int(input())
    passenger += 1  #passenger = passenger + 1 to increment up passenger number
    if age < 3:  #if the age integer is less than 3, loop back to while and skip 9 thru 12
        continue
    ticket_total += 100 # if age input is greater than 3, then ticket_total = t_t + 100
print(ticket_total) #when while loop increment to 5, print the total of tickets added