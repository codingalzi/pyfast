#!/usr/bin/env python
# coding: utf-8

# # 파이썬 기초

# .. topic:: Python for scientific computing
# 
#     We introduce here the Python language. Only the bare minimum
#     necessary for getting started with Numpy and Scipy is addressed here.
#     To learn more about the language, consider going through the
#     excellent tutorial https://docs.python.org/tutorial. Dedicated books
#     are also available, such as `Dive into Python 3 <https://diveintopython3.net/>`__.

# .. tip::
# 
#   Python is a **programming language**, as are C, Fortran, BASIC, PHP,
#   etc. Some specific features of Python are as follows:
# 
#   * an *interpreted* (as opposed to *compiled*) language. Contrary to e.g.
#     C or Fortran, one does not compile Python code before executing it. In
#     addition, Python can be used **interactively**: many Python
#     interpreters are available, from which commands and scripts canㄴ be
#     executed.
# 
#   * a free software released under an **open-source** license: Python can
#     be used and distributed free of charge, even for building commercial
#     software.
# 
#   * **multi-platform**: Python is available for all major operating
#     systems, Windows, Linux/Unix, MacOS X, most likely your mobile phone
#     OS, etc.
# 
#   * a very readable language with clear non-verbose syntax
# 
#   * a language for which a large variety of high-quality packages are
#     available for various applications, from web frameworks to scientific
#     computing.
# 
#   * a language very easy to interface with other languages, in particular C
#     and C++.
# 
#   * Some other features of the language are illustrated just below. For
#     example, Python is an object-oriented language, with dynamic typing
#     (the same variable can contain objects of different types during the
#     course of a program).

#   See https://www.python.org/about/ for more information about
#   distinguishing features of Python.

# _____
# 
# .. toctree::
#     :maxdepth: 2
# 
#     first_steps.rst
#     basic_types.rst
#     control_flow.rst
#     functions.rst
#     reusing_code.rst
#     io.rst
#     standard_library.rst
#     exceptions.rst
#     oop.rst

# First steps
# -------------
# 
# 
# Start the **Ipython** shell (an enhanced interactive Python shell):
# 
# * by typing "ipython" from a Linux/Mac terminal, or from the Windows cmd shell,
# * **or** by starting the program from a menu, e.g. in the `Python(x,y)`_ or
#   `EPD`_ menu if you have installed one of these scientific-Python suites.
# * **or** by starting the program from a menu, e.g. the `Anaconda Navigator`_,
#   the `Python(x,y)`_ menu or the `EPD`_ menu if you have installed one of these
#   scientific-Python suites.
# 
# .. _`Python(x,y)`: https://python-xy.github.io/
# .. _`Anaconda Navigator`: https://anaconda.org/anaconda/anaconda-navigator
# .. _`EPD`: http://store.enthought.com/
# 
# .. tip::
# 
#     If you don't have Ipython installed on your computer, other Python
#     shells are available, such as the plain Python shell started by
#     typing "python" in a terminal, or the Idle interpreter. However, we
#     advise to use the Ipython shell because of its enhanced features,
#     especially for interactive scientific computing.
# 
# Once you have started the interpreter, type ::
# 
#     >>> print("Hello, world!")
#     Hello, world!
# 
# .. tip::
# 
#     The message "Hello, world!" is then displayed. You just executed your
#     first Python instruction, congratulations!
# 
# To get yourself started, type the following stack of instructions ::
# 
#     >>> a = 3
#     >>> b = 2*a
#     >>> type(b)     # doctest: +SKIP
#     <type 'int'>
#     >>> print(b)
#     6
#     >>> a*b 
#     18
#     >>> b = 'hello' 
#     >>> type(b)    # doctest: +SKIP
#     <type 'str'>
#     >>> b + b
#     'hellohello'
#     >>> 2*b
#     'hellohello'
# 
# .. We need to skip the call to 'type' because in Python3 is prints as
#    'type', but in Python2 as 'class'
# 
# .. tip::
# 
#   Two variables ``a`` and ``b`` have been defined above. Note that one does
#   not declare the type of a variable before assigning its value. In C,
#   conversely, one should write:
# 
#   .. sourcecode:: c
# 
#       int a = 3;
# 
#   In addition, the type of a variable may change, in the sense that at
#   one point in time it can be equal to a value of a certain type, and a
#   second point in time, it can be equal to a value of a different
#   type. `b` was first equal to an integer, but it became equal to a
#   string when it was assigned the value `'hello'`. Operations on
#   integers (``b=2*a``) are coded natively in Python, and so are some
#   operations on strings such as additions and multiplications, which
#   amount respectively to concatenation and repetition.
# 

