#Pattern Printing
 #
 # Input = integer n
 # boolean = True or false
 # True n=5
 # *
 # **
 # ***
 # ****
 #
 # False n=5
 # ****
 # ***
 # **
 # *
 #

#
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


'''PasCal Triangle'''
# def func1(n):
#  for a in range(0, n+1):
#   for i in range(0, a + 1):
#    print(func2(a, i),
#          " ", end="")
#   print()
# def func2(n, k):
#  b = 1
#  if (k > n - k):
#   k = n - k
#  for i in range(0, k):
#   b = b * (n - i)
#   b = b // (i + 1)
#
#  return b
#
# n = int(input("Enter the number: "))
# func1(n)


