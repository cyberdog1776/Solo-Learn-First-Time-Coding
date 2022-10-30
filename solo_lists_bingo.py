#Given a list of numbers, output "bingo" if it contains the input number.
# write your code below
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

num = int(input())
if num is x[0:]:
    print("bingo")
else:
    print("no dice")