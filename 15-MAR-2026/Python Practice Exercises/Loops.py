
# 13. Write a program to print numbers from 1 to 50 using a loop.
for i in range(1,51):
    print(i)


# 14. Write a program to print the multiplication table of a number.
num=int(input("Enter a number: "))
for i in range(1,11):
    print(num,"x",i,"=",i*num)


# 15. Write a program to calculate the sum of numbers from 1 to 100.
sum=0
for i in range(1,100):
    sum=(i*(i+1)//2)
print("sum:",sum)


# 16. Write a program to print the factorial of a number.
num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial:",fact)