
days = raw_input("Type the days: ")
days = int(days)
count = 1
sum = 0
amount = 1

while count <= days:
  sum = sum + amount
  amount = amount * 2
  count += 1

print "The chieftain gets:", sum
  
  
