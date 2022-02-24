#!/usr/bin/env python
# coding: utf-8

# # 기본 자료형

# We introduce here the Python language. Only the bare minimum
# necessary for getting started with Numpy and Scipy is addressed here.
# To learn more about the language, consider going through the
# excellent tutorial https://docs.python.org/tutorial. Dedicated books
# are also available, such as [Dive into Python 3](https://diveintopython3.net/).

# ## First steps

# Start the **Ipython** shell (an enhanced interactive Python shell).

# Once you have started the interpreter, type
# 
# ```python
# >>> print("Hello, world!")
# Hello, world!
# ```

# The message "Hello, world!" is then displayed. You just executed your
# first Python instruction, congratulations!

# To get yourself started, type the following stack of instructions.

# ```python
# >>> a = 3
# >>> b = 2*a
# >>> type(b)     # doctest: +SKIP
# <type 'int'>
# >>> print(b)
# 6
# >>> a*b 
# 18
# >>> b = 'hello' 
# >>> type(b)    # doctest: +SKIP
# <type 'str'>
# >>> b + b
# 'hellohello'
# >>> 2*b
# 'hellohello'
# ```

# Two variables `a` and `b` have been defined above. Note that one does
# not declare the type of a variable before assigning its value. In C,
# conversely, one should write:

# ```c
# int a = 3;
# ```

# In addition, the type of a variable may change, in the sense that at
# one point in time it can be equal to a value of a certain type, and a
# second point in time, it can be equal to a value of a different
# type. `b` was first equal to an integer, but it became equal to a
# string when it was assigned the value `'hello'`. Operations on
# integers (`b=2*a`) are coded natively in Python, and so are some
# operations on strings such as additions and multiplications, which
# amount respectively to concatenation and repetition.

# ## Basic types

# ### Numerical types

# Python supports the following numerical, scalar types:

# **Integer**
# 
# ```python
# >>> 1 + 1
# 2
# >>> a = 4
# >>> type(a)   # doctest +SKIP
# <type 'int'>
# ```

# **Floats**
# 
# ```python
# >>> c = 2.1
# >>> type(c)   # doctest +SKIP
# <type 'float'>
# ```

# **Booleans**
# 
# ```python
# >>> 3 > 4
# False
# >>> test = (3 > 4)
# >>> test
# False
# >>> type(test)      # doctest +SKIP
# <type 'bool'>
# ```

# A Python shell can therefore replace your pocket calculator, with the
# basic arithmetic operations `+`, `-`, `*`, `/`, `%` (modulo)
# natively implemented
# 
# ```python
# >>> 7 * 3.
# 21.0
# >>> 2**10
# 1024
# >>> 8 % 3
# 2
# ```

# Type conversion (casting)
# 
# ```python
# >>> float(1)
# 1.0
# ```

# **warning Integer division**
# 
# ```python
# >>> 3 / 2   # doctest +SKIP
# 1.5
# ```

# **To be safe** use floats
# 
# ```python
# >>> 3 / 2.
# 1.5
# 
# >>> a = 3
# >>> b = 2
# >>> a / float(b)
# 1.5
# ```

# If you explicitly want integer division use `//`
# 
# ```python
# >>> 3.0 // 2
# 1.0
# ```

# ### Containers

# Python provides many efficient types of containers, in which
# collections of objects can be stored.

# #### Lists

# A list is an ordered collection of objects, that may have different
# types. For example
# 
# ```python
# >>> colors = ['red', 'blue', 'green', 'black', 'white']
# >>> type(colors)     # doctest +SKIP
# <type 'list'>
# ```

# Indexing accessing individual objects contained in the list
# 
# ```python
# >>> colors[2]
# 'green'
# ```

# Counting from the end with negative indices
# 
# ```python
# >>> colors[-1]
# 'white'
# >>> colors[-2]
# 'black'
# ```

# **warning**
# 
# **Indexing starts at 0** (as in C), not at 1 (as in Fortran or Matlab)!

# Slicing obtaining sublists of regularly-spaced elements
# 
# ```python
# >>> colors
# ['red', 'blue', 'green', 'black', 'white']
# >>> colors[24]
# ['green', 'black']
# ```

