def function (n):
  return 1 if (n==1 or n==0) else n*function (n-1)
num = int(input("enter a number:"))
print(f"the factorial of {num} is ", fact(num))
