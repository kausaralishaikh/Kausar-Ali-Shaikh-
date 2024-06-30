a = int(input("choice"))
if(a==1):
   bug= int(input("budget"))
   if(bug>10000 and bug<20000):
      print("realme")
   elif(bug>20000 and bug<50000):
        print("samsung")
       
   elif(a==2):
        bug=int(input("enter budget"))
if budget>=100000:
    print("asus:1 lenovo:2 other:3")
    choice=int(input("enter choice"))
    if choice == 1:
       print("bought asus")
    elif choice == 2:
        print("bought lenovo")
    else:
        print("go away >:(")
elif budget>5000 and budget<100000:
    print("lenovo:1 other:2")
    choice=int(input("enter choice"))
    if choice == 1:
        print("bought lenovo")
    else:
        print("go away")
else:
    print("i can draw a laptop or")
