#!/usr/bin/env python
# coding: utf-8

# # 기본 자료형

# 데이터 과학을 위해 필수적으로 알아야 하는 
# 파이썬 프로그래밍 언어의 사용법을 소개한다.
# 파이썬 프로그래밍의 보다 체계적인 학습은
# [파이썬 프로그래밍 기초](https://codingalzi.github.io/pybook/intro.html)를
# 추천한다.
# 

# ## 파이썬 시작하기

# 다음 명령을 실행하면 `Hello, world` 문장이 화면에 출력된다.

# In[1]:


print("Hello, world!")


# 계속해서 아래 명령문도 실행해보자. 

# In[2]:


a = 3
b = 2 * a
type(b)


# :::{admonition} 코드 셀 실행
# :class: tip
# 
# 주피터 노트북의 코드 셀<font size="2">code cell</font>은
# IPython 콘솔처럼 명령문을 실행할 수 있으며 
# 이어지는 코드 셀은 이전에 실행된 코드 셀의
# 내용을 이어 받는다.
# 하지만 코드 셀은 콘솔과는 달리 여러 줄의 파이썬 명령문을 
# 마치 편집기로 작성된 하나의 코드 파일을 실행하는 것처럼
# 전체 명령문을 차례대로 실행할 수 있다.
# :::

# In[3]:


print(b)


# In[4]:


a * b 


# In[5]:


b = "hello"
type(b)


# In[6]:


b + b


# In[7]:


2 * b


# In[8]:


b * 2


# 변수를 선언할 때 변수의 자료형<font size="2">data type</font>을 
# 지정하지 않는다.
# 변수의 자료형을 지정하지 않기 때문에
# 변수가 가리키는 값을 다른 자료형의 값으로 변경할 수 있다.
# 예를 들어 변수 `b` 가 처음에는 정수 `6` 을 
# 가리켰다가 이후엔 문자열 `'hello'` 를 가리킨다.

# :::{admonition} 변수의 자료형
# :class: tip
# 
# C, C++, C#, 자바 등 다른 프로그래밍 언어와의 차이점 중에 하나다.
# 예를 들어, C 언어에서 변수 선언은 아래와 같이 변수의 자료형을 지정한다.
# 
# ```c
# int b = 6;
# ```
# 
# 따라서 파이썬과는 달리 아래와 같이 문자열 등 다른 자료형의 값을 가리키도
# 하는 것을 허용하지 않는다.
# 
# ```c
# b = "hello";
# ```
# :::

# 곱셈 기호 `*` 는 인자의 자료형에 따라 다른 연산자로 작동한다. 
# `3 * 6` 은 두 정수의 곱셈이지만
# `2 * 'hello'` 와 `2 * 'hello'` 는 문자열 `'hello'` 를 두 번 
# 이어붙인다.
# 덧셈 기호 `+` 도 사용되는 인자에 따라 다르게 작동한다.

# ## 기본 자료형

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
