# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:19:25 2019

@author: nawaz
"""

def print_rangoli(size):
    # your code goes here
    alp='abcdefghijklmnopqrstuvwxyz'
    for i in range((size*2)-1):
        for j in range((size*2)-1):
            a=abs(size-1-i)
            b=2*(size-1)-a
            if j in range(a,b+1):
                if(j==size-1):
                    print(alp[abs(size-1-i)],end="")
                elif(j<size-1):
                    print(alp[size-1-(j-a)],end="-")
                elif(j>size-1):
                    print("-",alp[size-1-(b-j)],sep="",end="")
            else:
                print("--",end="")
        print("")
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)