# Basic types
# ============
# 
# Numerical types
# ----------------
# 
# .. tip::
# 
#     Python supports the following numerical, scalar types:
# 
# :Integer:
# 
#     >>> 1 + 1
#     2
#     >>> a = 4
#     >>> type(a)   # doctest: +SKIP
#     <type 'int'>
# 
# :Floats:
# 
#     >>> c = 2.1
#     >>> type(c)   # doctest: +SKIP
#     <type 'float'>
# 
# :Complex:
# 
#     >>> a = 1.5 + 0.5j
#     >>> a.real
#     1.5
#     >>> a.imag
#     0.5
#     >>> type(1. + 0j)   # doctest: +SKIP
#     <type 'complex'>
# 
# :Booleans:
# 
#     >>> 3 > 4
#     False
#     >>> test = (3 > 4)
#     >>> test
#     False
#     >>> type(test)      # doctest: +SKIP
#     <type 'bool'>
# 
# .. tip::
# 
#     A Python shell can therefore replace your pocket calculator, with the
#     basic arithmetic operations ``+``, ``-``, ``*``, ``/``, ``%`` (modulo)
#     natively implemented
# 
# ::
# 
#     >>> 7 * 3.
#     21.0
#     >>> 2**10
#     1024
#     >>> 8 % 3
#     2
# 
# Type conversion (casting)::
# 
#     >>> float(1)
#     1.0
# 
# .. warning:: Integer division
# 
#     In Python 2::
# 
#         >>> 3 / 2   # doctest: +SKIP
#         1
# 
#     In Python 3::
# 
#         >>> 3 / 2   # doctest: +SKIP
#         1.5
# 
#     **To be safe**: use floats::
# 
#         >>> 3 / 2.
#         1.5
# 
#         >>> a = 3
#         >>> b = 2
#         >>> a / b # In Python 2  # doctest: +SKIP
#         1
#         >>> a / float(b)
#         1.5
# 
#     **Future behavior**: to always get the behavior of Python3
# 
#         >>> from __future__ import division  # doctest: +SKIP
#         >>> 3 / 2  # doctest: +SKIP
#         1.5
# 
#     .. tip::
# 
#       If you explicitly want integer division use ``//``::
# 
#         >>> 3.0 // 2
#         1.0
# 
#       .. note::
# 
#         The behaviour of the division operator has changed in `Python 3
#         <http://python3porting.com/preparing.html#use-instead-of-when-dividing-integers>`_.
# 
# Containers
# ------------
# 
# .. tip::
# 
#     Python provides many efficient types of containers, in which
#     collections of objects can be stored.
# 
# Lists
# ~~~~~
# 
# .. tip::
# 
#     A list is an ordered collection of objects, that may have different
#     types. For example:
# 
# ::
# 
#     >>> colors = ['red', 'blue', 'green', 'black', 'white']
#     >>> type(colors)     # doctest: +SKIP
#     <type 'list'>
# 
# Indexing: accessing individual objects contained in the list::
# 
#     >>> colors[2]
#     'green'
# 
# Counting from the end with negative indices::
# 
#     >>> colors[-1]
#     'white'
#     >>> colors[-2]
#     'black'
# 
# .. warning::
# 
#     **Indexing starts at 0** (as in C), not at 1 (as in Fortran or Matlab)!
# 
# Slicing: obtaining sublists of regularly-spaced elements::
# 
#     >>> colors
#     ['red', 'blue', 'green', 'black', 'white']
#     >>> colors[2:4]
#     ['green', 'black']
# 
# .. Warning::
# 
#     Note that ``colors[start:stop]`` contains the elements with indices ``i``
#     such as  ``start<= i < stop`` (``i`` ranging from ``start`` to
#     ``stop-1``). Therefore, ``colors[start:stop]`` has ``(stop - start)`` elements.
# 
# **Slicing syntax**: ``colors[start:stop:stride]``
# 
# .. tip::
# 
#   All slicing parameters are optional::
# 
#     >>> colors
#     ['red', 'blue', 'green', 'black', 'white']
#     >>> colors[3:]
#     ['black', 'white']
#     >>> colors[:3]
#     ['red', 'blue', 'green']
#     >>> colors[::2]
#     ['red', 'green', 'white']
# 
# Lists are *mutable* objects and can be modified::
# 
#     >>> colors[0] = 'yellow'
#     >>> colors
#     ['yellow', 'blue', 'green', 'black', 'white']
#     >>> colors[2:4] = ['gray', 'purple']
#     >>> colors
#     ['yellow', 'blue', 'gray', 'purple', 'white']
# 
# .. Note::
# 
#    The elements of a list may have different types::
# 
#         >>> colors = [3, -200, 'hello']
#         >>> colors
#         [3, -200, 'hello']
#         >>> colors[1], colors[2]
#         (-200, 'hello')
# 
#    .. tip::
# 
#     For collections of numerical data that all have the same type, it
#     is often **more efficient** to use the ``array`` type provided by
#     the ``numpy`` module. A NumPy array is a chunk of memory
#     containing fixed-sized items.  With NumPy arrays, operations on
#     elements can be faster because elements are regularly spaced in
#     memory and more operations are performed through specialized C
#     functions instead of Python loops.
# 
# 
# .. tip::
# 
#     Python offers a large panel of functions to modify lists, or query
#     them. Here are a few examples; for more details, see
#     https://docs.python.org/tutorial/datastructures.html#more-on-lists
# 
# Add and remove elements::
# 
#     >>> colors = ['red', 'blue', 'green', 'black', 'white']
#     >>> colors.append('pink')
#     >>> colors
#     ['red', 'blue', 'green', 'black', 'white', 'pink']
#     >>> colors.pop() # removes and returns the last item
#     'pink'
#     >>> colors
#     ['red', 'blue', 'green', 'black', 'white']
#     >>> colors.extend(['pink', 'purple']) # extend colors, in-place
#     >>> colors
#     ['red', 'blue', 'green', 'black', 'white', 'pink', 'purple']
#     >>> colors = colors[:-2]
#     >>> colors
#     ['red', 'blue', 'green', 'black', 'white']
# 
# Reverse::
# 
#     >>> rcolors = colors[::-1]
#     >>> rcolors
#     ['white', 'black', 'green', 'blue', 'red']
#     >>> rcolors2 = list(colors) # new object that is a copy of colors in a different memory area
#     >>> rcolors2
#     ['red', 'blue', 'green', 'black', 'white']
#     >>> rcolors2.reverse() # in-place; reversing rcolors2 does not affect colors
#     >>> rcolors2
#     ['white', 'black', 'green', 'blue', 'red']
# 
# Concatenate and repeat lists::
# 
#     >>> rcolors + colors
#     ['white', 'black', 'green', 'blue', 'red', 'red', 'blue', 'green', 'black', 'white']
#     >>> rcolors * 2
#     ['white', 'black', 'green', 'blue', 'red', 'white', 'black', 'green', 'blue', 'red']
# 
# 
# .. tip::
# 
#   Sort::
# 
#     >>> sorted(rcolors) # new object
#     ['black', 'blue', 'green', 'red', 'white']
#     >>> rcolors
#     ['white', 'black', 'green', 'blue', 'red']
#     >>> rcolors.sort()  # in-place
#     >>> rcolors
#     ['black', 'blue', 'green', 'red', 'white']
# 
# .. topic:: **Methods and Object-Oriented Programming**
# 
#     The notation ``rcolors.method()`` (e.g. ``rcolors.append(3)`` and ``colors.pop()``) is our
#     first example of object-oriented programming (OOP). Being a ``list``, the
#     object `rcolors` owns the *method* `function` that is called using the notation
#     **.**. No further knowledge of OOP than understanding the notation **.** is
#     necessary for going through this tutorial.
# 
# 
# .. topic:: **Discovering methods:**
# 
#     Reminder: in Ipython: tab-completion (press tab)
# 
#     .. sourcecode:: ipython
# 
#         In [28]: rcolors.<TAB>
#         rcolors.append   rcolors.index    rcolors.remove   
#         rcolors.count    rcolors.insert   rcolors.reverse  
#         rcolors.extend   rcolors.pop      rcolors.sort    
# 
# Strings
# ~~~~~~~
# 
# Different string syntaxes (simple, double or triple quotes)::
# 
#     s = 'Hello, how are you?'
#     s = "Hi, what's up"
#     s = '''Hello,
#            how are you'''         # tripling the quotes allows the
#                                   # string to span more than one line
#     s = """Hi,
#     what's up?"""
# 
# .. sourcecode:: ipython
# 
#     In [1]: 'Hi, what's up?'
#     ------------------------------------------------------------
#        File "<ipython console>", line 1
#         'Hi, what's up?'
#                ^
#     SyntaxError: invalid syntax
# 
# This syntax error can be avoided by enclosing the string in double quotes
# instead of single quotes. Alternatively, one can prepend a backslash to the
# second single quote. Other uses of the backslash are, e.g., the newline character
# ``\n`` and the tab character ``\t``.
# 
# .. tip::
# 
#     Strings are collections like lists. Hence they can be indexed and
#     sliced, using the same syntax and rules.
# 
# Indexing::
# 
#     >>> a = "hello"
#     >>> a[0]
#     'h'
#     >>> a[1]
#     'e'
#     >>> a[-1]
#     'o'
# 
# .. tip::
# 
#     (Remember that negative indices correspond to counting from the right
#     end.)
# 
# Slicing::
# 
# 
#     >>> a = "hello, world!"
#     >>> a[3:6] # 3rd to 6th (excluded) elements: elements 3, 4, 5
#     'lo,'
#     >>> a[2:10:2] # Syntax: a[start:stop:step]
#     'lo o'
#     >>> a[::3] # every three characters, from beginning to end
#     'hl r!'
# 
# .. tip::
#    
#     Accents and special characters can also be handled as in Python 3
#     strings consist of Unicode characters.
# 
# 
# A string is an **immutable object** and it is not possible to modify its
# contents. One may however create new strings from the original one.
# 
# .. sourcecode:: ipython
# 
#     In [53]: a = "hello, world!"
#     In [54]: a[2] = 'z'
#     ---------------------------------------------------------------------------
#     Traceback (most recent call last):
#        File "<stdin>", line 1, in <module>
#     TypeError: 'str' object does not support item assignment
# 
#     In [55]: a.replace('l', 'z', 1)
#     Out[55]: 'hezlo, world!'
#     In [56]: a.replace('l', 'z')
#     Out[56]: 'hezzo, worzd!'
# 
# .. tip::
# 
#     Strings have many useful methods, such as ``a.replace`` as seen
#     above. Remember the ``a.`` object-oriented notation and use tab
#     completion or ``help(str)`` to search for new methods.
# 
# .. seealso::
# 
#     Python offers advanced possibilities for manipulating strings,
#     looking for patterns or formatting. The interested reader is referred to
#     https://docs.python.org/library/stdtypes.html#string-methods and
#     https://docs.python.org/3/library/string.html#format-string-syntax
# 
# String formatting::
# 
#     >>> 'An integer: %i; a float: %f; another string: %s' % (1, 0.1, 'string') # with more values use tuple after %
#     'An integer: 1; a float: 0.100000; another string: string'
# 
#     >>> i = 102
#     >>> filename = 'processing_of_dataset_%d.txt' % i   # no need for tuples with just one value after %
#     >>> filename
#     'processing_of_dataset_102.txt'
# 
# Dictionaries
# ~~~~~~~~~~~~~
# 
# .. tip::
# 
#     A dictionary is basically an efficient table that **maps keys to
#     values**. It is an **unordered** container
# 
# ::
# 
#     >>> tel = {'emmanuelle': 5752, 'sebastian': 5578}
#     >>> tel['francis'] = 5915
#     >>> tel     # doctest: +SKIP
#     {'sebastian': 5578, 'francis': 5915, 'emmanuelle': 5752}
#     >>> tel['sebastian']
#     5578
#     >>> tel.keys()   # doctest: +SKIP
#     ['sebastian', 'francis', 'emmanuelle']
#     >>> tel.values()   # doctest: +SKIP
#     [5578, 5915, 5752]
#     >>> 'francis' in tel
#     True
# 
# .. tip::
# 
#   It can be used to conveniently store and retrieve values
#   associated with a name (a string for a date, a name, etc.). See
#   https://docs.python.org/tutorial/datastructures.html#dictionaries
#   for more information.
# 
#   A dictionary can have keys (resp. values) with different types::
# 
#     >>> d = {'a':1, 'b':2, 3:'hello'}
#     >>> d       # doctest: +SKIP
#     {'a': 1, 3: 'hello', 'b': 2}
# 
# More container types
# ~~~~~~~~~~~~~~~~~~~~
# 
# **Tuples**
# 
# Tuples are basically immutable lists. The elements of a tuple are written
# between parentheses, or just separated by commas::
# 
#     >>> t = 12345, 54321, 'hello!'
#     >>> t[0]
#     12345
#     >>> t
#     (12345, 54321, 'hello!')
#     >>> u = (0, 2)
# 
# **Sets:** unordered, unique items::
# 
#     >>> s = set(('a', 'b', 'c', 'a'))
#     >>> s    # doctest: +SKIP
#     set(['a', 'c', 'b'])
#     >>> s.difference(('a', 'b'))    # doctest: +SKIP
#     set(['c'])
# 
# Assignment operator
# -------------------
# 
# .. tip::
# 
#  `Python library reference
#  <https://docs.python.org/reference/simple_stmts.html#assignment-statements>`_
#  says:
# 
#   Assignment statements are used to (re)bind names to values and to
#   modify attributes or items of mutable objects.
# 
#  In short, it works as follows (simple assignment):
# 
#  #. an expression on the right hand side is evaluated, the corresponding
#     object is created/obtained
#  #. a **name** on the left hand side is assigned, or bound, to the
#     r.h.s. object
# 
# Things to note:
# 
# * a single object can have several names bound to it:
# 
#     .. sourcecode:: ipython
# 
#         In [1]: a = [1, 2, 3]
#         In [2]: b = a
#         In [3]: a
#         Out[3]: [1, 2, 3]
#         In [4]: b
#         Out[4]: [1, 2, 3]
#         In [5]: a is b
#         Out[5]: True
#         In [6]: b[1] = 'hi!'
#         In [7]: a
#         Out[7]: [1, 'hi!', 3]
# 
# * to change a list *in place*, use indexing/slices:
# 
#     .. sourcecode:: ipython
# 
#         In [1]: a = [1, 2, 3]
#         In [3]: a
#         Out[3]: [1, 2, 3]
#         In [4]: a = ['a', 'b', 'c'] # Creates another object.
#         In [5]: a
#         Out[5]: ['a', 'b', 'c']
#         In [6]: id(a)
#         Out[6]: 138641676
#         In [7]: a[:] = [1, 2, 3] # Modifies object in place.
#         In [8]: a
#         Out[8]: [1, 2, 3]
#         In [9]: id(a)
#         Out[9]: 138641676 # Same as in Out[6], yours will differ...
# 
# * the key concept here is **mutable vs. immutable**
# 
#     * mutable objects can be changed in place
#     * immutable objects cannot be modified once created
# 
# .. seealso:: A very good and detailed explanation of the above issues can
#    be found in David M. Beazley's article `Types and Objects in Python
#    <http://www.informit.com/articles/article.aspx?p=453682>`_.
# 

