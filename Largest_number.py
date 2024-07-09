a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
def maximum(a,b):
    if a>b:
        print(a,"is biggest")
    else:
        print(b,"is biggest")
    
maximum(c,max(b,a))  
