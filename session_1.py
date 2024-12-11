# welcome to the world of python
# alt+shift+. increase
# alt+shit+, decrease
# ctrl + / to convert a code or line to comment

# print('hi')
# print(1)
# print(5+10)
# print(11//5)#floor
# print(10/0)
# print(7//2)#floor division
#
# print("""
# *
# **
# ***
# ****
# *****
# """)
# print('Hi "Anu" welocme')
# print("Hi 'Anu' welocme")
# Hi 'Anu' welcome, it's your car
# print("Hi 'Anu' welcome, it's your car")
# print("Hi" 'Anu' welocme, it's your "caar")
# print("""Hi 'Anu' welocme, it's your "caar".""")
# Hi 'Anu' welocme, it's """your""" "caar".
# print('Hi \"Anu\", it\'s your car')
#
#
# print('Hi, I\'m a \"Python" mentor')
# types esc.seq..
# \t tab esc.seq
# \n next line
# \b backspace
# \x hexadecimal value
# types esc.seq..
# \t tab esc.seq
# \n next line
# \b backspace
# \x hexadecimal value
# print('\tHi\n, I\'m\b a \"Python" me\ntor')
# \t tab key gives 4 space

# print("*\n**\n***\n****\n*****")
#data types
#int
#float
#String
#boolean (True, False)
#complex (imaginary number 5+6j)
#none
# a=1
# b="hello"
# c=7.5
# d=True
# print(type(a),type(b),type(c),type(d))
# img=(5+6j)
# print(type(img))
#camelcasing and pascal casing
#pythonFileTwo camel casing
#pascal casing PythonFileTwo
#Python_File_Two
#concatenation
# a="Hey"
# b="Helooo"
# c=10
# d=5.5
# #
# e = c+d
# print(e)
# f = a+" "+b
# print(f)
# c=20
# d=20
# e=20
# print(id(c))
# print(id(d))
# print(id(e))
# # print(id(a))

# _num1="ABC"
# _num2="ABC"
# Age =10
# AGE =20
# print(Age,AGE)

#type casting

# A=20
# print(type(A))
# print(A)
# A=float(A)#type casting
# print(type(A))
# print(A)
# Div1akar1=str(A)
# print(type(Div1akar1))
# print(Div1akar1)
# B=float(Div1akar1)
# print(type(B))

# name2=input("Enter your name:")
# age2=float(input("Enter your age:"))
# print("Name of the candidate is",name2)

# num1=input("enter the 1st number: ")
# num2=input("enter the 2nd number: ")
# sum_1=num1+num2
# print(num1,num2,sum_1)
# num1=int(input("enter the 1st number: "))
# num2=int(input("enter the 2nd number: "))
# sum_1=num1+num2
# print(num1,num2,sum_1)

# print("first number is {} second number is {} and sum is {}")
# print("first number is {num1} second number is {num2} and sum is {sum1}")

print("first number is {} second number is {} and sum is {}".format(num1,num2,sum_1))

print("first number is {2} second number is {0} and sum is {1}".format(num1,num2,sum_1))

num1=int(input("enter the 1st number: "))
num2=int(input("enter the 2nd number: "))
sum_1=num1*num2
print("first number is {} second number is {} and sum is {}".format(num1,num2,sum_1))