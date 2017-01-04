def binary():
  s=""
  n=(raw_input("Type a number:"))
  n=int(n)
  while n>0:
    r=n%2
    s=str(r)+s
    n=n/2
  print "the binary equivalent is", s
	 


binary()
