import os
from datetime import datetime

print(dir(os))
print(os.getcwd())
os.chdir("C:\PythonTraining\pythonProject")
print(os.getcwd())
print(os.listdir())
os.mkdir("folder new created by OS")
os.removedirs("folder new created by OS")

#intrebari
"""
2. functia cu parametru x =[]

def foo(x=[]):
    x.append(1)
    print(x)
foo()
foo()
3. unit test in PY e Pytest?
4. librarii uzuale
5. la clase ce mai e in afara de inheritance, overloading?

6. collection lib ?
"""


def foo(x=None):
    if x == None:
        x = list()
    x.append(1)
    print(x)
foo()
foo()

foo(x=["a","b","c"])
foo()
foo()