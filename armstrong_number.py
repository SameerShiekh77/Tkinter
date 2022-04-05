# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum1
sum1 = 0

# find the sum1 of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   # print(digit)
   sum1 += digit ** 3
   temp //= 10

# display the result
if num == sum1:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
