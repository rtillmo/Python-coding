def divisor():
  n=int(raw_input("Type a number:"))
  print "The divisors are:",
  for i in range (1,50):
     if n%i == 0:
       print i,
  print
  

divisor()
