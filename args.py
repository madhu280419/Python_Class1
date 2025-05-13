# w = input()
# if w == "sunny":
#     print("play cricket")
# elif w == "rainy":
#     print("play cubes")
# else:
    # print("play inside")
    
    
# name = "pranay"
# list = []
# for i in range(1,len(name)):
#     print(name[i])

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# operator = input("Enter operator: ")
# if operator == "+":
#     print(f"addition of 2 numbers is {num1 + num2}")
# elif operator == "-":
#     print(f"subtraction of 2 numbers is {num1 - num2}")
# elif operator == "*":
#     print(f"multiplication of 2 numbers is {num1 * num2}")
# elif operator == "/":
#     print(f"division of 2 numbers is {num1 / num2}")
# else:
#     print("invalid operator")

# list =[10,20,30,40,50,60,70,80]
# # print(list[1:7:3])
# print(list[-1::-1])
# print(list[1::1])

# def hourglass_pattern(n):
#     for i in range(n, 0, -1):
#         print(" " * (n - i) + "* " * i)
#     for i in range(2, n + 1):
#         print(" " * (n - i) + "* " * i)
# n = 5
# print(hourglass_pattern(n))

# s = "hello world"
#print(s[1]
#print(s[-1])
# print(s[1:3])
# print(s[1:-1])
# print(s[:3])
# print(s[2:])
# print(s[:-1])
# print(s[::2])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])

# a =[8,3,5,6,1,2,7,11,9]
# print(a[-1])

# i=j=[3]
# i += j
# print(i,j)
import random
num = random.randint(0,1)
# print(num)
# flip = random.choice(['Heads', 'Tails'])
# print(flip)
if num > 0.5:
    print('Heads')
else:
    print('Tails')