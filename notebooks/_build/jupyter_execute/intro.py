#!/usr/bin/env python
# coding: utf-8

# # 데이터 과학과 파이썬

# **감사의 말**: 아래 내용은 [SciPy Lecture Notes](https://scipy-lectures.org/_downloads/ScipyLectures-simple.pdf)의 1장 내용을 많이 참고합니다. 

# ## 파이썬

# 데이터 과학자는 보통 다음 세 가지를 필요로 한다.
# 
# * 데이터 구하기: 모의 실험
# * 데이터 처리: 데이터로부터 정보 얻기
# * 데이터 시각화: 얻어진 정보 이해 및 전달

# 파이썬의 장점은 다음과 같다.
# 
# * 수치 계산, 데이터 처리 및 시각화와 관련된 많고 다양한 툴을 제공한다.
# * 배우고 사용하기 쉽다.
# * 문법이 단순하다.
# * 효율적인 코드를 작성하기 쉽다.
# * 데이터 분석 이외에 프로그래밍 관련 모든 분야에서 사용된다.

# ## 파이썬 대 기타 언어

# **컴파일 언어**
# 
# C, C++, C#, 자바 등 작성된 코드를 컴파일<font size="2">compile</font>한 후에 실행하도록 하는 
# 컴파일 언어<font size="2">compiled language</font>의
# 장점과 단점은 다음과 같다.
# 
# * 장점
#     * 실행이 매우 빠르다. 따라서 매우 많은 양의 계산에 적합하다.
# * 단점
#     * 사용하기 어렵다. 메모리 수동 관리, 복잡한 구문 등 일반 사용자가 접근하기에는 
#         조금 어려운 프로그래밍 언어이다.

# **매트랩**<font size="2">Matlab</font>
# 
# * 장점
#     * 다양한 분야에서 활용될 수 있는 효율적인 수치 계산용 알고리즘을 포함하는 라이브러리를 제공한다.
#     * 편리한 개발환경을 제공한다.
#     * (유료) 기술 지원이 제공된다.
# * 단점
#     * 언어 자체가 고수준의 기능을 지원하지 않는다.
#     * 유료.

# **R**
# 
# * 장점
#     * 오픈 소스<font size="2">open source</font>이며 무료.
#     * 통계 관련 고수준의 기능을 지원한다.
#     
# * 단점
#     * 매트랩보다 지원되는 알고리즘이 적으며, 언어 자체도 고수준의 기능을 제대로 지원하지 않는다.
#     * 지원되는 기능도 제한적인 영역에서만 활용되어 보편성이 떨어진다.

# **파이썬**
# 
# * 장점
#     * 계산 관련 라이브러리가 풍부하다.
#     * 체계적이며 가독성이 높은 코드 작성을 지원한다.
#     * 웹서버 등 계산 과학 이외의 기타 분야에서도 활용되는 라이브러리를 지원한다.
#     * 오픈 소스이자 무료이고 많은 사용자 그룹이 존재한다.
#     * 다양한 개발환경이 지원된다.
#         * [IPython](http://ipython.readthedocs.io/en/stable/)
#         * [Spyder](https://www.spyder-ide.org/)
#         * [Jupyter notebooks](http://jupyter.org/)
#         * [Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
#         
# * 단점
#     * 컴파일 언어로 작성된 프로그램에 비해 상대적으로 느리게 작동한다.
#     * 시스템 개발 등에 사용되기에는 제한적이다.

# ## 데이터 과학용 파이썬 생태계

# Unlike Matlab, or R, Python does not come with a prebundled set
# of modules for scientific computing. Below are the basic building blocks
# that can be combined to obtain a scientific computing environment:

# **Python**, a generic and modern computing language
# 
# * The language: flow control, data types (`string`, `int`),
#   data collections (lists, dictionaries), etc.
# 
# * Modules of the standard library: string processing, file
#   management, simple network protocols.
# 
# * A large number of specialized modules or applications written in
#   Python: web framework, etc. ... and scientific
#   computing.
# 
# * Development tools (automatic testing, documentation generation)
# 
# **참고**: `<python_language_chapter>`

# <div align="center"><img src="https://github.com/codingalzi/pyfast/blob/master/notebooks/images/random_c.jpg?raw=true" width="50%"></div>

