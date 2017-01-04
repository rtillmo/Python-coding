

def tree():
  n = raw_input("Type the rows:")
  n = int(n)
  i=1
  stars = 1
  while i<=n:
    print ' ' * (n - i) + '*' * stars
    i=i+1
    stars += 2
  #for i in range(n): print ('*'*(2*i+1)).center(2*n)
  print '  ' * (n/2-1) + ' **'
  print '  ' * (n/2-1) + ' **'


def binary():
  s=""
  n=(raw_input("Type a number:"))
  n=int(n)
  while n>0:
    r=n%2
    s=str(r)+s
    n=n/2
  print "the binary equivalent is", s
	 

def divisor():
  n=int(raw_input("Type a number:"))
  print "The divisors are:",
  for i in range (1,50):
     if n%i == 0:
       print i,
  print


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
  print "the square root of n is", guess


def asciiInitials():
  print '''
  _____________________
  \______   \__    ___/
   |       _/ |    |   
   |    |   \ |    |   
   |____|_  / |____|   
          \/           
                        '''


def menu():
  print "0 -- quit"
  print "1 -- Christmas Tree"
  print "2 -- Binary"
  print "3 -- Divisors"
  print "4 -- Square Root"
  print "5 -- Ascii Art"
 

choice = raw_input("Type your choice: ")
choice = int(choice)
while choice != 0:
  if choice == 0:
    break
  elif choice == 1:
    tree()
  elif choice == 2:
    binary()
  elif choice == 3:
    divisor()
  elif choice == 4:
    sqrt()
  elif choice == 5:
    asciiInitials()
  else:
    print "Not yet"
  choice = raw_input("Type your choice: ")
  choice = int(choice)
