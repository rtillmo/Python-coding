x=raw_input("Type a number:")
y=raw_input("Type a number:")
z=raw_input("Type a number:")

if x>y:
  if (x>z): 
    print x
  else:
    print z
    break
else:
  if (y>z):
    print y
else:
    print z