# **Core numeric libraries**
# 
# * **Numpy**: numerical computing with powerful **numerical arrays**
#   objects, and routines to manipulate them. [http://www.numpy.org/](http://www.numpy.org/)
# 
# **참고**: `<numpy>`
# 
# * **Scipy** : highlevel numerical routines.
#   Optimization, regression, interpolation, etc [http://www.scipy.org/](http://www.scipy.org/)
# 
# **참고**: `<scipy>`
# 
# * **Matplotlib** : 2D visualization, "publicationready" plots
#   [http://matplotlib.org/](http://matplotlib.org/)
# 
# **참고**: `<matplotlib>`

# <div align="center"><img src="https://github.com/codingalzi/pyfast/blob/master/notebooks/images/snapshot_ipython.png?raw=true" width="50%"></div>

# **Advanced interactive environments**:
# 
# * **IPython**, an advanced **Python console** [http://ipython.org/](http://ipython.org/)
# 
# * **Jupyter**, **notebooks** in the browser [http://jupyter.org/](http://jupyter.org/)

# <div align="center"><img src="https://github.com/codingalzi/pyfast/blob/master/notebooks/images/example_surface_from_irregular_data.jpg?raw=true" width="50%"></div>

# **Domainspecific packages**,
# 
# * **Mayavi** for 3D visualization (link to chapter `mayavilabel`)
# 
# * **pandas, statsmodels, seaborn** for statistics (link to chapter `statistics`)
# 
# * **sympy** for symbolic computing (link to chapter `sympy`)
# 
# * **scikitimage** for image processing (link to chapter `scikit_image`)
# 
# * **scikitlearn** for machine learning (link to chapter `scikitlearn_chapter`)
# 
# and much more packages not documented in the scipy lectures.
# 
# **참고**: chapters on advanced topics, chapters on packages and applications

# ## Before starting: Installing a working environment

# Python comes in many flavors, and there are many ways to install it.
# However, we recommend to install a scientificcomputing distribution,
# that comes readily with optimized versions of scientific modules.
# 
# **Under Linux**
# 
# If you have a recent distribution, most of the tools are probably
# packaged, and it is recommended to use your package manager.
# 
# **Other systems**
# 
# There are several fullyfeatured Scientific Python distributions:
# 
# * [Anaconda](https://www.anaconda.com/download/)
# * [EPD](https://store.enthought.com/downloads)
# * [WinPython](https://winpython.github.io)

# ## The workflow: interactive environments and text editors

# **Interactive work to test and understand algorithms:** In this section, we
# describe a workflow combining interactive work and consolidation.
# 
# Python is a generalpurpose language. As such, there is not one blessed
# environment to work in, and not only one way of using it. Although
# this makes it harder for beginners to find their way, it makes it
# possible for Python to be used for programs, in web servers, or
# embedded devices.

# ### Interactive work

# We recommend an interactive work with the 
# [IPython](http://ipython.org) console, or its offspring, the 
# [Jupyter notebook](http://jupyter.readthedocs.io/en/latest/contentquickstart.html). They are handy to explore and understand algorithms.

# **Under the notebook**
# 
# To execute code, press "shift enter"

# Start *ipython*:
# 
# ```
# In [1]: print('Hello world')
# Hello world
# ```

# Getting help by using the **?** operator after an object:

# ```
# In [2]: print?
# Docstring:
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# 
# Prints the values to a stream, or to sys.stdout by default.
# Optional keyword arguments:
# file:  a file-like object (stream); defaults to the current sys.stdout.
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.
# Type:      builtin_function_or_method
# ```

# **참고**
# 
# * IPython user manual: [https://ipython.readthedocs.io/en/stable/](https://ipython.readthedocs.io/en/stable/)
# 
# * Jupyter Notebook QuickStart:
#   [http://jupyter.readthedocs.io/en/latest/contentquickstart.html](http://jupyter.readthedocs.io/en/latest/contentquickstart.html)

# ### Elaboration of the work in an editor

# As you move forward, it will be important to not only work interactively,
# but also to create and reuse Python files. For this, a powerful code editor
# will get you far. Here are several good easytouse editors:
# 
#   * [Spyder](https://www.spyderide.org/): integrates an IPython
#     console, a debugger, a profiler...
#   * [PyCharm](https://www.jetbrains.com/pycharm): integrates an IPython
#     console, notebooks, a debugger... (freely available,
#     but commercial)
#   * [Visual Studio Code](https://code.visualstudio.com/docs/languages/python):
#     integrates a Python console, notebooks, a debugger, ...
#   * [Atom](https://atom.io)
# 
# Some of these are shipped by the various scientific Python distributions,
# and you can find them in the menus.

