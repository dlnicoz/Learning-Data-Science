# learning all basics of python from beginning

# print("hello dheeraj sahani")


import sys
print(sys.version)


# variables in python

# x = 4
# y = 10
# c = y - x
# print (c)

# x = int(4)
# y = str(5)
# z = float(4)
#
# print(type(x) , type(y) ,type(z) )

# stucture

# x = y = z = "hello "
# print(x)
# print(y)
# print(z)

# unpack collection

# fruits = ["apple", "orange", "banana"]
# x , y , z = fruits
# print(x)
# print(y)
# print(z)

# learn about global and local variables

# x = " dheeraj sahani "
#
# def full_name():
#     x = "adheeraj sahani"
#     a = "good moring "
#     print(a + x)
#     
# full_name()
#
# print("good moring " + x)


# conversion of variables

# x = 1
# y = 2.4
# z = 1j
#
# a = float(x)
# print(type(a))

# use of random number

# import random
#
# print(random.randrange(1 ,20))

# lets learn loops in while do while 

# thelist = ["apple" , "banana", "strawberry", "orange"]
# for x in thelist:
#     print(x)


# thelist = ["apple" , "banana", "strawberry", "orange"]
# x = 0

# for i in range(20):
#     print(i)

# i =0
# while i <= 20 : 
#     print(i)
#     i += 1

# def fib(n):
#     a, b = 0 ,1 
#     for x in range(n) : 
#         print(a )
#         a ,b = b , a +b
#
# fib(30)



# writing bmi formula 
#
# def calculate_bmi(we , he):
#     bmi = we / (he ** 2)
#     return bmi
# def bmi_category(bmi):
#     if bmi < 18.5:
#         return "underweigth"
#
#     elif 18.5 <= bmi < 24.9:
#         return "normal weight"
#     elif 25 <=bmi < 29.9:
#         return "overweigth"
#     else:
#         return "obesity"
# def main():
#     try:
#         we = float(input("enter weight"))
#         he = float(input("enter height"))
#
#         bmi = calculate_bmi(we , he)
#
#         category = bmi_category(bmi)
#
#         print(f"your bmi is :{bmi:.2f}")
#         print(f"you are classified as :{category}")
#
#     except ValueError:
#         print("invalid input")
# if __name__ == "__main__": 
#     main()
