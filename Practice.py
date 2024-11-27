def function (n):
  if (n==1) or (n==0):
    return 1
  elif n<0:
    return "NOT POSSIBLE"
  else:
    fact=1
    for i in range(1,n+1):
      fact*=i
    return fact
num=int(input("Enter a number:"))
print(f"THE FACTORIAL OF {num} IS",fact)
              
  
