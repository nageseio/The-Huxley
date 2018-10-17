def Primo(num):
  primo=0
  n = num
  i = 1
  j = 0
  n2 = (n/2)
  while (i <= n):
    if (n % i==0):
        i = i+1
        j = j+1
    if (i>=n2):
        i = n
        i = i+1
        j = j+1
    else:
        i = i+1
  if(j==2):
    primo+=1
  if n < 2 or n == 4:
    return 0
  if primo == 1:
    return 1
  else:
    return 0

def Primo2(num1,num2):
  if Primo(num1) == 0 and Primo(num2) == 1:
    print("O numero",num1,"nao eh primo.")
  elif Primo(num1) == 1 and Primo(num2) == 0:
    print("O numero",num2,"nao eh primo.")
  elif Primo(num1) == 1 and Primo(num2) == 1:
    if Primo(num1+num2) == 1:
      print("A soma de",num1,"e",num2,"eh um primo.")
    else:
      print("A soma de",num1,"e",num2,"nao eh um primo.")

num1=int(input())
num2=int(input())

Primo2(num1,num2)
