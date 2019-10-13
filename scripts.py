SOLVEMEFIRST
def solveMeFirst(a,b):
	# Hint: Type return a+b below
    return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

SAY 'HELLO WORLD!' WITH PYTHON
print("Hello, World!")

ARITHMETIC OPERATION
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
if a<b:
    print(b-a)
elif b<a:
    print(a-b)
print(a*b)

PYTHON:DIVISION
if __name__ == '__main__':
    a = int(input())
    b = int(input())
if b==0:
    print('nothing')
elif b!=0:
    print(a//b)
    print(a/b)
    
LOOPS
 if __name__ == '__main__':
    n = int(input())
for i in range(0,n):
    print(i*i)

PRINT FUNCTION
if __name__ == '__main__':
    n = int(input())
for i in range(1,n+1):
    print(i,end='')
    
PYTHON IF-ELSE
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0 or (n%2==0 and 6<=n<=20):
    print('Weird')
elif n%2==0 and (2<=n<=5 or n>20):
    print('Not Weird')

WRITE A FUNCTION
def is_leap(year):
    leap = False
    if (year%4==0 and year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
        return(True)
    elif (year%4==0 and year%100==0 and year%400!=0) or year%4!=0:
        return(leap)
    return(leap)

REDUCE A FUNCTION
def product(fracs):
    t = reduce(lambda x,y:x*y,fracs)
    return t.numerator, t.denominator

LIST COMPREHENSIONS
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
lst=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
print(lst)

FIND THE RUNNER-UP SCORE
if __name__ == '__main__':
    n = int(input())
    arr =input().split()
    arr.sort()
    lst0=[int(i) for i in arr]
    lst=[lst0[i] for i in range(len(lst0)) if lst0[i]!=lst0[i-1]]
    if all(i<0 for i in lst)==True:
        lst.remove(max(lst))
        print(min(lst))
    else:
        lst.remove(max(lst))
        print(max(lst))

FINDING THE PERCENTAGE
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=str(sum(student_marks[query_name])/len(student_marks[query_name]))+'0'
    print('%.2f' % float(a))

TUPLE
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    lst=[int(i) for i in integer_list]
    print(hash(tuple(lst)))

sWAP cASE
def swap_case(s):
    s1=''
    for i in s:
        if i.islower()==True:
            s1+=i.upper()
        elif i.isupper()==True:
            s1+=i.lower()
        elif i==' ':
            s1+=' '
        elif i.isalpha()==False:
            s1+=i
        elif i.isnumeric()==True:
            s1+=i
    return(s1)
  
STRING SPLIT AND JOIN
  def split_and_join(line):
    newline=line.split()
    newline='-'.join(newline)
    return(newline)

WHAT'S YOUR NAME?
def print_full_name(a, b):
    print("Hello"+" "+first_name+" "+last_name+"!"+" "+"You just delved into python.")

MUTATIONS
def mutate_string(string, position, character):
    s_new=string[:position]+character+string[position+1:]
    return(s_new)

TEXT ALIGNMENT
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
TEXT WRAP
def wrap(string, max_width):
    a=textwrap.fill(string,width=max_width)
    return(a)
    

