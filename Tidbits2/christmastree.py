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
  

tree()


