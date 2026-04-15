#Arithmetics Operators

a=10
b=5

print("Addition: ", a+b)
print("Subtraction: ", a-b)
print("Multiplication: ", a*b)
print("Division: ", a/b)
print("Floor Division: ", a//b)
print("Modulo: ", a%b)
print("Exponentiation: ", a**b)

#Comparison Operators

x=5
y=10

print("Equal: ", x==y)
print("Not Equal: ", x!=y)
print("Greater: ", x>y)
print("Less: ", x<y)
print("Greater than or equal: ", x>=y)
print("Less than or equal: ", x<=y)

#Logical Operators

a=True
b=False

print(a and b)
print(a or b)
print(not a)
print(not a or b)

#Assignment Operator

x=10
print(x)

x+=10
print(x)

x-=10
print(x)

x*=10
print(x)

x/=10
print(x)

#Identity Operators

a=[1,2]
b=a
c=[1,2]

print(a is b)
print(a is c)
print(a is not c)

#Membership operators

x= [1,2,3,4]

print(2 in x)
print(3 in x)
print(5 in x)
print(5 not in x)

#Bitwise operator

a=5
b=3

print("Bitwise AND ", a&b)
print("Bitwise OR ", a|b)
print("Bitwise XOR ", a^b)
print("Bitwise NOT ", ~b)
print("Bitwise Right shift ", a>>b)
print("Bitwise Left shift ", a<<b)

#Walrus Operator
if (n := 5) > 3:  # assign and use in the same line
    print(n)

if name := "Zeru":
    print("Hello", name)



