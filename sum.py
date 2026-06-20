# Normal Sum Program 
num=int(input("Enter a Positive Integer Number:"))
s=0
if num>0:
    i=1
    while i<=num:
        s=s+i
        i=i+1
    print(f"The Sum Of All Numbers: {s} ")
else:
    print("Enter a Integer Number: ")

#if user entered non positive integer again it will user to enter positive integer number    

num=0
while num<=0:
    num=int(input("Enter a Positive Integer: "))
    if num <=0:
        print("You Entered Non Positive Integer!!") 
s=0
i=1
while i<=num:
    s=s+i
    i=i+1
print("Tota Sum Of Positive Integers: ",s)    


       