# **Warning**
# 
# Note that `colors[startstop]` contains the elements with indices `i`
# such as  `start<= i < stop` (`i` ranging from `start` to
# `stop-1`). Therefore, `colors[startstop]` has `(stop - start)` elements.

# **Slicing syntax** `colors[startstopstride]`
# 
# All slicing parameters are optional:
# 
# ```python
# >>> colors
# ['red', 'blue', 'green', 'black', 'white']
# >>> colors[3]
# ['black', 'white']
# >>> colors[3]
# ['red', 'blue', 'green']
# >>> colors[2]
# ['red', 'green', 'white']
# ```

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

# **Methods and Object-Oriented Programming**
# 
# The notation `rcolors.method()` (e.g. `rcolors.append(3)` and `colors.pop()`) is our
# first example of object-oriented programming (OOP). Being a `list`, the
# object `rcolors` owns the *method* `function` that is called using the notation
# **.**. No further knowledge of OOP than understanding the notation **.** is
# necessary for going through this tutorial.

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

# #### Strings

# Different string syntaxes (simple, double or triple quotes)
# 
# ```python
# s = 'Hello, how are you?'
# s = "Hi, what's up"
# s = '''Hello,
#    how are you'''         # tripling the quotes allows the
#                           # string to span more than one line
# s = """Hi,
# what's up?"""
# ```

# ```python
# In [1] 'Hi, what's up?'
# ------------------------------------------------------------
# File "<ipython console>", line 1
# 'Hi, what's up?'
#        ^
# SyntaxError invalid syntax
# ```

# This syntax error can be avoided by enclosing the string in double quotes
# instead of single quotes. Alternatively, one can prepend a backslash to the
# second single quote. Other uses of the backslash are, e.g., the newline character
# `\n` and the tab character `\t`.

# Strings are collections like lists. Hence they can be indexed and
# sliced, using the same syntax and rules.

# Indexing
# 
# ```python
# >>> a = "hello"
# >>> a[0]
# 'h'
# >>> a[1]
# 'e'
# >>> a[-1]
# 'o'
# ```

# (Remember that negative indices correspond to counting from the right
# end.)

# Slicing
# 
# ```python
# >>> a = "hello, world!"
# >>> a[36] # 3rd to 6th (excluded) elements elements 3, 4, 5
# 'lo,'
# >>> a[2102] # Syntax a[startstopstep]
# 'lo o'
# >>> a[3] # every three characters, from beginning to end
# 'hl r!'
# ```

# Accents and special characters can also be handled as in Python 3
# strings consist of Unicode characters.

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

# Strings have many useful methods, such as `a.replace` as seen
# above. Remember the `a.` object-oriented notation and use tab
# completion or `help(str)` to search for new methods.

# **seealso**
# 
# Python offers advanced possibilities for manipulating strings,
# looking for patterns or formatting. The interested reader is referred to
# https//docs.python.org/library/stdtypes.html#string-methods and
# https//docs.python.org/3/library/string.html#format-string-syntax

# String formatting
# 
# ```python
# >>> 'An integer %i; a float %f; another string %s' % (1, 0.1, 'string') # with more values use tuple after %
# 'An integer 1; a float 0.100000; another string string'
# 
# >>> i = 102
# >>> filename = 'processing_of_dataset_%d.txt' % i   # no need for tuples with just one value after %
# >>> filename
# 'processing_of_dataset_102.txt'
# ```

# #### Dictionaries

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

# #### More container types

# **Tuples**
# 
# Tuples are basically immutable lists. The elements of a tuple are written
# between parentheses, or just separated by commas
# 
# ```python
# >>> t = 12345, 54321, 'hello!'
# >>> t[0]
# 12345
# >>> t
# (12345, 54321, 'hello!')
# >>> u = (0, 2)
# ```

# **Sets** unordered, unique items
# 
# ```python
# >>> s = set(('a', 'b', 'c', 'a'))
# >>> s    # doctest +SKIP
# set(['a', 'c', 'b'])
# >>> s.difference(('a', 'b'))    # doctest +SKIP
# set(['c'])
# ```

# ### List Comprehensions
# 
# Instead of creating a list by means of a loop, one can make use
# of a list comprehension with a rather self-explaining syntax.
# 
# ```python
# >>> [i**2 for i in range(4)]
# [0, 1, 4, 9]
# ```
