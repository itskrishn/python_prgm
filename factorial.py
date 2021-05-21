# -*- coding: utf-8 -*-
"""
Created on Sun May 16 00:44:11 2021

@author: shubh
"""

# Factorial of a number

class fac:
    def __init__(self, number):
        self.number = number
        # print(number)
        x= 1
        s=1
        # using while loop
        print("while loop")
        while x<= number:
            s = s*x 
            x =x+1
        print(s)
        #for loop
        print("for loop")
        for x in range(number, 0):
            s= s*x
            x=x-1
            
        print(s)

        
f1 = fac( int(input("Enter a number: ")))    