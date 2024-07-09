c = int(input('''enter ur choice 
               1 for add
                2 for sub 
                3 for multi
                4 for div : \n'''))
n1 = int(input('enter first number : '))
n2 = int(input('enter second number : '))

def add (n1,n2):
    print(n1+n2)
def sub (n1,n2):
    print (n1-n2)
def multiply (n1,n2):  
    print (n1*n2)
def divide (n1,n2):  
   print (n1/n2)



if c == 1:
  add(n1,n2)
elif c == 2:
  sub(n1,n2)
elif c == 3:
  multi(n1,n2)
elif c ==4:
  div(n1,n2)
else :
  print('invalid input')
