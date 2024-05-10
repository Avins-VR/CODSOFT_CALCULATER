def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if(b!=0):
        return a/b
    else:
        return "division will not be calculated"

print("1.Add")
print("2.Subtract")
print("3.multiply")
print("4.division")
while True:
    w=input("Enter the choice 1 or 2 or 3 or 4:")
    if w in ('1','2','3','4'):
        n1=float(input("Enter the number 1:"))
        n2=float(input("Enter the number 2:"))
        if(w=='1'):
            print(n1 ,"+" ,n2 ,"=" ,add(n1,n2))
        elif(w=='2'):
            print(n1 ,"-" ,n2 ,"=" ,subtract(n1,n2))
        elif(w=='3'):
            print(n1 ,"*" ,n2 ,"=" ,multiply(n1,n2))
        elif(w=='4'):
            print(n1 ,"/" ,n2 ,"=" ,division(n1,n2))
        break
    else:
            print("Invalid")
