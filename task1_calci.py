# SIMPLE CALCULATOR for integers

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

oper={"+":add,"-":sub,"*":mul,"/":div}

def calci():
  num1=int(input("Enter first number:"))
  for i in oper:
      print(i)
  flag=True
  while flag:
    opsym=input("Enter operation symbol:")
    num2=int(input("Enter second number:"))
    calu=oper[opsym]
    output=calu(num1,num2)
    printf(f"{num1} {opsym} {num2} = {output}")
    cont=input(f"Enter 'y' to continue with {output} (or) 'n' to start (or) 'x' to exit:").lower()
    if cont=="y":
        num1=output
    elif cont=="n":
        flag=False
        os.system("cls")
        calci()
    elif cont=="x":
        cont=False
  print("BYE")

calci()
