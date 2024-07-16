#N1

for i in range (0, 20, 1):
    print (i)

#N2

num = int(input("enter a number"))

if num % 2 == 0:
        print("The number is even")
else:
        print("The number is not even")

#N3

sum = 0

for num in range(50, 101):
    sum += num
    print(sum) 

#N4

for i in range(0, 51, 5):
  print(i)

#N5

num1 = int(input("enter a number"))
num2 = int(input("enter a number"))

ver = bool

if num1 > num2:
     ver == True
elif num1 < num2:
     ver == False

if ver == True:
     for i in range(num1, num2):
          print(i)
else:
     for i in range(num2, num1):
          print(i)

#N6

sum = 1

for i in range(5, 11):
     sum *= i
     print(sum)