# Control Flow
# ============
# 
# Controls the order in which the code is executed.
# 
# if/elif/else
# ------------
# 
# .. sourcecode:: python
# 
#     >>> if 2**2 == 4:
#     ...     print('Obvious!')
#     ...
#     Obvious!
# 
# 
# **Blocks are delimited by indentation**
# 
# .. tip::
#    
#     Type the following lines in your Python interpreter, and be careful
#     to **respect the indentation depth**. The Ipython shell automatically
#     increases the indentation depth after a colon ``:`` sign; to
#     decrease the indentation depth, go four spaces to the left with the
#     Backspace key. Press the Enter key twice to leave the logical block.
# 
# .. sourcecode:: python
# 
#     >>> a = 10
# 
#     >>> if a == 1:
#     ...     print(1)
#     ... elif a == 2:
#     ...     print(2)
#     ... else:
#     ...     print('A lot')
#     A lot
# 
# Indentation is compulsory in scripts as well. As an exercise, re-type the
# previous lines with the same indentation in a script ``condition.py``, and
# execute the script with ``run condition.py`` in Ipython.
# 
# for/range
# ----------
# 
# Iterating with an index::
# 
#     >>> for i in range(4):
#     ...     print(i)
#     0
#     1
#     2
#     3
# 
# But most often, it is more readable to iterate over values::
# 
#     >>> for word in ('cool', 'powerful', 'readable'):
#     ...     print('Python is %s' % word)
#     Python is cool
#     Python is powerful
#     Python is readable
# 
# 
# while/break/continue
# ---------------------
# 
# Typical C-style while loop (Mandelbrot problem)::
# 
#     >>> z = 1 + 1j
#     >>> while abs(z) < 100:
#     ...     z = z**2 + 1
#     >>> z
#     (-134+352j)
# 
# **More advanced features**
# 
# ``break`` out of enclosing for/while loop::
# 
#     >>> z = 1 + 1j
# 
#     >>> while abs(z) < 100:
#     ...     if z.imag == 0:
#     ...         break
#     ...     z = z**2 + 1
# 
# 
# ``continue`` the next iteration of a loop.::
# 
#     >>> a = [1, 0, 2, 4]
#     >>> for element in a:
#     ...     if element == 0:
#     ...         continue
#     ...     print(1. / element)
#     1.0
#     0.5
#     0.25
# 
# 
# 
# Conditional Expressions
# -----------------------
# 
# :``if <OBJECT>``:
# 
#   Evaluates to False:
#     * any number equal to zero (0, 0.0, 0+0j)
#     * an empty container (list, tuple, set, dictionary, ...)
#     * ``False``, ``None``
# 
#   Evaluates to True:
#     * everything else
# 
# :``a == b``:
# 
#   Tests equality, with logics::
# 
#     >>> 1 == 1.
#     True
# 
# :``a is b``:
# 
#   Tests identity: both sides are the same object::
# 
#     >>> 1 is 1.
#     False
# 
#     >>> a = 1
#     >>> b = 1
#     >>> a is b
#     True
# 
# :``a in b``:
# 
#   For any collection ``b``: ``b`` contains ``a`` ::
# 
#     >>> b = [1, 2, 3]
#     >>> 2 in b
#     True
#     >>> 5 in b
#     False
# 
# 
#   If ``b`` is a dictionary, this tests that ``a`` is a key of ``b``.
# 
# Advanced iteration
# -------------------------
# 
# Iterate over any *sequence*
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# You can iterate over any sequence (string, list, keys in a dictionary, lines in
# a file, ...)::
# 
#     >>> vowels = 'aeiouy'
# 
#     >>> for i in 'powerful':
#     ...     if i in vowels:
#     ...         print(i)
#     o
#     e
#     u
# 
# ::
# 
#     >>> message = "Hello how are you?"
#     >>> message.split() # returns a list
#     ['Hello', 'how', 'are', 'you?']
#     >>> for word in message.split():
#     ...     print(word)
#     ...
#     Hello
#     how
#     are
#     you?
# 
# .. tip::
# 
#     Few languages (in particular, languages for scientific computing) allow to
#     loop over anything but integers/indices. With Python it is possible to
#     loop exactly over the objects of interest without bothering with indices
#     you often don't care about. This feature can often be used to make
#     code more readable.
# 
# 
# .. warning:: Not safe to modify the sequence you are iterating over.
# 
# Keeping track of enumeration number
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# Common task is to iterate over a sequence while keeping track of the
# item number.
# 
# * Could use while loop with a counter as above. Or a for loop::
# 
#     >>> words = ('cool', 'powerful', 'readable')
#     >>> for i in range(0, len(words)):
#     ...     print((i, words[i]))
#     (0, 'cool')
#     (1, 'powerful')
#     (2, 'readable')
# 
# * But, Python provides a built-in function - ``enumerate`` - for this::
# 
#     >>> for index, item in enumerate(words):
#     ...     print((index, item))
#     (0, 'cool')
#     (1, 'powerful')
#     (2, 'readable')
# 
# 
# 
# Looping over a dictionary
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# Use **items**::
# 
#     >>> d = {'a': 1, 'b':1.2, 'c':1j}
# 
#     >>> for key, val in sorted(d.items()):
#     ...     print('Key: %s has value: %s' % (key, val))
#     Key: a has value: 1
#     Key: b has value: 1.2
#     Key: c has value: 1j
# 
# .. note::
# 
#    The ordering of a dictionary is random, thus we use :func:`sorted`
#    which will sort on the keys.
# 
# List Comprehensions
# -------------------
# 
# Instead of creating a list by means of a loop, one can make use
# of a list comprehension with a rather self-explaining syntax.
# 
# ::
# 
#     >>> [i**2 for i in range(4)]
#     [0, 1, 4, 9]
# 
# _____
# 
# 
# .. topic:: Exercise
#     :class: green
# 
#     Compute the decimals of Pi using the Wallis formula:
# 
#     .. math::
#         \pi = 2 \prod_{i=1}^{\infty} \frac{4i^2}{4i^2 - 1}
# 
# .. :ref:`pi_wallis`
# 

