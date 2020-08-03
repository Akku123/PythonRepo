
from unittest import TestCase
def test_evenodd():
    num = open("D:/FileHandling/FileRead.txt", "r")
    print(num.read())
    t = num.read()
    print(t.isdigit())
    if t == 5:
        print("number is even")
    else:
        print("Number is odd")

