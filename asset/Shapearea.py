# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jbnz4qAbnNnqwgAQsgT-mt-jvaN4Lgo7
"""

print("Kindly choose the shape which area you are calculating.")
print("A. Triangle")
print("B. Rectangle")
print("C. Circle")
k=(input())
if (k=="A"):
  print("input Base of triangle")
  b=int(input())
  b = abs(b) # Converting to positive if negative
  print("input height of triangle")
  h=int(input())
  h = abs(h) # Converting to positive if negative
  Ar= 1/2*b*h
  print(Ar)
if (k=="B"):
 print("Input the length of the Rectangle ")
 l=int(input())
 l = abs(l) # Converting to positive if negative
 print("Input the Width of the Rectangle ")
 w=int(input())
 w = abs(w) # Converting to positive if negative
 Ar=l*w
 print(Ar)
if (k=="C"):
 import math
 print("Input the Radius of the Circle ")
 r=int(input())
 r = abs(r) # Converting to positive if negative
 Ar=math.pi*r*r
 print(Ar)