# Defining functions
# =====================
# 
# Function definition
# -------------------
# 
# .. sourcecode:: ipython
# 
#     In [56]: def test():
#        ....:     print('in test function')
#        ....:
#        ....:
# 
#     In [57]: test()
#     in test function
# 
# .. Warning::
# 
#     Function blocks must be indented as other control-flow blocks.
# 
# Return statement
# ----------------
# 
# Functions can *optionally* return values.
# 
# .. sourcecode:: ipython
# 
#     In [6]: def disk_area(radius):
#        ...:     return 3.14 * radius * radius
#        ...:
# 
#     In [8]: disk_area(1.5)
#     Out[8]: 7.0649999999999995
# 
# .. Note:: By default, functions return ``None``.
# 
# .. Note:: Note the syntax to define a function:
# 
#     * the ``def`` keyword;
# 
#     * is followed by the function's **name**, then
# 
#     * the arguments of the function are given between parentheses followed
#       by a colon.
# 
#     * the function body;
# 
#     * and ``return object`` for optionally returning values.
# 
# 
# Parameters
# ----------
# 
# Mandatory parameters (positional arguments)
# 
# .. sourcecode:: ipython
# 
#     In [81]: def double_it(x):
#        ....:     return x * 2
#        ....:
# 
#     In [82]: double_it(3)
#     Out[82]: 6
# 
#     In [83]: double_it()
#     ---------------------------------------------------------------------------
#     Traceback (most recent call last):
#       File "<stdin>", line 1, in <module>
#     TypeError: double_it() takes exactly 1 argument (0 given)
# 
# Optional parameters (keyword or named arguments)
# 
# .. sourcecode:: ipython
# 
#     In [84]: def double_it(x=2):
#        ....:     return x * 2
#        ....:
# 
#     In [85]: double_it()
#     Out[85]: 4
# 
#     In [86]: double_it(3)
#     Out[86]: 6
# 
# Keyword arguments allow you to specify *default values*.
# 
# .. warning::
# 
#    Default values are evaluated when the function is defined, not when
#    it is called. This can be problematic when using mutable types (e.g.
#    dictionary or list) and modifying them in the function body, since the
#    modifications will be persistent across invocations of the function.
# 
#    Using an immutable type in a keyword argument:
# 
#    .. sourcecode:: ipython
# 
#        In [124]: bigx = 10
# 
#        In [125]: def double_it(x=bigx):
#           .....:     return x * 2
#           .....:
# 
#        In [126]: bigx = 1e9  # Now really big
# 
#        In [128]: double_it()
#        Out[128]: 20
# 
#    Using an mutable type in a keyword argument (and modifying it inside the
#    function body):
# 
#    .. sourcecode:: ipython
# 
#        In [2]: def add_to_dict(args={'a': 1, 'b': 2}):
#           ...:     for i in args.keys():
#           ...:         args[i] += 1
#           ...:     print(args)
#           ...:
# 
#        In [3]: add_to_dict
#        Out[3]: <function __main__.add_to_dict>
# 
#        In [4]: add_to_dict()
#        {'a': 2, 'b': 3}
# 
#        In [5]: add_to_dict()
#        {'a': 3, 'b': 4}
# 
#        In [6]: add_to_dict()
#        {'a': 4, 'b': 5}
# 
# .. tip::
# 
#   More involved example implementing python's slicing:
# 
#   .. sourcecode:: ipython
# 
#     In [98]: def slicer(seq, start=None, stop=None, step=None):
#        ....:     """Implement basic python slicing."""
#        ....:     return seq[start:stop:step]
#        ....:
# 
#     In [101]: rhyme = 'one fish, two fish, red fish, blue fish'.split()
# 
#     In [102]: rhyme
#     Out[102]: ['one', 'fish,', 'two', 'fish,', 'red', 'fish,', 'blue', 'fish']
# 
#     In [103]: slicer(rhyme)
#     Out[103]: ['one', 'fish,', 'two', 'fish,', 'red', 'fish,', 'blue', 'fish']
# 
#     In [104]: slicer(rhyme, step=2)
#     Out[104]: ['one', 'two', 'red', 'blue']
# 
#     In [105]: slicer(rhyme, 1, step=2)
#     Out[105]: ['fish,', 'fish,', 'fish,', 'fish']
# 
#     In [106]: slicer(rhyme, start=1, stop=4, step=2)
#     Out[106]: ['fish,', 'fish,']
# 
#   The order of the keyword arguments does not matter:
# 
#   .. sourcecode:: ipython
# 
#     In [107]: slicer(rhyme, step=2, start=1, stop=4)
#     Out[107]: ['fish,', 'fish,']
# 
#   but it is good practice to use the same ordering as the function's
#   definition.
# 
# *Keyword arguments* are a very convenient feature for defining functions
# with a variable number of arguments, especially when default values are
# to be used in most calls to the function.
# 
# Passing by value
# ----------------
# 
# .. tip::
# 
#     Can you modify the value of a variable inside a function? Most languages
#     (C, Java, ...) distinguish "passing by value" and "passing by reference".
#     In Python, such a distinction is somewhat artificial, and it is a bit
#     subtle whether your variables are going to be modified or not.
#     Fortunately, there exist clear rules.
# 
#     Parameters to functions are references to objects, which are passed by
#     value. When you pass a variable to a function, python passes the
#     reference to the object to which the variable refers (the **value**).
#     Not the variable itself.
# 
# If the **value** passed in a function is immutable, the function does not
# modify the caller's variable.  If the **value** is mutable, the function
# may modify the caller's variable in-place::
# 
#     >>> def try_to_modify(x, y, z):
#     ...     x = 23
#     ...     y.append(42)
#     ...     z = [99] # new reference
#     ...     print(x)
#     ...     print(y)
#     ...     print(z)
#     ...
#     >>> a = 77    # immutable variable
#     >>> b = [99]  # mutable variable
#     >>> c = [28]
#     >>> try_to_modify(a, b, c)
#     23
#     [99, 42]
#     [99]
#     >>> print(a)
#     77
#     >>> print(b)
#     [99, 42]
#     >>> print(c)
#     [28]
# 
# 
# 
# Functions have a local variable table called a *local namespace*.
# 
# The variable ``x`` only exists within the function ``try_to_modify``.
# 
# 
# Global variables
# ----------------
# 
# Variables declared outside the function can be referenced within the
# function:
# 
# .. sourcecode:: ipython
# 
#     In [114]: x = 5
# 
#     In [115]: def addx(y):
#        .....:     return x + y
#        .....:
# 
#     In [116]: addx(10)
#     Out[116]: 15
# 
# But these "global" variables cannot be modified within the function,
# unless declared **global** in the function.
# 
# This doesn't work:
# 
# .. sourcecode:: ipython
# 
#     In [117]: def setx(y):
#        .....:     x = y
#        .....:     print('x is %d' % x)
#        .....:
#        .....:
# 
#     In [118]: setx(10)
#     x is 10
# 
#     In [120]: x
#     Out[120]: 5
# 
# This works:
# 
# .. sourcecode:: ipython
# 
#     In [121]: def setx(y):
#        .....:     global x
#        .....:     x = y
#        .....:     print('x is %d' % x)
#        .....:
#        .....:
# 
#     In [122]: setx(10)
#     x is 10
# 
#     In [123]: x
#     Out[123]: 10
# 
# 
# Variable number of parameters
# -----------------------------
# Special forms of parameters:
#   * ``*args``: any number of positional arguments packed into a tuple
#   * ``**kwargs``: any number of keyword arguments packed into a dictionary
# 
# .. sourcecode:: ipython
# 
#     In [35]: def variable_args(*args, **kwargs):
#        ....:     print('args is', args)
#        ....:     print('kwargs is', kwargs)
#        ....:
# 
#     In [36]: variable_args('one', 'two', x=1, y=2, z=3)
#     args is ('one', 'two')
#     kwargs is {'x': 1, 'y': 2, 'z': 3}
# 
# 
# Docstrings
# ----------
# 
# Documentation about what the function does and its parameters.  General
# convention:
# 
# .. sourcecode:: ipython
# 
#     In [67]: def funcname(params):
#        ....:     """Concise one-line sentence describing the function.
#        ....:
#        ....:     Extended summary which can contain multiple paragraphs.
#        ....:     """
#        ....:     # function body
#        ....:     pass
#        ....:
# 
#     In [68]: funcname?
#     Type:           function
#     Base Class:     type 'function'>
#     String Form:    <function funcname at 0xeaa0f0>
#     Namespace:      Interactive
#     File:           <ipython console>
#     Definition:     funcname(params)
#     Docstring:
#         Concise one-line sentence describing the function.
# 
#         Extended summary which can contain multiple paragraphs.
# 
# .. Note:: **Docstring guidelines**
# 
# 
#     For the sake of standardization, the `Docstring
#     Conventions <https://www.python.org/dev/peps/pep-0257>`_ webpage
#     documents the semantics and conventions associated with Python
#     docstrings.
# 
#     Also, the Numpy and Scipy modules have defined a precise standard
#     for documenting scientific functions, that you may want to follow for
#     your own functions, with a ``Parameters`` section, an ``Examples``
#     section, etc. See
#     https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
# 
# Functions are objects
# ---------------------
# Functions are first-class objects, which means they can be:
#   * assigned to a variable
#   * an item in a list (or any collection)
#   * passed as an argument to another function.
# 
# .. sourcecode:: ipython
# 
#     In [38]: va = variable_args
# 
#     In [39]: va('three', x=1, y=2)
#     args is ('three',)
#     kwargs is {'x': 1, 'y': 2}
# 
# 
# Methods
# -------
# 
# Methods are functions attached to objects.  You've seen these in our
# examples on *lists*, *dictionaries*, *strings*, etc...
# 
# 
# Exercises
# ---------
# 
# .. topic:: Exercise: Fibonacci sequence
#     :class: green
# 
#     Write a function that displays the ``n`` first terms of the Fibonacci
#     sequence, defined by:
# 
#     .. math::
#         \left\{
#             \begin{array}{ll}
#                 U_{0} = 0 \\
#                 U_{1} = 1 \\
#                 U_{n+2} = U_{n+1} + U_{n}
#             \end{array}
#         \right.
# 
# .. :ref:`fibonacci`
# 
# .. topic:: Exercise: Quicksort
#     :class: green
# 
#     Implement the quicksort algorithm, as defined by wikipedia
# 
# .. parsed-literal::
# 
#     function quicksort(array)
#         var list less, greater
#         if length(array) < 2
#             return array
#         select and remove a pivot value pivot from array
#         for each x in array
#             if x < pivot + 1 then append x to less
#             else append x to greater
#         return concatenate(quicksort(less), pivot, quicksort(greater))
# 
# .. :ref:`quick_sort`
# 

