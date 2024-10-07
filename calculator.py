#sum
def sum(a,b):
    return a+b
#subtract
def subtract(a,b):
    return a-b
#multiplication
def multiply(a,b):
    return a*b
#division
def divide(a,b):
    if b==0 :
        return"Error : can't divide with zero"
    else:
       return a/b
#input
first = float(input("Enter first number="))
second = float(input("Enter second number="))
opr= str(input("Enter operation( +, -, *, / )="))

if opr=="+":
    total = first+second
elif opr=="-":
      total = first+second
elif opr=="*":
      total = first*second
elif opr=="/":
      total = first/second
else:
     str("Please Enter the valid Operation")
print(total)