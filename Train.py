# This is a file for trying and learning
import string

list_1 = [2, 0, 3, 5, 6, 7]
#prints options for given argument e.g.  'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
#print(dir(list_1))
#prints documentation detailed on given argument; similar to dir() but extended
#print(help(list_1))

#Numbers
x = 4
y = 5
#int division
#print(y//x)
#float division
#print(y/x)
#print(type(y))
#print(float(x))

#Strings - immutable, iterable
text = "my message"
#print(dir(text))
# some functions for strings: 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
# f print
print(f"Hello! this is my message: {text.upper()} instead of original {text}")

#Lists
list_1 = [2, 0, 3, 5, 6, 7]
list_2 = list(list_1) #use list() constructor to make a copy of list_1
list_1.pop()
print(list_1, list_2)
#slicing
print(list_2[2:5]) #slicing includes starting index but excludes ending index
#list comprehension
squares = [i**2 for i in range(1,11) if i%2 == 0 if i%4 == 0]
print(squares)
A =[1, 3, 5, 7]
B =[2, 4, 6 ,8]
#cartesian product
C = [(a,b) for a in A for b in B]
print(C)
list_2.reverse()
print(list_2)
list_2.remove(7)
print("removed elem 7", list_2)
list_2.insert(5,10)
print("added elem 10 at pos 5",list_2)
set_x = set(list_2)
set_x.add(44)
print(set_x)
print(dir(set_x))
#functions for sets:'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

#Tuples
my_tuple = ()
my_tuple = (6, ) # To make a tuple with just one element you need to type a comma at the end.
my_tuple = 3, 5
#tuple unpacking
survey2 = (31, "Switzerland", False)
age, country, knows_python = survey2
list_tuple = tuple(list_1)
print(type(list_tuple))
print(sum(list_tuple))

#Functions
#Keyword arguments help you to write flexible functions and clean code.
#There are two kinds of arguments you can use when writing a function. A keyword argument (or default argument), which has an equal sign, and a required argument which does not have an equal sign. When writing a function, you can use both kinds of arguments. But if you do this, the keyword arguments must come last.
def g(y, x = 0):
    print(x + y)

#Lambda functions - are anonymous functions and are small, one line
compute_remainder = lambda x, y: x % y
r = compute_remainder(10, 3)
print(r)

full_name = lambda first, last: first.strip().title() + " " + last.strip().title()
print(full_name(" leonhard", "EUler"))

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
ordered_authors = sorted(scifi_authors, key=lambda name: name.split()[-1].lower())
print(ordered_authors)

def create_multiplier_function(n):
    return lambda x: x * n

my_doubler = create_multiplier_function(11)
print(my_doubler(2)) #result 22

def make_quadratic_function(a, b, c):
    return lambda x: a*x**2 + b*x + c

f = make_quadratic_function(2, 3, -5)
print(f(0))
print(f(2))

#Exceptions
a = 42
b = 10
c = 0
try:
    remainder = (a + b) % c
except (TypeError, NameError) as err:
    print(f"Cannot compute result, reason: {err}.")
except Exception as err:
    print(f"A {type(err)} occurred, please inspect: {err}.")

def foo(x = []):
    print(f"x value is {x}")
    x.append(1)
    return x

print(foo())
print(foo(x=[]))
print(foo())
print(foo(x=[]))
print(foo())

#Dictionaries
d = {"a":1, "b":2}
e = dict.copy(d)
print(type(e) == dict)



keys = ["name", "phone", "email"]
values = ["Mike", "+40791882123", "michael@yahoo.com"]

d = dict(zip(keys, values))
print(d)
#elem = d.popitem()
#print(elem)
print(d.setdefault("name", "klk"))
print(d.setdefault("age", "44"))
print(d)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("model",car.get("model", "NA"))

post = {"user_id": 209, "message": "I am learning about dictionaries. Yay!", "language": "English", "created": "2021-03-02T10:11:06.278326", "location": (46.766667, 23.583333)}

ordered_dict = sorted(post.items(), key=lambda x: x[0])
print(ordered_dict)

text = "He ordered his regular breakfast. Two eggs sunnyside up, hash browns, and two strips of bacon. He continued to look at the menu wondering if this would be the day he added something new. This was also part of the routine. A few seconds of hesitation to see if something else would be added to the order before demuring and saying that would be all. It was the same exact meal that he had ordered every day for the past two years."

def count_words_in_text(input_text):
    """Function that populates a dict with words and their frequency"""
    if not isinstance(text, str):
        raise TypeError(f"Expected input is string. Provided input is {type(text)}")
    freq_word = {}
    for word in input_text.split():
        clean_word = word.strip(string.punctuation).lower()
        freq_word[clean_word] = freq_word.get(clean_word, 0) + 1
    return freq_word

split_text = count_words_in_text(text)
print(split_text)
d_sorted = dict(sorted(split_text.items()))
print(d_sorted)
print(type(d_sorted))
print(count_words_in_text.__doc__)


if __name__ == '__main__':
    print("main")
    #Q1: what is doing: if __name__ == '__main__':  ???
    #print(help(function_test()))

l1 = [2,3,2,5]
l2 = set(l1)
litems = [elem for elem in l1 if elem not in l2]
print(litems)

from collections import Counter
count = Counter(l1).items()
items = [item for item, count in Counter(l1).items() if count > 1]
print(items)

import random
print(random.randint(5, 100))

a = [1,2,4,2]
my_list = [y-x for x,y in zip(a, a[1:])]
print(my_list)

def test(x, y, z):
    print(x, y, z)
res = test(**{'x': 1, 'y': 2, 'z': 3})


