#!/usr/bin/env python
# coding: utf-8

# # 모음 자료형 2편

# 집합형 컨테이너 두 개를 소개한다.

# ## 집합

# unordered, unique items
# 
# ```python
# >>> s = set(('a', 'b', 'c', 'a'))
# >>> s    # doctest +SKIP
# set(['a', 'c', 'b'])
# >>> s.difference(('a', 'b'))    # doctest +SKIP
# set(['c'])
# ```

# ## 사전

# A dictionary is basically an efficient table that **maps keys to
# values**. It is an **unordered** container

# ```python
# >>> tel = {'emmanuelle' 5752, 'sebastian' 5578}
# >>> tel['francis'] = 5915
# >>> tel     # doctest +SKIP
# {'sebastian' 5578, 'francis' 5915, 'emmanuelle' 5752}
# >>> tel['sebastian']
# 5578
# >>> tel.keys()   # doctest +SKIP
# ['sebastian', 'francis', 'emmanuelle']
# >>> tel.values()   # doctest +SKIP
# [5578, 5915, 5752]
# >>> 'francis' in tel
# True
# ```

# It can be used to conveniently store and retrieve values
# associated with a name (a string for a date, a name, etc.). See
# https//docs.python.org/tutorial/datastructures.html#dictionaries
# for more information.

# A dictionary can have keys (resp. values) with different types
# 
# ```python
# >>> d = {'a'1, 'b'2, 3'hello'}
# >>> d       # doctest +SKIP
# {'a' 1, 3 'hello', 'b' 2}
# ```

# ## 수정 가능성

# ### 문자열

# A string is an **immutable object** and it is not possible to modify its
# contents. One may however create new strings from the original one.
# 
# ```python
# In [53] a = "hello, world!"
# In [54] a[2] = 'z'
# ---------------------------------------------------------------------------
# Traceback (most recent call last)
# File "<stdin>", line 1, in <module>
# TypeError 'str' object does not support item assignment
# 
# In [55] a.replace('l', 'z', 1)
# Out[55] 'hezlo, world!'
# In [56] a.replace('l', 'z')
# Out[56] 'hezzo, worzd!'
# ```

# ### 리스트

# Lists are *mutable* objects and can be modified
# 
# ```python
# >>> colors[0] = 'yellow'
# >>> colors
# ['yellow', 'blue', 'green', 'black', 'white']
# >>> colors[24] = ['gray', 'purple']
# >>> colors
# ['yellow', 'blue', 'gray', 'purple', 'white']
# ```

# **Note**
# 
# The elements of a list may have different types
# 
# ```python
# >>> colors = [3, -200, 'hello']
# >>> colors
# [3, -200, 'hello']
# >>> colors[1], colors[2]
# (-200, 'hello')
# ```

# For collections of numerical data that all have the same type, it
# is often **more efficient** to use the `array` type provided by
# the `numpy` module. A NumPy array is a chunk of memory
# containing fixed-sized items.  With NumPy arrays, operations on
# elements can be faster because elements are regularly spaced in
# memory and more operations are performed through specialized C
# functions instead of Python loops.

# Python offers a large panel of functions to modify lists, or query
# them. Here are a few examples; for more details, see
# https//docs.python.org/tutorial/datastructures.html#more-on-lists

# Add and remove elements
# 
# ```python
# >>> colors = ['red', 'blue', 'green', 'black', 'white']
# >>> colors.append('pink')
# >>> colors
# ['red', 'blue', 'green', 'black', 'white', 'pink']
# >>> colors.pop() # removes and returns the last item
# 'pink'
# >>> colors
# ['red', 'blue', 'green', 'black', 'white']
# >>> colors.extend(['pink', 'purple']) # extend colors, in-place
# >>> colors
# ['red', 'blue', 'green', 'black', 'white', 'pink', 'purple']
# >>> colors = colors[-2]
# >>> colors
# ['red', 'blue', 'green', 'black', 'white']
# ```

# Reverse
# 
# ```python
# >>> rcolors = colors[-1]
# >>> rcolors
# ['white', 'black', 'green', 'blue', 'red']
# >>> rcolors2 = list(colors) # new object that is a copy of colors in a different memory area
# >>> rcolors2
# ['red', 'blue', 'green', 'black', 'white']
# >>> rcolors2.reverse() # in-place; reversing rcolors2 does not affect colors
# >>> rcolors2
# ['white', 'black', 'green', 'blue', 'red']
# ```

# Concatenate and repeat lists
# 
# ```python
# >>> rcolors + colors
# ['white', 'black', 'green', 'blue', 'red', 'red', 'blue', 'green', 'black', 'white']
# >>> rcolors * 2
# ['white', 'black', 'green', 'blue', 'red', 'white', 'black', 'green', 'blue', 'red']
# ```

# Sort
# 
# ```python
# >>> sorted(rcolors) # new object
# ['black', 'blue', 'green', 'red', 'white']
# >>> rcolors
# ['white', 'black', 'green', 'blue', 'red']
# >>> rcolors.sort()  # in-place
# >>> rcolors
# ['black', 'blue', 'green', 'red', 'white']
# ```

# ## List Comprehensions
# 
# Instead of creating a list by means of a loop, one can make use
# of a list comprehension with a rather self-explaining syntax.
# 
# ```python
# >>> [i**2 for i in range(4)]
# [0, 1, 4, 9]
# ```

# ## Methods and Object-Oriented Programming

# The notation `rcolors.method()` (e.g. `rcolors.append(3)` and `colors.pop()`) is our
# first example of object-oriented programming (OOP). Being a `list`, the
# object `rcolors` owns the *method* `function` that is called using the notation
# **.**. No further knowledge of OOP than understanding the notation **.** is
# necessary for going through this tutorial.
# 
# **Discovering methods**
# 
# Reminder in Ipython tab-completion (press tab)
# 
# ```python
# In [28] rcolors.<TAB>
# rcolors.append   rcolors.index    rcolors.remove   
# rcolors.count    rcolors.insert   rcolors.reverse  
# rcolors.extend   rcolors.pop      rcolors.sort    
# ```
