
# 9. Write a program to check whether a number is even or odd.
num=int(input("Enter a number: "))
if num%2==0:
    print("even")
else:
    print("odd")


# 10. Write a program to check whether a number is positive or negative .
num=int(input("Enter a number: "))
if num>0:
    print("positive")
elif num==0:
    print("zero")
else:
    print("negative")


# 11. Write a program to check whether a person is eligible to vote (age ≥ 18) .
age=int(input("Enter a number: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 12. Write a program that takes marks as input and prints grade:
marks=int(input("Enter ur marks: "))
if marks>=90:
    print("A")
elif marks>=70:
    print("B")
elif marks>=50:
    print("C")
else:
    print("Fail")