# As an exercise, create a file *my_file.py* in a code editor, and add the
# following lines:
# 
# ```
# s = 'Hello world'
# print(s)
# ```

# Now, you can run it in IPython console or a notebook and explore the
# resulting variables:

# ```
# In [1]: %run my_file.py
# Hello world
# 
# In [2]: s
# Out[2]: 'Hello world'
# 
# In [3]: %whos
# Variable   Type    Data/Info
# ----------------------------
# s          str     Hello world
# ```

# ```{seealso}
# 
# **From a script to functions**
# 
# While it is tempting to work only with scripts, that is a file full
# of instructions following each other, do plan to progressively evolve
# the script to a set of functions:
# 
# * A script is not reusable, functions are.
# 
# * Thinking in terms of functions helps breaking the problem in small
#   blocks.
# ```

# ### IPython and Jupyter Tips and Tricks

# The user manuals contain a wealth of information. Here we give a quick
# introduction to four useful features: *history*, *tab completion*, *magic
# functions*, and *aliases*.

# **Command history** Like a UNIX shell, the IPython console supports
# command history. Type *up* and *down* to navigate previously typed
# commands:

# ```
# In [1]: x = 10
# 
# In [2]: <UP>
# 
# In [2]: x = 10
# ```

# **Tab completion** Tab completion, is a convenient way to explore the
# structure of any object you’re dealing with. Simply type object_name.<TAB> to
# view the object’s attributes. Besides Python objects and keywords, tab
# completion also works on file and directory names.*

# ```
# In [1]: x = 10
# 
# In [2]: x.<TAB>
# x.bit_length   x.denominator  x.imag         x.real
# x.conjugate    x.from_bytes   x.numerator    x.to_bytes
# ```

# **Magic functions**
# The console and the notebooks support socalled *magic* functions by prefixing a command with the
# `%` character. For example, the `run` and `whos` functions from the
# previous section are magic functions. Note that, the setting `automagic`,
# which is enabled by default, allows you to omit the preceding `%` sign. Thus,
# you can just type the magic function and it will work.
# 
# Other useful magic functions are:
# 
# * `%cd` to change the current directory.
# 
#     ```
#     In [1]: cd /tmp
#     /tmp
#     ```
# 
# * `%cpaste` allows you to paste code, especially code from websites which has
#   been prefixed with the standard Python prompt (e.g. `>>>`) or with an ipython
#   prompt, (e.g. `in [3]`):
# 
#     ```
#     In [2]: %cpaste
#     Pasting code; enter '' alone on the line to stop or use CtrlD.
#     :>>> for i in range(3):
#     :...     print(i)
#     :--
#     0
#     1
#     2
#     ```
#     
# * `%timeit` allows you to time the execution of short snippets using the
#   `timeit` module from the standard library:
# 
#     ```
#     In [3]: %timeit x = 10
#     10000000 loops, best of 3: 39 ns per loop
#     ```
#     
#     **참고**: `<optimizing_code_chapter>`
# 
# * `%debug` allows you to enter postmortem debugging. That is to say, if the
#   code you try to execute, raises an exception, using `%debug` will enter the
#   debugger at the point where the exception was thrown.
# 
#     ```
#     In [4]: x === 10
#     File "<ipythoninput612fd421b5f28>", line 1
#         x === 10
#         ^
#     SyntaxError: invalid syntax
# 
#     In [5]: %debug
#     > /.../IPython/core/compilerop.py (87)ast_parse()
#          86         and are passed to the builtin compile function."""
#     ---> 87         return compile(source, filename, symbol, self.flags  PyCF_ONLY_AST, 1)
#          88
# 
#     ipdb>locals()
#     {'source': u'x === 10\n', 'symbol': 'exec', 'self':
#     <IPython.core.compilerop.CachingCompiler instance at 0x2ad8ef0>,
#     'filename': '<ipythoninput612fd421b5f28>'}
#     ```
# 
#     **참고**: `<debugging_chapter>`

# **Aliases**
# Furthermore IPython ships with various *aliases* which emulate common UNIX
# command line tools such as `ls` to list files, `cp` to copy files and `rm` to
# remove files (a full list of aliases is shown when typing `alias`).

# **Getting help**
# 
# * The builtin cheatsheet is accessible via the `%quickref` magic
#     function.
# 
# * A list of all available magic functions is shown when typing `%magic`.
