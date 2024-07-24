# print("hello")
# print("dheeraj sahani");
# import sys
# print(sys.version)
# if 5 > 2: 
#     print("2 , is smaller")
#     print ("hello again")
# x = 8
# y = 10
# c = x - y
# print(c)
#
# x = str(5)
# y = int(10)
# c = float(11)
# print(type(x) , type(y) , type(c))
T = int(input())
for i in range(T):
    N = input()
    if N[0] == "0":
        print(N)  # If the string starts with "0", just print it as it is
    else:
        print(N[::-1])  # This reverses the string using slicing

