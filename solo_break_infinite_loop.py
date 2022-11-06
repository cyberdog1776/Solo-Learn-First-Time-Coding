i = 0
while True:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking") #Breaks here once x >= 5, otherwise endless
    break

print("Finished")