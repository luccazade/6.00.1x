def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      print(n)
      return 1
   else:
      print(n * f(n-1))
      return n * f(n-1)

print(f(3))