# Reusing code: scripts and modules
# =================================
# 
# For now, we have typed all instructions in the interpreter. For longer
# sets of instructions we need to change track and write the code in text
# files (using a text editor), that we will call either *scripts* or
# *modules*. Use your favorite text editor (provided it offers syntax
# highlighting for Python), or the editor that comes with the Scientific
# Python Suite you may be using.
# 
# Scripts
# -------
# 
# .. tip::
# 
#     Let us first write a *script*, that is a file with a sequence of
#     instructions that are executed each time the script is called.
#     Instructions may be e.g. copied-and-pasted from the interpreter (but
#     take care to respect indentation rules!).
# 
# The extension for Python files is ``.py``. Write or copy-and-paste the
# following lines in a file called ``test.py`` ::
# 
#     message = "Hello how are you?"
#     for word in message.split():
#         print(word)
# 
# .. tip::
# 
#     Let us now execute the script interactively, that is inside the
#     Ipython interpreter. This is maybe the most common use of scripts in
#     scientific computing.
# 
# .. note::
# 
#     in Ipython, the syntax to execute a script is ``%run script.py``. For
#     example,
# 
# .. sourcecode:: ipython
# 
#     In [1]: %run test.py
#     Hello
#     how
#     are
#     you?
# 
#     In [2]: message
#     Out[2]: 'Hello how are you?'
# 
# 
# The script has been executed. Moreover the variables defined in the
# script (such as ``message``) are now available inside the interpreter's
# namespace.
# 
# .. tip::
# 
#     Other interpreters also offer the possibility to execute scripts
#     (e.g., ``execfile`` in the plain Python interpreter, etc.).
# 
# It is also possible In order to execute this script as a *standalone
# program*, by executing the script inside a shell terminal (Linux/Mac
# console or cmd Windows console). For example, if we are in the same
# directory as the test.py file, we can execute this in a console:
# 
# .. sourcecode:: bash
# 
#     $ python test.py
#     Hello
#     how
#     are
#     you?
# 
# .. tip::
# 
#     Standalone scripts may also take command-line arguments
# 
#     In ``file.py``::
# 
#         import sys
#         print(sys.argv)
# 
#     .. sourcecode:: bash
# 
#         $ python file.py test arguments
#         ['file.py', 'test', 'arguments']
# 
#     .. warning::
# 
#         Don't implement option parsing yourself. Use a dedicated module such as
#         :mod:`argparse`.
# 
# 
# Importing objects from modules
# ------------------------------
# 
# .. sourcecode:: ipython
# 
#     In [1]: import os
# 
#     In [2]: os
#     Out[2]: <module 'os' from '/usr/lib/python2.6/os.pyc'>
# 
#     In [3]: os.listdir('.')
#     Out[3]:
#     ['conf.py',
#      'basic_types.rst',
#      'control_flow.rst',
#      'functions.rst',
#      'python_language.rst',
#      'reusing.rst',
#      'file_io.rst',
#      'exceptions.rst',
#      'workflow.rst',
#      'index.rst']
# 
# And also:
# 
# .. sourcecode:: ipython
# 
#     In [4]: from os import listdir
# 
# Importing shorthands:
# 
# .. sourcecode:: ipython
# 
#     In [5]: import numpy as np
# 
# .. warning::
# 
#     ::
# 
#         from os import *
# 
#     This is called the *star import* and please, **Do not use it**
# 
#     * Makes the code harder to read and understand: where do symbols come
#       from?
# 
#     * Makes it impossible to guess the functionality by the context and
#       the name (hint: `os.name` is the name of the OS), and to profit
#       usefully from tab completion.
# 
#     * Restricts the variable names you can use: `os.name` might override
#       `name`, or vise-versa.
# 
#     * Creates possible name clashes between modules.
# 
#     * Makes the code impossible to statically check for undefined
#       symbols.
# 
# .. tip::
# 
#   Modules are thus a good way to organize code in a hierarchical way. Actually,
#   all the scientific computing tools we are going to use are modules::
# 
#     >>> import numpy as np # data arrays
#     >>> np.linspace(0, 10, 6)
#     array([  0.,   2.,   4.,   6.,   8.,  10.])
#     >>> import scipy # scientific computing
# 
# 
# Creating modules
# -----------------
# 
# .. tip::
# 
#     If we want to write larger and better organized programs (compared to
#     simple scripts), where some objects are defined, (variables,
#     functions, classes) and that we want to reuse several times, we have
#     to create our own *modules*.
# 
# Let us create a module ``demo`` contained in the file ``demo.py``:
# 
#   .. literalinclude:: demo.py
# 
# .. tip::
# 
#     In this file, we defined two functions ``print_a`` and ``print_b``. Suppose
#     we want to call the ``print_a`` function from the interpreter. We could
#     execute the file as a script, but since we just want to have access to
#     the function ``print_a``, we are rather going to **import it as a module**.
#     The syntax is as follows.
# 
# 
# .. sourcecode:: ipython
# 
#     In [1]: import demo
# 
# 
#     In [2]: demo.print_a()
#     a
# 
#     In [3]: demo.print_b()
#     b
# 
# Importing the module gives access to its objects, using the
# ``module.object`` syntax. Don't forget to put the module's name before the
# object's name, otherwise Python won't recognize the instruction.
# 
# 
# Introspection
# 
# .. sourcecode:: ipython
# 
#     In [4]: demo?
#     Type:               module
#     Base Class: <type 'module'>
#     String Form:        <module 'demo' from 'demo.py'>
#     Namespace:  Interactive
#     File:               /home/varoquau/Projects/Python_talks/scipy_2009_tutorial/source/demo.py
#     Docstring:
#         A demo module.
# 
# 
#     In [5]: who
#     demo
# 
#     In [6]: whos
#     Variable   Type      Data/Info
#     ------------------------------
#     demo       module    <module 'demo' from 'demo.py'>
# 
#     In [7]: dir(demo)
#     Out[7]:
#     ['__builtins__',
#     '__doc__',
#     '__file__',
#     '__name__',
#     '__package__',
#     'c',
#     'd',
#     'print_a',
#     'print_b']
# 
# 
#     In [8]: demo.<TAB>
#     demo.c        demo.print_a  demo.py       
#     demo.d        demo.print_b  demo.pyc      
# 
# 
# Importing objects from modules into the main namespace
# 
# .. sourcecode:: ipython
# 
#     In [9]: from demo import print_a, print_b
# 
#     In [10]: whos
#     Variable   Type        Data/Info
#     --------------------------------
#     demo       module      <module 'demo' from 'demo.py'>
#     print_a    function    <function print_a at 0xb7421534>
#     print_b    function    <function print_b at 0xb74214c4>
# 
#     In [11]: print_a()
#     a
# 
# .. warning::
# 
#     **Module caching**
# 
#      Modules are cached: if you modify ``demo.py`` and re-import it in the
#      old session, you will get the old one.
# 
#     Solution:
# 
#      .. sourcecode :: ipython
# 
#         In [10]: reload(demo)
# 
#     In Python3 instead ``reload`` is not builtin, so you have to import the ``importlib`` module first and then do:
#     
#      .. sourcecode :: ipython
# 
#         In [10]: importlib.reload(demo)
# 
# '__main__' and module loading
# ------------------------------
# 
# .. tip::
# 
#     Sometimes we want code to be executed when a module is
#     run directly, but not when it is imported by another module.
#     ``if __name__ == '__main__'`` allows us to check whether the
#     module is being run directly.
# 
# File ``demo2.py``:
# 
#   .. literalinclude:: demo2.py
# 
# Importing it:
# 
# .. sourcecode:: ipython
# 
#     In [11]: import demo2
#     b
# 
#     In [12]: import demo2
# 
# Running it:
# 
# .. sourcecode:: ipython
# 
#     In [13]: %run demo2
#     b
#     a
# 
# 
# Scripts or modules? How to organize your code
# ---------------------------------------------
# 
# .. Note:: Rule of thumb
# 
#     * Sets of instructions that are called several times should be
#       written inside **functions** for better code reusability.
# 
#     * Functions (or other bits of code) that are called from several
#       scripts should be written inside a **module**, so that only the
#       module is imported in the different scripts (do not copy-and-paste
#       your functions in the different scripts!).
# 
# How modules are found and imported
# ..................................
# 
# 
# When the ``import mymodule`` statement is executed, the module ``mymodule``
# is searched in a given list of directories. This list includes a list
# of installation-dependent default path (e.g., ``/usr/lib/python``) as
# well as the list of directories specified by the environment variable
# ``PYTHONPATH``.
# 
# The list of directories searched by Python is given by the ``sys.path``
# variable
# 
# .. sourcecode:: ipython
# 
#     In [1]: import sys
# 
#     In [2]: sys.path
#     Out[2]: 
#     ['',
#      '/home/varoquau/.local/bin',
#      '/usr/lib/python2.7',
#      '/home/varoquau/.local/lib/python2.7/site-packages',
#      '/usr/lib/python2.7/dist-packages',
#      '/usr/local/lib/python2.7/dist-packages',
#      ...]
# 
# Modules must be located in the search path, therefore you can:
# 
# * write your own modules within directories already defined in the
#   search path (e.g. ``$HOME/.local/lib/python2.7/dist-packages``). You
#   may use symbolic links (on Linux) to keep the code somewhere else.
# 
# * modify the environment variable ``PYTHONPATH`` to include the
#   directories containing the user-defined modules.
# 
#   .. tip::
# 
#     On Linux/Unix, add the following line to a file read by the shell at
#     startup (e.g. /etc/profile, .profile)
# 
#     ::
# 
#       export PYTHONPATH=$PYTHONPATH:/home/emma/user_defined_modules
# 
#     On Windows, http://support.microsoft.com/kb/310519 explains how to
#     handle environment variables.
# 
# * or modify the ``sys.path`` variable itself within a Python script.
# 
#   .. tip::
# 
#     ::
# 
#         import sys
#         new_path = '/home/emma/user_defined_modules'
#         if new_path not in sys.path:
#             sys.path.append(new_path)
# 
#     This method is not very robust, however, because it makes the code
#     less portable (user-dependent path) and because you have to add the
#     directory to your sys.path each time you want to import from a module
#     in this directory.
# 
# .. seealso::
# 
#     See https://docs.python.org/tutorial/modules.html for more information
#     about modules.
# 
# Packages
# --------
# 
# A directory that contains many modules is called a *package*. A package
# is a module with submodules (which can have submodules themselves, etc.).
# A special file called ``__init__.py`` (which may be empty) tells Python
# that the directory is a Python package, from which modules can be
# imported.
# 
# .. sourcecode:: bash
# 
#     $ ls
#     cluster/        io/          README.txt@     stsci/
#     __config__.py@  LATEST.txt@  setup.py@       __svn_version__.py@
#     __config__.pyc  lib/         setup.pyc       __svn_version__.pyc
#     constants/      linalg/      setupscons.py@  THANKS.txt@
#     fftpack/        linsolve/    setupscons.pyc  TOCHANGE.txt@
#     __init__.py@    maxentropy/  signal/         version.py@
#     __init__.pyc    misc/        sparse/         version.pyc
#     INSTALL.txt@    ndimage/     spatial/        weave/
#     integrate/      odr/         special/
#     interpolate/    optimize/    stats/
#     $ cd ndimage
#     $ ls
#     doccer.py@   fourier.pyc   interpolation.py@  morphology.pyc   setup.pyc
#     doccer.pyc   info.py@      interpolation.pyc  _nd_image.so
#     setupscons.py@
#     filters.py@  info.pyc      measurements.py@   _ni_support.py@
#     setupscons.pyc
#     filters.pyc  __init__.py@  measurements.pyc   _ni_support.pyc  tests/
#     fourier.py@  __init__.pyc  morphology.py@     setup.py@
# 
# 
# From Ipython:
# 
# .. sourcecode:: ipython
# 
#     In [1]: import scipy
# 
#     In [2]: scipy.__file__
#     Out[2]: '/usr/lib/python2.6/dist-packages/scipy/__init__.pyc'
# 
#     In [3]: import scipy.version
# 
#     In [4]: scipy.version.version
#     Out[4]: '0.7.0'
# 
#     In [5]: import scipy.ndimage.morphology
# 
#     In [6]: from scipy.ndimage import morphology
# 
#     In [17]: morphology.binary_dilation?
#     Type:           function
#     Base Class:     <type 'function'>
#     String Form:    <function binary_dilation at 0x9bedd84>
#     Namespace:      Interactive
#     File:           /usr/lib/python2.6/dist-packages/scipy/ndimage/morphology.py
#     Definition:     morphology.binary_dilation(input, structure=None,
#     iterations=1, mask=None, output=None, border_value=0, origin=0,
#     brute_force=False)
#     Docstring:
#         Multi-dimensional binary dilation with the given structure.
# 
#         An output array can optionally be provided. The origin parameter
#         controls the placement of the filter. If no structuring element is
#         provided an element is generated with a squared connectivity equal
#         to one. The dilation operation is repeated iterations times.  If
#         iterations is less than 1, the dilation is repeated until the
#         result does not change anymore.  If a mask is given, only those
#         elements with a true value at the corresponding mask element are
#         modified at each iteration.
# 
# 
# 
# 
# Good practices
# --------------
# 
# * Use **meaningful** object **names**
# 
# * **Indentation: no choice!**
# 
#   .. tip::
# 
#     Indenting is compulsory in Python! Every command block following a
#     colon bears an additional indentation level with respect to the
#     previous line with a colon. One must therefore indent after
#     ``def f():`` or ``while:``. At the end of such logical blocks, one
#     decreases the indentation depth (and re-increases it if a new block
#     is entered, etc.)
# 
#     Strict respect of indentation is the price to pay for getting rid of
#     ``{`` or ``;`` characters that delineate logical blocks in other
#     languages. Improper indentation leads to errors such as
# 
#     .. sourcecode:: ipython
# 
#         ------------------------------------------------------------
#         IndentationError: unexpected indent (test.py, line 2)
# 
#     All this indentation business can be a bit confusing in the
#     beginning. However, with the clear indentation, and in the absence of
#     extra characters, the resulting code is very nice to read compared to
#     other languages.
# 
# * **Indentation depth**: Inside your text editor, you may choose to
#   indent with any positive number of spaces (1, 2, 3, 4, ...). However,
#   it is considered good practice to **indent with 4 spaces**. You may
#   configure your editor to map the ``Tab`` key to a 4-space
#   indentation. 
# 
# * **Style guidelines**
# 
#   **Long lines**: you should not write very long lines that span over more
#   than (e.g.) 80 characters. Long lines can be broken with the ``\``
#   character ::
# 
#       >>> long_line = "Here is a very very long line \
#       ... that we break in two parts."
# 
#   **Spaces**
# 
#   Write well-spaced code: put whitespaces after commas, around arithmetic
#   operators, etc.::
# 
#       >>> a = 1 # yes
#       >>> a=1 # too cramped
# 
#   A certain number of rules
#   for writing "beautiful" code (and more importantly using the same
#   conventions as anybody else!) are given in the `Style Guide for Python
#   Code <https://www.python.org/dev/peps/pep-0008>`_.
# 
# 
# ____
# 
# 
# .. topic:: **Quick read**
# 
#    If you want to do a first quick pass through the Scipy lectures to
#    learn the ecosystem, you can directly skip to the next chapter:
#    :ref:`numpy`.
# 
#    The remainder of this chapter is not necessary to follow the rest of
#    the intro part. But be sure to come back and finish this chapter later.
# 

