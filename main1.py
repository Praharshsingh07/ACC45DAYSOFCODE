


def factorial(x):
    if x==1:
        return 1
    else:
        return x *factorial(x-1)


num= int(input("enter the number to be factorial"))
if num < 0:
  print("Invalid input ! Please enter a positive number.")
elif num == 0:
  print("Factorial of number 0 is 1")
else:
  print("Factorial of number", num, "=",factorial(num))