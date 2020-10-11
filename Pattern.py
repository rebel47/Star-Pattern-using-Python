n = int(input("Enter the number: "))
b = int(input("Enter 0/1: "))
c = bool(b)
if c==True:
 for i in range(0, n):
  for j in range(0, i+1):
   print("*", end=" ")
  print("\r")
if c==False:
 for i in range(n):
  for j in range(n-i):
   print("*", end=" ")
  print("\r")
