from calc import *
while(1):
    x=input("Enter the command ")
    n1=int(input("Enter first number "))
    n2=int(input("Enter second number "))
    if x=="add":
        print ("Sum is" +" "+ str(add(n1,n2)))
    elif x=="sub":
        print ("Subtraction is" +" "+ str(sub(n1,n2)))
    elif x=="mul":
        print ("Multiplication is" +" "+ str(mul(n1,n2)))
    elif x=="div":
        print ("Division is" +" "+ str(div(n1,n2)))



    again=input("Do you want to try again?")
    if again=="yes":
        continue
    if again=="stop":
        break
    
        
        



