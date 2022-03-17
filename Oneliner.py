from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations
import string

d = {'IN': 2, 'GE': 2, 'AK': 3, 'BEG': 1}
sorted_dict = sorted(d.items(), key=lambda x: (x[1], len(x[0]), x[0]))
print("sorted dict", sorted_dict)
sor = {k: v for k, v in sorted_dict}
print("sor", sor)

print(ord('a'))
print(chr(100))

l = [1,2,3,4]
x = list(combinations(l,3))
z = list(permutations(l,2))
print(x)

def set_upper_text(text):
    print(text.upper())
    return text.upper()


input = ["123", "abc"]

l = list(map(set_upper_text, input))
print(l)

def my_func(b):
    print(b)
    print(*b)
    a,b,c = b
    print(a,b)

my_func([1,2,3])
my_func("abc")

first_dictionary = {'name': 'Fatos', 'location': 'Munich'}
second_dictionary = {'name': 'Fatos', 'surname': 'Morina',
                     'location': 'Bavaria, Munich'}
result = first_dictionary | second_dictionary
print(result)
print(f"Dict result is {result}")

def multiplexers():
    return [lambda n: index * n for index in range(4)]

print([m(2) for m in multiplexers ()]) # results [6, 6, 6, 6] It’s because of the late binding as the value of the variable <index> gets looked up after a call to any of multiplexers functions.

wordList='1,3,2,4,5,3,2,1,4,3,2'.split(',')
print(wordList)

def get_dict(input_List):
    """Can you iterate over a list of words and use a dictionary to keep track of the frequency(count) of each word? Consider the below example."""

    new_dict = {}
    for elem in input_List:
        new_dict[elem] = new_dict.get(elem, 0) + 1
    return new_dict

print(get_dict(wordList))

class Engineer:
    def __init__(self, name):
        self.name = name
        self.__salary = 6200

me = Engineer("Marius")
print(me.name)
print(me._Engineer__salary)

s = "fefe3 45"
print(s.isalnum())
print(s.isspace())

from collections import Counter
result = Counter("Banana")
print(result)
result = Counter([1,4,2,1,4,5,0])
print(result)
print(result.most_common())

my_list = ['1', 1, 0, 'a', 'b', 2, 'a', 'c', 'a']
print(max(my_list, key=my_list.count))
"""
l = [1,4,5,2,0,3]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)

def fibo(n):
    if n < 0:
        raise ValueError("ree")
    if not isinstance(n, int):
        raise TypeError("int expected")
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

l = [fibo(i) for i in range(10)]
print(l)

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

print(factorial(5))

full_choice = {"p": "paper", "r": "rock,", "s": "scissors"}
x = list(full_choice.keys())
for i in x:
    print(i)

s = list(reversed(x))
t = list(sorted(x))
print(s, t)
"""
print(f"My string is \n\t\n {s}.")
print(s.split()[-2].upper())