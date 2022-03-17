# Python program to use
# main for function call.
import File_A
from subfolder_test import File_C

print("into File_B")
def my_functionB():
    print("I am inside function of File_B")

d2 = {'a': 10, 'b': 20, 'c': 30}
print(d2.items())
print(d2["b"])
print("exit File_B")

def main():
    my_functionB()
    File_A.my_function()
    File_C.my_functionC()
    print(File_C.d)
    print(File_A.d)

if __name__ == '__main__':
    main()


