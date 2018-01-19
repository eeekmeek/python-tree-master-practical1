# summing the digits in an integer

num = int(input("The integer is "))
num1 = num 
sum = 0


while (num1 > 0):
    sum += num1 % 10
    num1 //= 10

print("The summation of all the digits of {0} is {1}".format(num, num1))
