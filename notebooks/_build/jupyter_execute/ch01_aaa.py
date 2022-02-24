#!/usr/bin/env python
# coding: utf-8

# # 모듈과 패키지

# For now, we have typed all instructions in the interpreter. For longer
# sets of instructions we need to change track and write the code in text
# files (using a text editor), that we will call either *scripts* or
# *modules*. Use your favorite text editor (provided it offers syntax
# highlighting for Python), or the editor that comes with the Scientific
# Python Suite you may be using.

# ## Scripts

# Let us first write a *script*, that is a file with a sequence of
# instructions that are executed each time the script is called.
# Instructions may be e.g. copied-and-pasted from the interpreter (but
# take care to respect indentation rules!).
# 
# The extension for Python files is ``.py``. Write or copy-and-paste the
# following lines in a file called ``test.py`` ::
# 
# message = "Hello how are you?"
# for word in message.split():
#     print(word)
# 
# .. tip::
# 
# Let us now execute the script interactively, that is inside the
# Ipython interpreter. This is maybe the most common use of scripts in
# scientific computing.
# 
# .. note::
# 
# in Ipython, the syntax to execute a script is ``%run script.py``. For
# example,
# 
# .. sourcecode:: ipython
# 
# In [1]: %run test.py
# Hello
# how
# are
# you?
# 
# In [2]: message
# Out[2]: 'Hello how are you?'
# 
# 
# The script has been executed. Moreover the variables defined in the
# script (such as ``message``) are now available inside the interpreter's
# namespace.
# 
# .. tip::
# 
# Other interpreters also offer the possibility to execute scripts
# (e.g., ``execfile`` in the plain Python interpreter, etc.).
# 
# It is also possible In order to execute this script as a *standalone
# program*, by executing the script inside a shell terminal (Linux/Mac
# console or cmd Windows console). For example, if we are in the same
# directory as the test.py file, we can execute this in a console:
# 
# .. sourcecode:: bash
# 
# $ python test.py
# Hello
# how
# are
# you?
# 
# .. tip::
# 
# Standalone scripts may also take command-line arguments
# 
# In ``file.py``::
# 
#     import sys
#     print(sys.argv)
# 
# .. sourcecode:: bash
# 
#     $ python file.py test arguments
#     ['file.py', 'test', 'arguments']
# 
# .. warning::
# 
#     Don't implement option parsing yourself. Use a dedicated module such as
#     :mod:`argparse`.
# 
# 
# Importing objects from modules
# ------------------------------
# 
# .. sourcecode:: ipython
# 
# In [1]: import os
# 
# In [2]: os
# Out[2]: <module 'os' from '/usr/lib/python2.6/os.pyc'>
# 
# In [3]: os.listdir('.')
# Out[3]:
# ['conf.py',
#  'basic_types.rst',
#  'control_flow.rst',
#  'functions.rst',
#  'python_language.rst',
#  'reusing.rst',
#  'file_io.rst',
#  'exceptions.rst',
#  'workflow.rst',
#  'index.rst']
# 
# And also:
# 
# .. sourcecode:: ipython
# 
# In [4]: from os import listdir
# 
# Importing shorthands:
# 
# .. sourcecode:: ipython
# 
# In [5]: import numpy as np
# 
# .. warning::
# 
# ::
# 
#     from os import *
# 
# This is called the *star import* and please, **Do not use it**
# 
# * Makes the code harder to read and understand: where do symbols come
#   from?
# 
# * Makes it impossible to guess the functionality by the context and
#   the name (hint: `os.name` is the name of the OS), and to profit
#   usefully from tab completion.
# 
# * Restricts the variable names you can use: `os.name` might override
#   `name`, or vise-versa.
# 
# * Creates possible name clashes between modules.
# 
# * Makes the code impossible to statically check for undefined
#   symbols.
# 
# .. tip::
# 
# Modules are thus a good way to organize code in a hierarchical way. Actually,
# all the scientific computing tools we are going to use are modules::
# 
# >>> import numpy as np # data arrays
# >>> np.linspace(0, 10, 6)
# array([  0.,   2.,   4.,   6.,   8.,  10.])
# >>> import scipy # scientific computing
# 
# 
# Creating modules
# -----------------
# 
# .. tip::
# 
# If we want to write larger and better organized programs (compared to
# simple scripts), where some objects are defined, (variables,
# functions, classes) and that we want to reuse several times, we have
# to create our own *modules*.
# 
# Let us create a module ``demo`` contained in the file ``demo.py``:
# 
# .. literalinclude:: demo.py
# 
# .. tip::
# 
# In this file, we defined two functions ``print_a`` and ``print_b``. Suppose
# we want to call the ``print_a`` function from the interpreter. We could
# execute the file as a script, but since we just want to have access to
# the function ``print_a``, we are rather going to **import it as a module**.
# The syntax is as follows.
# 
# 
# .. sourcecode:: ipython
# 
# In [1]: import demo
# 
# 
# In [2]: demo.print_a()
# a
# 
# In [3]: demo.print_b()
# b
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
# In [4]: demo?
# Type:               module
# Base Class: <type 'module'>
# String Form:        <module 'demo' from 'demo.py'>
# Namespace:  Interactive
# File:               /home/varoquau/Projects/Python_talks/scipy_2009_tutorial/source/demo.py
# Docstring:
#     A demo module.
# 
# 
# In [5]: who
# demo
# 
# In [6]: whos
# Variable   Type      Data/Info
# ------------------------------
# demo       module    <module 'demo' from 'demo.py'>
# 
# In [7]: dir(demo)
# Out[7]:
# ['__builtins__',
# '__doc__',
# '__file__',
# '__name__',
# '__package__',
# 'c',
# 'd',
# 'print_a',
# 'print_b']
# 
# 
# In [8]: demo.<TAB>
# demo.c        demo.print_a  demo.py       
# demo.d        demo.print_b  demo.pyc      
# 
# 
# Importing objects from modules into the main namespace
# 
# .. sourcecode:: ipython
# 
# In [9]: from demo import print_a, print_b
# 
# In [10]: whos
# Variable   Type        Data/Info
# --------------------------------
# demo       module      <module 'demo' from 'demo.py'>
# print_a    function    <function print_a at 0xb7421534>
# print_b    function    <function print_b at 0xb74214c4>
# 
# In [11]: print_a()
# a
# 
# .. warning::
# 
# **Module caching**
# 
#  Modules are cached: if you modify ``demo.py`` and re-import it in the
#  old session, you will get the old one.
# 
# Solution:
# 
#  .. sourcecode :: ipython
# 
#     In [10]: reload(demo)
# 
# In Python3 instead ``reload`` is not builtin, so you have to import the ``importlib`` module first and then do:
# 
#  .. sourcecode :: ipython
# 
#     In [10]: importlib.reload(demo)
# 
# '__main__' and module loading
# ------------------------------
# 
# .. tip::
# 
# Sometimes we want code to be executed when a module is
# run directly, but not when it is imported by another module.
# ``if __name__ == '__main__'`` allows us to check whether the
# module is being run directly.
# 
# File ``demo2.py``:
# 
# .. literalinclude:: demo2.py
# 
# Importing it:
# 
# .. sourcecode:: ipython
# 
# In [11]: import demo2
# b
# 
# In [12]: import demo2
# 
# Running it:
# 
# .. sourcecode:: ipython
# 
# In [13]: %run demo2
# b
# a
# 
# 
# Scripts or modules? How to organize your code
# ---------------------------------------------
# 
# .. Note:: Rule of thumb
# 
# * Sets of instructions that are called several times should be
#   written inside **functions** for better code reusability.
# 
# * Functions (or other bits of code) that are called from several
#   scripts should be written inside a **module**, so that only the
#   module is imported in the different scripts (do not copy-and-paste
#   your functions in the different scripts!).
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
# In [1]: import sys
# 
# In [2]: sys.path
# Out[2]: 
# ['',
#  '/home/varoquau/.local/bin',
#  '/usr/lib/python2.7',
#  '/home/varoquau/.local/lib/python2.7/site-packages',
#  '/usr/lib/python2.7/dist-packages',
#  '/usr/local/lib/python2.7/dist-packages',
#  ...]
# 
# Modules must be located in the search path, therefore you can:
# 
# * write your own modules within directories already defined in the
# search path (e.g. ``$HOME/.local/lib/python2.7/dist-packages``). You
# may use symbolic links (on Linux) to keep the code somewhere else.
# 
# * modify the environment variable ``PYTHONPATH`` to include the
# directories containing the user-defined modules.
# 
# .. tip::
# 
# On Linux/Unix, add the following line to a file read by the shell at
# startup (e.g. /etc/profile, .profile)
# 
# ::
# 
#   export PYTHONPATH=$PYTHONPATH:/home/emma/user_defined_modules
# 
# On Windows, http://support.microsoft.com/kb/310519 explains how to
# handle environment variables.
# 
# * or modify the ``sys.path`` variable itself within a Python script.
# 
# .. tip::
# 
# ::
# 
#     import sys
#     new_path = '/home/emma/user_defined_modules'
#     if new_path not in sys.path:
#         sys.path.append(new_path)
# 
# This method is not very robust, however, because it makes the code
# less portable (user-dependent path) and because you have to add the
# directory to your sys.path each time you want to import from a module
# in this directory.
# 
# .. seealso::
# 
# See https://docs.python.org/tutorial/modules.html for more information
# about modules.
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
# $ ls
# cluster/        io/          README.txt@     stsci/
# __config__.py@  LATEST.txt@  setup.py@       __svn_version__.py@
# __config__.pyc  lib/         setup.pyc       __svn_version__.pyc
# constants/      linalg/      setupscons.py@  THANKS.txt@
# fftpack/        linsolve/    setupscons.pyc  TOCHANGE.txt@
# __init__.py@    maxentropy/  signal/         version.py@
# __init__.pyc    misc/        sparse/         version.pyc
# INSTALL.txt@    ndimage/     spatial/        weave/
# integrate/      odr/         special/
# interpolate/    optimize/    stats/
# $ cd ndimage
# $ ls
# doccer.py@   fourier.pyc   interpolation.py@  morphology.pyc   setup.pyc
# doccer.pyc   info.py@      interpolation.pyc  _nd_image.so
# setupscons.py@
# filters.py@  info.pyc      measurements.py@   _ni_support.py@
# setupscons.pyc
# filters.pyc  __init__.py@  measurements.pyc   _ni_support.pyc  tests/
# fourier.py@  __init__.pyc  morphology.py@     setup.py@
# 
# 
# From Ipython:
# 
# .. sourcecode:: ipython
# 
# In [1]: import scipy
# 
# In [2]: scipy.__file__
# Out[2]: '/usr/lib/python2.6/dist-packages/scipy/__init__.pyc'
# 
# In [3]: import scipy.version
# 
# In [4]: scipy.version.version
# Out[4]: '0.7.0'
# 
# In [5]: import scipy.ndimage.morphology
# 
# In [6]: from scipy.ndimage import morphology
# 
# In [17]: morphology.binary_dilation?
# Type:           function
# Base Class:     <type 'function'>
# String Form:    <function binary_dilation at 0x9bedd84>
# Namespace:      Interactive
# File:           /usr/lib/python2.6/dist-packages/scipy/ndimage/morphology.py
# Definition:     morphology.binary_dilation(input, structure=None,
# iterations=1, mask=None, output=None, border_value=0, origin=0,
# brute_force=False)
# Docstring:
#     Multi-dimensional binary dilation with the given structure.
# 
#     An output array can optionally be provided. The origin parameter
#     controls the placement of the filter. If no structuring element is
#     provided an element is generated with a squared connectivity equal
#     to one. The dilation operation is repeated iterations times.  If
#     iterations is less than 1, the dilation is repeated until the
#     result does not change anymore.  If a mask is given, only those
#     elements with a true value at the corresponding mask element are
#     modified at each iteration.
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
# .. tip::
# 
# Indenting is compulsory in Python! Every command block following a
# colon bears an additional indentation level with respect to the
# previous line with a colon. One must therefore indent after
# ``def f():`` or ``while:``. At the end of such logical blocks, one
# decreases the indentation depth (and re-increases it if a new block
# is entered, etc.)
# 
# Strict respect of indentation is the price to pay for getting rid of
# ``{`` or ``;`` characters that delineate logical blocks in other
# languages. Improper indentation leads to errors such as
# 
# .. sourcecode:: ipython
# 
#     ------------------------------------------------------------
#     IndentationError: unexpected indent (test.py, line 2)
# 
# All this indentation business can be a bit confusing in the
# beginning. However, with the clear indentation, and in the absence of
# extra characters, the resulting code is very nice to read compared to
# other languages.
# 
# * **Indentation depth**: Inside your text editor, you may choose to
# indent with any positive number of spaces (1, 2, 3, 4, ...). However,
# it is considered good practice to **indent with 4 spaces**. You may
# configure your editor to map the ``Tab`` key to a 4-space
# indentation. 
# 
# * **Style guidelines**
# 
# **Long lines**: you should not write very long lines that span over more
# than (e.g.) 80 characters. Long lines can be broken with the ``\``
# character ::
# 
#   >>> long_line = "Here is a very very long line \
#   ... that we break in two parts."
# 
# **Spaces**
# 
# Write well-spaced code: put whitespaces after commas, around arithmetic
# operators, etc.::
# 
#   >>> a = 1 # yes
#   >>> a=1 # too cramped
# 
# A certain number of rules
# for writing "beautiful" code (and more importantly using the same
# conventions as anybody else!) are given in the `Style Guide for Python
# Code <https://www.python.org/dev/peps/pep-0008>`_.
# 
# 
# ____
# 
# 
# .. topic:: **Quick read**
# 
# If you want to do a first quick pass through the Scipy lectures to
# learn the ecosystem, you can directly skip to the next chapter:
# :ref:`numpy`.
# 
# The remainder of this chapter is not necessary to follow the rest of
# the intro part. But be sure to come back and finish this chapter later.

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
