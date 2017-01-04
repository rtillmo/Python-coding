def sqrt():
  n=int(raw_input("Type a number:"))  
  guess= n/2
  while True:
    if guess*guess < n: 
      guess+= 0.001
    else:
      guess-= 0.001
    if abs(guess*guess-n) <= 0.001:
      break
    count=4
    count=count+1
  print "the square root of n is", guess
  


sqrt()
