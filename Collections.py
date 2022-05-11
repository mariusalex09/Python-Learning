#Collections module
import collections
import itertools
from typing import ChainMap, Counter
import re

#collections module implements specialized container datatypes providing alternatives to built-in containers like dict, list, set and tuple

#ChainMap   
#ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit; it is much faster than
#creating a dict and running multiple update() calls
#the class can be used for simulating nested scopes and is useful in templating

#class collections.ChainMap(*maps) a ChainMap groups multiple dicts or mappings to create together a single, updatable view. If no maps are specified,
# a single empty dict is created so that  a new chain always has at least one mapping
#the underlying map is a list which is public and can be accessed or updated using the maps attribute
#all dict methods are supported

#maps - a user updateable list of mappings; list is ordered from first-searched to last-searched; list should always contain at least one mapping

#new_child(m=None) - Returns a new ChainMap containing a new map followed by all of the maps in the current instance
"""
If m is specified, it becomes the new map at the front of the list of mappings; if not specified, an empty dict is used, so that a call to
 d.new_child() is equivalent to: ChainMap({}, *d.maps). This method is used for creating subcontexts that can be updated without altering values
 in any of the parent mappings.
"""

#parents 
"""
Property returning a new ChainMap containing all of the maps in the current instance except the first one. This is useful for skipping the first
map in the search. Use cases are similar to those for the nonlocal keyword used in nested scopes. The use cases also parallel those for the
 built-in super() function. A reference to d.parents is equivalent to: ChainMap(*d.maps[1:]).
"""
#Note: the iteration order of a ChainMap() is determined by scanning the mappings last to first

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
x = ChainMap(adjustments, baseline)
print(x) #ChainMap({'art': 'van gogh', 'opera': 'carmen'}, {'music': 'bach', 'art': 'rembrandt'})
print(list(ChainMap(adjustments, baseline))) #['music', 'art', 'opera']

#does same as dict.update()
combined = baseline.copy()
combined.update(adjustments)
print(list(combined)) #['music', 'art', 'opera']

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5}
d3 = {'f': 6, 'g': 7}

chain = {**d1, **d2, **d3}
print(chain) #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
chain = ChainMap(d1, d2, d3)
print(chain) #ChainMap({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}, {'f': 6, 'g': 7})
print(list(chain)) #['f', 'g', 'd', 'e', 'a', 'b', 'c']
print(chain.keys) #<bound method Mapping.keys of ChainMap({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}, {'f': 6, 'g': 7})>
for k,v in chain.items():
    print(k,v)

"""
f 6
g 7
d 4
e 5
a 1
b 2
c 3
"""

d4 = Counter(['h', 'h', 'i', 'i', 'j'])
chain = ChainMap(d1, d2, d3, d4)
print(chain) #ChainMap({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}, {'f': 6, 'g': 7}, Counter({'h': 2, 'i': 2, 'j': 1}))
print(chain.maps) #[{'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}, {'f': 6, 'g': 7}, Counter({'h': 2, 'i': 2, 'j': 1})]
print(chain.parents) #ChainMap({'d': 4, 'e': 5}, {'f': 6, 'g': 7}, Counter({'h': 2, 'i': 2, 'j': 1})) contains al except the first one  

#Counter
cnt = Counter()
for word in ["red", "blue", "red", "green", "blue", "blue"]:
    cnt[word] +=1
print(cnt) #Counter({'blue': 3, 'red': 2, 'green': 1})

#easier and same result
cnt = Counter(["red", "blue", "red", "green", "blue", "blue"])
print(cnt) #Counter({'blue': 3, 'red': 2, 'green': 1})

#find the ten most common used words in Hamlet using mostcommon() function
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
print(Counter(words).most_common(10)) #[('hamlet', 21), ('the', 18), ('his', 11), ('s', 11), ('to', 10), ('of', 9), ('and', 9), ('ghost', 7), ('king', 6), ('for', 5)]

#Counter is a dict subclass for counting hashatable objects; elements are the keys and their counts are the values; accepts a input any iterable or mapping

c = Counter("gallahad")
print(c.items())  #dict_items([('g', 1), ('a', 3), ('l', 2), ('h', 1), ('d', 1)])
print(c["a"]) #3

c = Counter({'red': 4, 'blue': 3})
c = Counter(cats = 4, dogs = 8)
#Counter objects return zero count for missing items instead of KeyError

c = Counter(['eggs', 'ham'])
print(c['bacon']) #0

#delete element from a counter with del
del c['ham']
print(c.items()) #dict_items([('eggs', 1)])

#Counter supports other methods too besides those of dictionaries excepting 2 of them: fromkeys() which is not supported and update() which work differently
#elements() return an iterator over elements reapeating each as many times as its count; if an element count is less than 1 it ignores; order is kept
c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements())) #['a', 'a', 'a', 'a', 'b', 'b']
print(sorted(c.elements())) #['a', 'a', 'a', 'a', 'b', 'b']

#mostcommon()
print(Counter('abracadabra').most_common()) #[('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
print(Counter('abracadabra').most_common(3)) #[('a', 5), ('b', 2), ('r', 2)]

#subtract() - elements are subtracted from an iterable or other counter; like dict.update() but subtract counts instead of replacing
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c) #Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

