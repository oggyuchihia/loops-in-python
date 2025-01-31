num=87
for i in range(1,11):
    mul=num*i
    print(f"87x{i}={mul}")


#nested loop
n=int(input("please enter the number of rows"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*" , end=" ")
    print("\n")

#WHILE LOOP
num=1
sum=0
while (num<=10) :
    sum=sum+num
    num=num+1

print("the sum of first 10 natural no. is",sum)

#prime number  check
num=int(input("please enter a number to be checked"))
flag=False
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            flag=True
            break

if flag:
    print("no. is not prime")  
else:
    print("no. is prime")      







