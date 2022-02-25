#!/usr/bin/env python
# coding: utf-8

# # 명령문

# ## Assignment operator

# [Python library reference](<https//docs.python.org/reference/simple_stmts.html#assignment-statements>)
# says
# 
#     Assignment statements are used to (re)bind names to values and to
#     modify attributes or items of mutable objects.
# 
# In short, it works as follows (simple assignment)
# 
# 1. an expression on the right hand side is evaluated, the corresponding
# object is created/obtained
# 1. a **name** on the left hand side is assigned, or bound, to the
# r.h.s. object

# Things to note
# 
# * a single object can have several names bound to it
# 
# ```python
# In [1] a = [1, 2, 3]
# In [2] b = a
# In [3] a
# Out[3] [1, 2, 3]
# In [4] b
# Out[4] [1, 2, 3]
# In [5] a is b
# Out[5] True
# In [6] b[1] = 'hi!'
# In [7] a
# Out[7] [1, 'hi!', 3]
# ```

# * to change a list *in place*, use indexing/slices
# 
# ```python
# In [1] a = [1, 2, 3]
# In [3] a
# Out[3] [1, 2, 3]
# In [4] a = ['a', 'b', 'c'] # Creates another object.
# In [5] a
# Out[5] ['a', 'b', 'c']
# In [6] id(a)
# Out[6] 138641676
# In [7] a[] = [1, 2, 3] # Modifies object in place.
# In [8] a
# Out[8] [1, 2, 3]
# In [9] id(a)
# Out[9] 138641676 # Same as in Out[6], yours will differ...
# ```

# * the key concept here is **mutable vs. immutable**
#     * mutable objects can be changed in place
#     * immutable objects cannot be modified once created

# ## Control Flow

# Controls the order in which the code is executed.

# ### if/elif/else

# ```python
# >>> if 2**2 == 4:
# ...     print('Obvious!')
# ...
# Obvious!
# ```

# **Blocks are delimited by indentation**

# Type the following lines in your Python interpreter, and be careful
# to **respect the indentation depth**. The Ipython shell automatically
# increases the indentation depth after a colon ``:`` sign; to
# decrease the indentation depth, go four spaces to the left with the
# Backspace key. Press the Enter key twice to leave the logical block.

# ```python
# >>> a = 10
# 
# >>> if a == 1:
# ...     print(1)
# ... elif a == 2:
# ...     print(2)
# ... else:
# ...     print('A lot')
# A lot
# ```

# Indentation is compulsory in scripts as well. As an exercise, re-type the
# previous lines with the same indentation in a script ``condition.py``, and
# execute the script with ``run condition.py`` in Ipython.

# ### for/range

# Iterating with an index:
# 
# ```python
# >>> for i in range(4):
# ...     print(i)
# 0
# 1
# 2
# 3
# ```

# But most often, it is more readable to iterate over values:

# ```python
# >>> for word in ('cool', 'powerful', 'readable'):
# ...     print('Python is %s' % word)
# Python is cool
# Python is powerful
# Python is readable
# ```

# ### while/break/continue

# Typical C-style while loop (Mandelbrot problem):
# 
# ```python
# >>> z = 1 + 1j
# >>> while abs(z) < 100:
# ...     z = z**2 + 1
# >>> z
# (-134+352j)
# ```

# **More advanced features**
# 
# `break` out of enclosing for/while loop:
# 
# ```python
# >>> z = 1 + 1j
# 
# >>> while abs(z) < 100:
# ...     if z.imag == 0:
# ...         break
# ...     z = z**2 + 1
# ```

# `continue` the next iteration of a loop.:
# 
# ```python
# >>> a = [1, 0, 2, 4]
# >>> for element in a:
# ...     if element == 0:
# ...         continue
# ...     print(1. / element)
# 1.0
# 0.5
# 0.25
# ```

# ### Conditional Expressions

# `if <OBJECT>`
# 
# Evaluates to False:
# * any number equal to zero (`0`, `0.0`, `0+0`)
# * an empty container (list, tuple, set, dictionary, ...)
# * `False`, `None`
# 
# Evaluates to True:
# * everything else

# `a == b`
# 
# Tests equality, with logics:
# 
# ```python
# >>> 1 == 1.
# True
# ```

# `a is b`
# 
# Tests identity: both sides are the same object:
# 
# ```python
# >>> 1 is 1.
# False
# 
# >>> a = 1
# >>> b = 1
# >>> a is b
# True
# ```

# `a in b`
# 
# For any collection `b`: `b` contains `a` :
# 
# ```python
# >>> b = [1, 2, 3]
# >>> 2 in b
# True
# >>> 5 in b
# False
# ```
# 
# If `b` is a dictionary, this tests that `a` is a key of `b`.

# ### Advanced iteration

# **Iterate over any sequence**
# 
# You can iterate over any sequence (string, list, keys in a dictionary, lines in
# a file, ...):
# 
# ```python
# >>> vowels = 'aeiouy'
# 
# >>> for i in 'powerful':
# ...     if i in vowels:
# ...         print(i)
# o
# e
# u
# ```

# ```python
# >>> message = "Hello how are you?"
# >>> message.split() # returns a list
# ['Hello', 'how', 'are', 'you?']
# >>> for word in message.split():
# ...     print(word)
# ...
# Hello
# how
# are
# you?
# ```

# Few languages (in particular, languages for scientific computing) allow to
# loop over anything but integers/indices. With Python it is possible to
# loop exactly over the objects of interest without bothering with indices
# you often don't care about. This feature can often be used to make
# code more readable.

# **warning**: Not safe to modify the sequence you are iterating over.

# **Keeping track of enumeration number**
# 
# Common task is to iterate over a sequence while keeping track of the
# item number.

# * Could use while loop with a counter as above. Or a for loop:
# 
# ```python
# >>> words = ('cool', 'powerful', 'readable')
# >>> for i in range(0, len(words)):
# ...     print((i, words[i]))
# (0, 'cool')
# (1, 'powerful')
# (2, 'readable')
# ```

# * But, Python provides a built-in function - `enumerate` - for this:
# 
# ```python
# >>> for index, item in enumerate(words):
# ...     print((index, item))
# (0, 'cool')
# (1, 'powerful')
# (2, 'readable')
# ```

# **Looping over a dictionary**
# 
# Use **items**:
# 
# ```python
# >>> d = {'a': 1, 'b':1.2, 'c':1j}
# 
# >>> for key, val in sorted(d.items()):
# ...     print('Key: %s has value: %s' % (key, val))
# Key: a has value: 1
# Key: b has value: 1.2
# Key: c has value: 1j
# ```

# **note**
# 
# The ordering of a dictionary is random, thus we use :func:`sorted`
# which will sort on the keys.

# **Exercise**
# ref: `pi_wallis`
# 
# Compute the decimals of Pi using the Wallis formula:
# 
# $$
# \pi = 2 \prod_{i=1}^{\infty} \frac{4i^2}{4i^2 - 1}
# $$
# 