#update()
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.update(d) #behaves like a sum compared to subtract, so make the opposite
print(c) # Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2})

c = Counter(a=3, b= 1)
d = Counter(a=1, b=2)
print(sum(c.values())) #4
#c.clear() #reset all counts
#list(c) list unique elements
#set(c) convert to a set
#dict(c) convert to a normal dict
#c.items() convert to a list of (elem, cnt) pairs
#Counter(dict(list_of_pairs)) convert from a list of (elem, cnt) pairs
#c.mostcommon()[:-n-1:-1] n least common elements
# +c remove zero and negative counts

c = Counter(a=3, b= 1)
d = Counter(a=1, b=2)
#some mathematical operations are provided for combining Counter objects to produce multisets
print(c + d) #Counter({'a': 4, 'b': 3})
print(c - d) #Counter({'a': 2}) as keeps only positive values
print(c & d) #Counter({'a': 1, 'b': 1}) intersection: min(c[x], d[x])
print(c | d) #Counter({'a': 3, 'b': 2}) union: max[c[x], d[x]]

c = Counter(a=4, b=-2)
print(+c) #Counter({'a': 4})
print(-c) #Counter({'a': 4})


"""deques for lists
class collections.deque([iterable[, maxlen]])
read as "deck" can append to both left and right of lists; returns a new deque object from an iterable; if iterable is not provided an empty deque object is created
deques are a genralization of stacks and queues with O(1) perofrmance in either direction so thread-safe and memory-efficient
if maxlen is not specified or is None, deque can grow to an arbitrary length; otherwise it is bounded to maxlen;
 if deque is full, when new items are added, a coresponding nunber of items are discarded from the opposite end
supports lists methods as well left-applicable ones e.g. appendleft() or popleft()
"""

d = collections.deque('ghi')
for elem in d:
    print(elem)
"""
g
h
i
"""
d.append('j')
d.appendleft('f')
print(d) #deque(['f', 'g', 'h', 'i', 'j'])
d.popleft()
print(d) #deque(['g', 'h', 'i', 'j'])
d.rotate()
print(d) #deque(['j', 'g', 'h', 'i'])
d.rotate(-1)
print(d) #deque(['g', 'h', 'i', 'j'])
d.rotate(-3)
print(d) #deque(['j', 'g', 'h', 'i'])
d.extendleft('abc')
print(d) #deque(['c', 'b', 'a', 'j', 'g', 'h', 'i'])
d.extend('abc')
print(d) # deque(['c', 'b', 'a', 'j', 'g', 'h', 'i', 'a', 'b', 'c'])

#useful recipes
def tail(filename, n = 10):
    """return the last n lines of a file"""
    with open(filename) as f:
        return collections.deque(f, n)

#implementation of delete function as deque does not support deletion del[n]
#d.pop() removes the rightmost element so cannot specify an indey like for list 
l =[1,2,4]
print(l.pop(-2)) #2

#rotate() provides a way to implement deletion and slicing
def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

d = collections.deque([1, 3, 5]) #deque([1, 3, 5])
delete_nth(d, 2)
print(d) #deque([1, 3])
d = collections.deque([1, 3, 5]) #deque([1, 3, 5])

#Another approach to using deques is to maintain a sequence of recently added elements by appending to the right and popping to the left:
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    print(f"Iteration it: {it}")
    d = collections.deque(itertools.islice(it, n-1))
    print(f"Deque: {d}")
    d.appendleft(0)
    print(f"Deque after append: {d}")
    s = sum(d)
    print(f"Sum: {s}")
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


x = moving_average([40, 30, 50, 46, 39, 44])
print(next(x)) #40.0
print(next(x)) #42.0
print(next(x)) #45.0
print(next(x)) #43.0
#print(next(x)) #StopIteration

#A round-robin scheduler can be implemented with input iterators stored in a deque. Values are yielded from the active iterator in position zero. If that iterator is exhausted, it can be removed with popleft(); otherwise, it can be cycled back to the end with the rotate() method:

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = collections.deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()


"""defaultdict objects
class collections.defaultdict(default_factory=None, /[, ...])
Return a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable. The remaining functionality is the same as for the dict class and is not documented here.
The first argument provides the initial value for the default_factory attribute; it defaults to None. All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
"""

#examples of defaultdict
#1 use list as the default_factory; it is easy to group a sequence of key-value pairs into a dictionary of lists
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d) #defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
print(d.items()) #dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])

"""
Explanation: When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created using the default_factory function which returns an empty list. The list.append() operation then attaches the value to the new list. When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the list.append() operation adds another value to the list. 
This technique is simpler and faster than an equivalent technique using dict.setdefault():
"""

d = {}
for k, v in s:
    d.setdefault(k, []).append(v)
print(d.items()) #dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])

#Setting the default_factory to int makes the defaultdict useful for counting (like a bag or multiset in other languages):
s = 'mississippi'
d = collections.defaultdict(int)
for elem in s:
    d[elem] += 1
print(d.items()) #dict_items([('m', 1), ('i', 4), ('s', 4), ('p', 2)])

#Setting the default_factory to set makes the defaultdict useful for building a dictionary of sets:
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = collections.defaultdict(set)
for k, v in s:
    d[k].add(v)
print(d.items())