# Input and Output
# ================
# 
# To be exhaustive, here are some information about input and output in
# Python. Since we will use the Numpy methods to read and write files,
# **you may skip this chapter at first reading**.
# 
# We write or read **strings** to/from files (other types must be converted to
# strings). To write in a file::
# 
#     >>> f = open('workfile', 'w') # opens the workfile file
#     >>> type(f)    # doctest: +SKIP 
#     <type 'file'>
#     >>> f.write('This is a test \nand another test')   # doctest: +SKIP 
#     >>> f.close()
# 
# To read from a file
# 
# .. sourcecode:: ipython
# 
#     In [1]: f = open('workfile', 'r')
# 
#     In [2]: s = f.read()
# 
#     In [3]: print(s)
#     This is a test 
#     and another test
# 
#     In [4]: f.close()
# 
# 
# .. seealso::
#    
#    For more details: https://docs.python.org/tutorial/inputoutput.html
# 
# Iterating over a file
# ~~~~~~~~~~~~~~~~~~~~~
# 
# .. sourcecode:: ipython
# 
#     In [6]: f = open('workfile', 'r')
# 
#     In [7]: for line in f:
#        ...:     print(line)
#        ...:
#     This is a test 
# 
#     and another test
# 
#     In [8]: f.close()
# 
# File modes
# ----------
# 
# * Read-only: ``r``
# * Write-only: ``w``
# 
#   * Note: Create a new file or *overwrite* existing file.
# 
# * Append a file: ``a``
# * Read and Write: ``r+``
# * Binary mode: ``b``
# 
#   * Note: Use for binary files, especially on Windows.
# 
# 

