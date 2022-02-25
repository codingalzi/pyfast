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

# ## 파이썬의 기본 자료형

# 정수, 부동소수점, 부울값 등 세 종류의 **스칼라**<font size="2">scalar</font> 
# 자료형을 기본으로 제공한다.

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


# ## 연산자

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


# 나눗셈의 몫이 정수인 경우엔 차이를 두지 않는다.

# In[27]:


(4 / 2) == (4 // 2)


# :::{admonition} 형변환 함수
# :class: info
# 
# `2.3 + 3`을 실행하면 파이썬 해석기<font size="2">interpreter</font>는
# 내부적으로 정수를 부동소수점으로 형변환하는 함수 `float()`를 이용하여
# 정수 `3`을 부동소수점 `3.0`으로 유형을 변환한 후에
# 덧셈을 처리한다. 
# 이렇게 값의 유형을 적절하게 자동 변환하는 기능을 
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
# 여기서는 자료형과 함수 이름을 구분하기 위해 
# 함수는 `int()`, `float()`, `str()`, `list()` 등처럼
# 함수 이름과 괄호를 함께 사용하는 표기법 관행을 따른다.
# :::
