file = open("D:\FileHandling\FileRead.txt",'r')
print(file.read())
print()


file = open("D:\FileHandling\FileRead.txt",'r')
print(file.read(5))
print(file.readlines())


file = open("D:\FileHandling\FileRead.txt",'w')
file.write("Oeverwritten")
print(file.read(5))
print(file.readlines())

file = open("D:\FileHandling\Pycharmcreate.txt",'x')
file.write("Created by Pycharm")
file.close()
print(file.read(5))
print(file.readlines())

import os
if os.path.exists("FileRead.txt"):
 os.remove("FileRead.txt")
else:
   print("file do not exist")

   os.rmdir("myfolder")

print("---------------------EXCEL--------------------")

import pandas as pd

print(pd.__version__)

print(pd.read_excel("D:\PycharmExcel.xlsx"))
print(pd.read_excel("D:\PycharmExcel.xlsx", usecols="A:C",index_col=1))
print(pd.read_excel("D:\PycharmExcel.xlsx", usecols=[0,3]))
print(pd.read_excel("D:\PycharmExcel.xlsx", sheet_name=1,skiprows=[1,2]))