# Standard Library
# ================
# 
# .. note:: Reference document for this section:
# 
#  * The Python Standard Library documentation:
#    https://docs.python.org/library/index.html
# 
#  * Python Essential Reference, David Beazley, Addison-Wesley Professional
# 
# ``os`` module: operating system functionality
# -----------------------------------------------
# 
# *"A portable way of using operating system dependent functionality."*
# 
# Directory and file manipulation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# Current directory:
# 
# .. sourcecode:: ipython
# 
#     In [17]: os.getcwd()
#     Out[17]: '/Users/cburns/src/scipy2009/scipy_2009_tutorial/source'
# 
# List a directory:
# 
# .. sourcecode:: ipython
# 
#     In [31]: os.listdir(os.curdir)
#     Out[31]:
#     ['.index.rst.swo',
#      '.python_language.rst.swp',
#      '.view_array.py.swp',
#      '_static',
#      '_templates',
#      'basic_types.rst',
#      'conf.py',
#      'control_flow.rst',
#      'debugging.rst',
#      ...
# 
# Make a directory:
# 
# .. sourcecode:: ipython
# 
#     In [32]: os.mkdir('junkdir')
# 
#     In [33]: 'junkdir' in os.listdir(os.curdir)
#     Out[33]: True
# 
# Rename the directory:
# 
# .. sourcecode:: ipython
# 
#     In [36]: os.rename('junkdir', 'foodir')
# 
#     In [37]: 'junkdir' in os.listdir(os.curdir)
#     Out[37]: False
# 
#     In [38]: 'foodir' in os.listdir(os.curdir)
#     Out[38]: True
# 
#     In [41]: os.rmdir('foodir')
# 
#     In [42]: 'foodir' in os.listdir(os.curdir)
#     Out[42]: False
# 
# Delete a file:
# 
# .. sourcecode:: ipython
# 
#     In [44]: fp = open('junk.txt', 'w')
# 
#     In [45]: fp.close()
# 
#     In [46]: 'junk.txt' in os.listdir(os.curdir)
#     Out[46]: True
# 
#     In [47]: os.remove('junk.txt')
# 
#     In [48]: 'junk.txt' in os.listdir(os.curdir)
#     Out[48]: False
# 
# ``os.path``: path manipulations
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# ``os.path`` provides common operations on pathnames.
# 
# .. sourcecode:: ipython
# 
#     In [70]: fp = open('junk.txt', 'w')
# 
#     In [71]: fp.close()
# 
#     In [72]: a = os.path.abspath('junk.txt')
# 
#     In [73]: a
#     Out[73]: '/Users/cburns/src/scipy2009/scipy_2009_tutorial/source/junk.txt'
# 
#     In [74]: os.path.split(a)
#     Out[74]: ('/Users/cburns/src/scipy2009/scipy_2009_tutorial/source',
#               'junk.txt')
# 
#     In [78]: os.path.dirname(a)
#     Out[78]: '/Users/cburns/src/scipy2009/scipy_2009_tutorial/source'
# 
#     In [79]: os.path.basename(a)
#     Out[79]: 'junk.txt'
# 
#     In [80]: os.path.splitext(os.path.basename(a))
#     Out[80]: ('junk', '.txt')
# 
#     In [84]: os.path.exists('junk.txt')
#     Out[84]: True
# 
#     In [86]: os.path.isfile('junk.txt')
#     Out[86]: True
# 
#     In [87]: os.path.isdir('junk.txt')
#     Out[87]: False
# 
#     In [88]: os.path.expanduser('~/local')
#     Out[88]: '/Users/cburns/local'
# 
#     In [92]: os.path.join(os.path.expanduser('~'), 'local', 'bin')
#     Out[92]: '/Users/cburns/local/bin'
# 
# Running an external command
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# .. sourcecode:: ipython
# 
#   In [8]: os.system('ls')
#   basic_types.rst   demo.py          functions.rst  python_language.rst  standard_library.rst
#   control_flow.rst  exceptions.rst   io.rst         python-logo.png
#   demo2.py          first_steps.rst  oop.rst        reusing_code.rst
# 
# .. note:: Alternative to ``os.system``
# 
#     A noteworthy alternative to ``os.system`` is the `sh module
#     <http://amoffat.github.com/sh/>`_. Which provides much more convenient ways to
#     obtain the output, error stream and exit code of the external command.
# 
#     .. sourcecode:: ipython
# 
#         In [20]: import sh
#         In [20]: com = sh.ls()
# 
#         In [21]: print(com)
#         basic_types.rst   exceptions.rst   oop.rst              standard_library.rst
#         control_flow.rst  first_steps.rst  python_language.rst
#         demo2.py          functions.rst    python-logo.png
#         demo.py           io.rst           reusing_code.rst
# 
#         In [22]: print(com.exit_code)
#         0
#         In [23]: type(com)
#         Out[23]: sh.RunningCommand
# 
# 
# Walking a directory
# ~~~~~~~~~~~~~~~~~~~~
# 
# ``os.path.walk`` generates a list of filenames in a directory tree.
# 
# .. sourcecode:: ipython
# 
#     In [10]: for dirpath, dirnames, filenames in os.walk(os.curdir):
#        ....:     for fp in filenames:
#        ....:         print(os.path.abspath(fp))
#        ....:
#        ....:
#     /Users/cburns/src/scipy2009/scipy_2009_tutorial/source/.index.rst.swo
#     /Users/cburns/src/scipy2009/scipy_2009_tutorial/source/.view_array.py.swp
#     /Users/cburns/src/scipy2009/scipy_2009_tutorial/source/basic_types.rst
#     /Users/cburns/src/scipy2009/scipy_2009_tutorial/source/conf.py
#     /Users/cburns/src/scipy2009/scipy_2009_tutorial/source/control_flow.rst
#     ...
# 
# Environment variables:
# ~~~~~~~~~~~~~~~~~~~~~~
# 
# .. sourcecode:: ipython
# 
#     In [9]: import os
# 
#     In [11]: os.environ.keys()
#     Out[11]:
#     ['_',
#      'FSLDIR',
#      'TERM_PROGRAM_VERSION',
#      'FSLREMOTECALL',
#      'USER',
#      'HOME',
#      'PATH',
#      'PS1',
#      'SHELL',
#      'EDITOR',
#      'WORKON_HOME',
#      'PYTHONPATH',
#      ...
# 
#     In [12]: os.environ['PYTHONPATH']
#     Out[12]: '.:/Users/cburns/src/utils:/Users/cburns/src/nitools:
#     /Users/cburns/local/lib/python2.5/site-packages/:
#     /usr/local/lib/python2.5/site-packages/:
#     /Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5'
# 
#     In [16]: os.getenv('PYTHONPATH')
#     Out[16]: '.:/Users/cburns/src/utils:/Users/cburns/src/nitools:
#     /Users/cburns/local/lib/python2.5/site-packages/:
#     /usr/local/lib/python2.5/site-packages/:
#     /Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5'
# 
# 
# ``shutil``: high-level file operations
# ---------------------------------------
# 
# The ``shutil`` provides useful file operations:
# 
#     * ``shutil.rmtree``: Recursively delete a directory tree.
#     * ``shutil.move``: Recursively move a file or directory to another location.
#     * ``shutil.copy``: Copy files or directories.
# 
# ``glob``: Pattern matching on files
# -------------------------------------
# 
# The ``glob`` module provides convenient file pattern matching.
# 
# Find all files ending in ``.txt``:
# 
# .. sourcecode:: ipython
# 
#     In [18]: import glob
# 
#     In [19]: glob.glob('*.txt')
#     Out[19]: ['holy_grail.txt', 'junk.txt', 'newfile.txt']
# 
# 
# 
# ``sys`` module: system-specific information
# --------------------------------------------
# 
# System-specific information related to the Python interpreter.
# 
# * Which version of python are you running and where is it installed:
# 
#   .. sourcecode:: ipython
# 
#     In [117]: sys.platform
#     Out[117]: 'darwin'
# 
#     In [118]: sys.version
#     Out[118]: '2.5.2 (r252:60911, Feb 22 2008, 07:57:53) \n
#               [GCC 4.0.1 (Apple Computer, Inc. build 5363)]'
# 
#     In [119]: sys.prefix
#     Out[119]: '/Library/Frameworks/Python.framework/Versions/2.5'
# 
# * List of command line arguments passed to a Python script:
# 
#   .. sourcecode:: ipython
# 
#    In [100]: sys.argv
#    Out[100]: ['/Users/cburns/local/bin/ipython']
# 
# 
# ``sys.path`` is a list of strings that specifies the search path for
# modules.  Initialized from PYTHONPATH:
# 
# .. sourcecode:: ipython
# 
#     In [121]: sys.path
#     Out[121]:
#     ['',
#      '/Users/cburns/local/bin',
#      '/Users/cburns/local/lib/python2.5/site-packages/grin-1.1-py2.5.egg',
#      '/Users/cburns/local/lib/python2.5/site-packages/argparse-0.8.0-py2.5.egg',
#      '/Users/cburns/local/lib/python2.5/site-packages/urwid-0.9.7.1-py2.5.egg',
#      '/Users/cburns/local/lib/python2.5/site-packages/yolk-0.4.1-py2.5.egg',
#      '/Users/cburns/local/lib/python2.5/site-packages/virtualenv-1.2-py2.5.egg',
#      ...
# 
# ``pickle``: easy persistence
# -------------------------------
# 
# Useful to store arbitrary objects to a file. Not safe or fast!
# 
# .. sourcecode:: ipython
# 
#   In [1]: import pickle
# 
#   In [2]: l = [1, None, 'Stan']
# 
#   In [3]: pickle.dump(l, file('test.pkl', 'w'))
# 
#   In [4]: pickle.load(file('test.pkl'))
#   Out[4]: [1, None, 'Stan']
# 
# 
# .. topic:: Exercise
# 
#     Write a program to search your ``PYTHONPATH`` for the module ``site.py``.
# 
# :ref:`path_site`
# 

