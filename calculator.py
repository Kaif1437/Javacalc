#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     22-02-2023
# Copyright:   (c) Admin 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
m=0
s=4
while m<4:
    n=int(input('Enter 1st number:::'))
    y=input('Enter operation:,+,-,/,*,%:::')
    z=int(input('Enter 2nd number:::'))
    if y=='+':
        k=n+z
        print("addition of above numbers inserted",k)
    elif y=='-':
        print('Substraction of entered numbers')
        print(n-z)
    elif y=='/':
        print('division of entered numbers')
        print(n/z)
    elif y=='*':
        print('Multiplication of numbers')
        print(n*z)
    elif y=='%':
        print('Remainder of entered numbers')
        print(n%z)
    else:
        print('invalid operation')
m=m+1