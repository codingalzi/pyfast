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

# ## 스칼라 자료형

# 스칼라<font size="2">scalar</font>는 정수, 부동소수점, 부울값 등
# 단일 차원의 값을 가리키며, 파이썬의 기본 스칼라 자료형으로 지원된다.

# ### 정수

# -2, -1, 0, 1, 2 등의 정수는 `int` 유형<font size="2">type</font>의 값이다.
# 정수는 사칙연산, 변수 할당 등에 사용된다.

# In[9]:


1 + 2


# In[10]:


a = 4
type(a)


# ### 부동소수점

# **부동소수점**은 유리수, 실수 등을 가리키며 `float` 유형의 값이다.
# 정수와 마찬가지로 사칙연산, 변수 할당 등에 사용된다.

# In[11]:


2.1 + 3.3


# In[12]:


c = 2.1
type(c)


# 정수와의 연산도 가능한데, 이때 정수를 부동소수점으로 취급한다. 
# 예를 들어 3은 3.0으로 처리된다.

# In[13]:


2.3 + 3


# In[14]:


2.3 + 3.0


# ### 부울값

# 참과 거짓을 의미하는 `True`와 `False`를 
# **부울값**<font size="2">boolean</font>
# 또는 **진리값**이라 한다.
# 부울값은 `bool` 유형을 갖는 **유일한 두 개의 값**이다.

# In[15]:


type(True)


# In[16]:


d = False
type(d)


# 등식, 부등식 등이 부울값을 가리키는 
# **표현식**<font size="2">expression</font>이다.

# In[17]:


3 > 4


# In[18]:


test = (1.0 == 1)


# In[19]:


test


# In[20]:


type(test)


# ### 연산자

# 덧셈(`+`), 뺄셈(`-`), 곱셈(`*`), 나눗셈(`/`) 등 사칙연산을 계산기처럼 사용할 수 있다.

# In[21]:


7 * 3


# 정수에 점(`.`)을 찍으면 부동소수점으로 처리된다.

# In[22]:


7 * 3.


# 지수승은 `**` 를 사용한다.

# In[23]:


2 ** 10


# 정수 나눗셈의 몫(`//`)과 나머지(`%`) 연산도 지원된다.

# In[24]:


8 // 3


# In[25]:


8 % 3


# 몫 계산과 나눗셈 연산은 다르다.
# 몫은 정수 계산이며, 나눗셈은 부동소수점 연산이다.

# In[26]:


8 / 3


# 나눗셈의 몫이 우연히 정수인 경우엔 차이를 두지 않는다.

# In[27]:


(4 / 2) == (4 // 2)


# :::{admonition} 형변환 함수
# :class: info
# 
# `2.3 + 3`을 실행하면 파이썬 해석기<font size="2">interpreter</font>는
# 내부적으로 정수 `3`을 
# 정수를 부동소수점으로 형변환하는 함수 `float()`를 이용하여
# 부동소수점 `3.0`으로 유형을 변환한 후에
# 덧셈을 처리한다. 
# 이렇게 값의 유형을 적절하게 변환하는 기능을 
# **형변환**<font size="2">type casting</font>이라 부른다.
# 
# ```python
# >>> float(3)
# 3.0
# ```
# 
# `float()` 함수 이외에 `int()`, `str()`, `list()` 등 다양한 형변환 함수를 앞으로 
# 만나게 될 것이다.
# :::

# :::{admonition} 함수 이름 표기법
# :class: tip
# 
# `float`는 부동소수점 자료형을 가리키기도 하고 
# 형변환 함수를 가리키기도 한다. 
# 이를 구분하기 위해 여기서는 
# `int`, `float`, `str`, `list` 등과 `int()`, `float()`, `str()`, `list()` 등을
# 구분하기 위해 함수 이름을 표기할 때 괄호를
# 함께 사용하는 표기법 관행을 따른다.
# :::

# ## 모음 자료형

# **모음**<font size="2">collection</font> 자료형은
# 여러 개의 값을 하나로 묶어 놓은 값의 유형이다.
# 파이썬은 문자열, 리스트, 튜플, 집합, 사전 등의 모음 자료형을
# 기본으로 제공하며,
# 여러 값을 묶어 둔다는 의미로 모음 자료형의 값을
# **컨테이너**<font size="2">container</font>라고도 부른다.
# 
# 모음 자료형은 크게 두 종류로 나뉜다.
# 
# - 순차형<font size="2">sequence type</font>: 포함된 항목들의 순서를 가리는 모음 자료형
#     - 문자열
#     - 리스트
#     - 튜플
# - 집합형<font size="2">set type</font>: 포함된 항목들의 순서를 무시하는 모음 자료형
#     - 집합
#     - 사전

# ### 문자열

# **문자열**<font size="2">string</font>은 문자 기호로 이루어진 단어, 문장 등을 가리킨다.
# 키보드에 포함된 영문 알파벳, 한글 자음과 모음 등을 기본적으로 사용한다.
# 문자열은 세 가지 방식으로 작성될 수 있다.

# - 작은 따옴표 활용

# In[28]:


s = '잘 지내세요?'
s


# - 큰 따옴표 활용

# In[29]:


s = "무슨 일 있나요?"
s


# - 연속된 세 개의 작은 또는 큰 따옴표 활용: 여러 줄로 이루어진 문자열 작성

# In[30]:


s = '''안녕.
무슨 일 있어?'''

s


# In[31]:


s = """안녕.
무슨 일 있어?"""

s


# 스페이스와 탭을 활용해서 생성된 여백<font size="2">white space</font>도 문자열로 처리된다.
# 또한 줄바꿈을 나타내는 문자는 `\n`이다.

# In[32]:


s = '''안녕.
    무슨 일 있어?'''

s


# In[33]:


s = """안녕.
    무슨 일 있어?"""

s


# 문자열에 따옴표를 사용하려면 문자열을 감싸는 방식에 주의해야 한다.
# 예를 들어, 작은 따옴표를 사용하는 문자열을 다음과 같이 지정하면 오류가 발생한다.
# 
# ```python
# >>> 'Hi, what's up?'
# ------------------------------------------------------------
# File "<ipython console>", line 1
# 'Hi, what's up?'
#        ^
# SyntaxError invalid syntax
# ```
# 
# 이유는 작은 따옴표로 문자열의 시작을 지정했기 때문에
# `what's` 문장에 사용된 작은 따옴표가 
# 문자열의 끝을 의미하게된다.
# 그런데 이후에도 문자열이 이어지게 되어 결국 문자열의 끝이 불분명해져서
# 구문 오류를 뜻하는 `SyntaxError`가 발생하였다.
# 
# 이런 오류를 방지하는 다양한 방식이 존재한다.
# 예를 들어 작은 따옴표 바로 앞에 슬래시 기호 (`\`)를 추가하면 된다.

# In[34]:


s = 'Hi, what\'s up?'
s


# 아니면 문자열을 큰 따옴표로 감싸면 혼란이 사라진다.

# In[35]:


s = "Hi, what\'s up?"
s


# 하지만 이 방식은 문자열이 작은 따옴표와 큰 따옴표 모두 포함하는 경우에 대해서는 
# 작동하지 않는다. 
# 따라서 앞서 언급한 슬래시 기호를 사용할 것을 추천한다.

# In[ ]:





# In[ ]:





# 슬래시 기호(&#x5C;)와 원화 기호(&#x20a9;)

# In[ ]:





# In[ ]:





# In[36]:


print(u'\U0001f604')


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

# ### 리스트

# 리스트<font size="2">list</font>는 여러 종류의 값을 순서지어 포함한다.
# 포함되는 항목의 개수에 제한이 없다.

# In[37]:


colors = ['red', 'blue', 'green', 'black', 'white']
type(colors)


# ### 인덱싱

# 순차형 컨테이너는 모두 정수를 이용하여 항목을 확인하고, 
# 경우에 따라 항목을 다른 값으로 변경하는
# **인덱싱**<font size="2">indexing</font> 기능을 갖는다.
# 
# 왼편에 위치한 항목으로부터 차례대로 0, 1, 2, ... 등의 
# **인덱스**<font size="2">index</font>를 다음과 같이 사용한다.

# In[38]:


colors[0]


# In[39]:


colors[1]


# In[40]:


colors[2]


# :::{admonition} 인덱스는 0부터 시작!
# :class: warning
# 
# 가장 왼편에 위치한 항목의 인덱스가 1이 아닌 0임에 주의해야 한다.
# 순차 자료형의 가장 왼편에 위치한 값으로부터 첫째, 둘째, 셋째 등으로 
# 언급하는 반면에 인덱스는 0, 1, 2 등으로 사용해야 해서 
# 익숙해질 때까지 시간이 조금 걸린다.
# 
# C 언어 계열의 언어를 비롯하여 자바, 자바스크립트 등 대부분의 
# 프로그래밍 언어가 0부터 인덱스를 시작한다.
# 반면에 포트란<font size="2">Fortran</font>, 매트랩 등
# 수치 계산 전용 프로그래밍 언어는 인덱스를 1부터 시작한다. 
# 
# 참고로 인덱스를 0부터 시작해야 하는 논리적 이유는 없다.
# 누군가 어떤 이유로 그렇게 정했고 나름 이유가 있었겠지만 
# 사용 면에서 보면 어떤 논리적인 장점도 없다.
# :::

# -1, -2, -3, ... 등 음의 정수를 인덱스로 사용하면 오른편에 위치한 항목부터 
# 차례대로 왼쪽으로 이동하면서 인덱싱을 실행할 수 있다.

# In[41]:


colors[-1]


# `colors` 변수가 가리키는 리스트에 5개의 문자열이 포함되어 있기 때문에
# 왼편에서 넷째, 오른편에 둘째 항목은 동일한 문자열이 된다.

# In[42]:


왼쪽에서셋째 = colors[3]
오른쪽에서둘째 = colors[-2]

왼쪽에서셋째 == 오른쪽에서둘째


# :::{admonition} 한글 변수 이름
# :class: warning
# 
# 한글을 변수와 함수의 이름으로 사용할 수도 있다. 
# 하지만 다른 버전 또는 타 언어와의 호환성 등의 문제가 발생할 수 있기에
# 아직은 일반적이지 않으며 추천되지 않는다.
# :::

# 포함된 항목의 개수를 벗어나는 인덱스는 오류를 유발한다.
# `colors` 리스트가 5개의 항목을 포함하기에 사용할 수 있는 인덱스는 
# 왼편에서 시작하는 경우엔 0부터 4까지이고
# 오른편에서 시작하면 -1부터 -5까지이다. 
# 
# 예를 들어 5를 인덱스로 사용하면 왼편에서 여섯째 항목을 확인하기 때문에
# 인덱스의 범위를 벗어난다.
# 따라서 `index out of range` 라는 설명과 함께 `IndexError`가 
# 다음과 같이 발생한다.
# 
# ```python
# >>> colors[5]
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-3-5976064932c2> in <module>
# ----> 1 colors[5]
# 
# IndexError: list index out of range
# ```

# ### 슬라이싱

# 인덱스의 구간을 지정하여 순차 자료형의 일부를 추출하는 것을
# **슬라이싱**<font size="2">slicing</font>이라 한다.
# 
# 예를 들어 `colors` 리스트의 둘째부터 넷째 까지의 항목으로
# 구성된 리스트를 생성하려면 다음과 같이 한다.

# In[43]:


colors[1:4]


# `[1:4]` 는 1번 인덱스, 즉 둘째부터 4번 인덱스 이전까지, 즉 3번 인덱스인 넷째 항목까지 
# 추출 대상으로 삼는다는 의미이다.

# 슬라이싱의 일반 형식은 다음과 같다.
# 
# ```python
# colors[시작:끝:보폭]
# ```
# 
# **시작**과 **끝**의 의 의미는 `colors[1:4]`의 경우에서 설명한 것과 동일하다.
# 반면에 **보폭**은 항목 추출법을 설명한다.
# 예를 들어 2를 보폭으로 사용하면
# 시작 인덱스로 부터 2씩 건너 뛰며 항목을 추출한다.
# `colors[1:4:2]`는 따라서 1번, 3번 두 개의 인덱스에 위치한 항목을 추출해서 
# 리스트를 생성한다.

# In[44]:


colors[1:4:2]


# 시작, 끝, 보폭 모두 생략될 수 있으며 각각에 대해 기본값이 사용된다.
# 
# - 시작의 기본값: 0
# - 끝의 기본값: 항목의 개수 + 1. 즉, 시작부터 끝까지.
# - 보폭의 기본값: 1

# In[45]:


colors[3:]


# In[46]:


colors[:3]


# In[47]:


colors[::2]


# ### 수정 가능성

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