# Exception handling in Python
# ============================
# 
# It is likely that you have raised Exceptions if you have
# typed all the previous commands of the tutorial. For example, you may
# have raised an exception if you entered a command with a typo.
# 
# Exceptions are raised by different kinds of errors arising when executing
# Python code. In your own code, you may also catch errors, or define custom
# error types. You may want to look at the descriptions of the `the built-in
# Exceptions <https://docs.python.org/2/library/exceptions.html>`_ when looking
# for the right exception type.
# 
# Exceptions
# -----------
# 
# Exceptions are raised by errors in Python:
# 
# .. sourcecode:: ipython
# 
#     In [1]: 1/0
#     ---------------------------------------------------------------------------
#     ZeroDivisionError: integer division or modulo by zero
# 
#     In [2]: 1 + 'e'
#     ---------------------------------------------------------------------------
#     TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 
#     In [3]: d = {1:1, 2:2}
# 
#     In [4]: d[3]
#     ---------------------------------------------------------------------------
#     KeyError: 3
# 
#     In [5]: l = [1, 2, 3]
# 
#     In [6]: l[4]
#     ---------------------------------------------------------------------------
#     IndexError: list index out of range
# 
#     In [7]: l.foobar
#     ---------------------------------------------------------------------------
#     AttributeError: 'list' object has no attribute 'foobar'
# 
# As you can see, there are **different types** of exceptions for different errors.
# 
# Catching exceptions
# --------------------
# 
# try/except
# ~~~~~~~~~~~
# 
# .. sourcecode:: ipython
# 
#     In [10]: while True:
#        ....:     try:
#        ....:         x = int(raw_input('Please enter a number: '))
#        ....:         break
#        ....:     except ValueError:
#        ....:         print('That was no valid number.  Try again...')
#        ....: 
#     Please enter a number: a
#     That was no valid number.  Try again...
#     Please enter a number: 1
# 
#     In [9]: x
#     Out[9]: 1
# 
# try/finally
# ~~~~~~~~~~~~
# 
# .. sourcecode:: ipython
# 
#     In [10]: try:
#        ....:     x = int(raw_input('Please enter a number: '))
#        ....: finally:
#        ....:     print('Thank you for your input')
#        ....:
#        ....:
#     Please enter a number: a
#     Thank you for your input
#     ---------------------------------------------------------------------------
#     ValueError: invalid literal for int() with base 10: 'a'
# 
# Important for resource management (e.g. closing a file)
# 
# Easier to ask for forgiveness than for permission
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# 
# .. sourcecode:: ipython
# 
#     In [11]: def print_sorted(collection):
#        ....:     try:
#        ....:         collection.sort()
#        ....:     except AttributeError:
#        ....:         pass # The pass statement does nothing
#        ....:     print(collection)
#        ....:
#        ....:
# 
#     In [12]: print_sorted([1, 3, 2])
#     [1, 2, 3]
# 
#     In [13]: print_sorted(set((1, 3, 2)))
#     set([1, 2, 3])
# 
#     In [14]: print_sorted('132')
#     132
# 
# 
# Raising exceptions
# ------------------
# 
# * Capturing and reraising an exception:
# 
#   .. sourcecode:: ipython
# 
#     In [15]: def filter_name(name):
#        ....:	try:
#        ....:	    name = name.encode('ascii')
#        ....:	except UnicodeError as e:
#        ....:	    if name == 'Gaël':
#        ....:		print('OK, Gaël')
#        ....:	    else:
#        ....:		raise e
#        ....:	return name
#        ....:
# 
#     In [16]: filter_name('Gaël')
#     OK, Gaël
#     Out[16]: 'Ga\xc3\xabl'
# 
#     In [17]: filter_name('Stéfan')
#     ---------------------------------------------------------------------------
#     UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 2: ordinal not in range(128)
# 
# 
# * Exceptions to pass messages between parts of the code:
# 
#   .. sourcecode:: ipython
# 
#     In [17]: def achilles_arrow(x):
#        ....:    if abs(x - 1) < 1e-3:
#        ....:        raise StopIteration
#        ....:    x = 1 - (1-x)/2.
#        ....:    return x
#        ....:
# 
#     In [18]: x = 0
# 
#     In [19]: while True:
#        ....:     try:
#        ....:         x = achilles_arrow(x)
#        ....:     except StopIteration:
#        ....:         break
#        ....:
#        ....:
# 
#     In [20]: x
#     Out[20]: 0.9990234375
# 
# 
# Use exceptions to notify certain conditions are met (e.g.
# StopIteration) or not (e.g. custom error raising)
# 
# 
# 

# Object-oriented programming (OOP)
# =================================
# 
# Python supports object-oriented programming (OOP). The goals of OOP are:
# 
#     * to organize the code, and
# 
#     * to re-use code in similar contexts.
# 
# 
# Here is a small example: we create a Student *class*, which is an object
# gathering several custom functions (*methods*) and variables (*attributes*),
# we will be able to use::
# 
#     >>> class Student(object):
#     ...     def __init__(self, name):
#     ...         self.name = name
#     ...     def set_age(self, age):
#     ...         self.age = age
#     ...     def set_major(self, major):
#     ...         self.major = major
#     ...
#     >>> anna = Student('anna')
#     >>> anna.set_age(21)
#     >>> anna.set_major('physics')
# 
# In the previous example, the Student class has ``__init__``, ``set_age`` and
# ``set_major`` methods. Its attributes are ``name``, ``age`` and ``major``. We
# can call these methods and attributes with the following notation:
# ``classinstance.method`` or  ``classinstance.attribute``.  The ``__init__``
# constructor is a special method we call with: ``MyClass(init parameters if
# any)``.
# 
# Now, suppose we want to create a new class MasterStudent with the same
# methods and attributes as the previous one, but with an additional
# ``internship`` attribute. We won't copy the previous class, but
# **inherit** from it::
# 
#     >>> class MasterStudent(Student):
#     ...     internship = 'mandatory, from March to June'
#     ...
#     >>> james = MasterStudent('james')
#     >>> james.internship
#     'mandatory, from March to June'
#     >>> james.set_age(23)
#     >>> james.age
#     23
# 
# The MasterStudent class inherited from the Student attributes and methods.
# 
# Thanks to classes and object-oriented programming, we can organize code
# with different classes corresponding to different objects we encounter
# (an Experiment class, an Image class, a Flow class, etc.), with their own
# methods and attributes. Then we can use inheritance to consider
# variations around a base class and **re-use** code. Ex : from a Flow
# base class, we can create derived StokesFlow, TurbulentFlow,
# PotentialFlow, etc.
# 
# 
