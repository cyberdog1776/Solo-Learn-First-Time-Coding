'''List Operations
Given a list of numbers, output "bingo" if it contains the input number.'''
items = [42, 88, 721, 12, 43, 22, 908]

num = int(input())
#your code goes here
#if num == int in items: ORIGINAL BAD CODE WRITTEN
if num in items:
    print('bingo')
