#!/usr/bin/env python
# coding: utf-8

# # 컴퓨터 과학과 파이썬

# 데이터 분석, 수치계산 등 컴퓨터 과학의 핵심은 **문제해결을 위한 컴퓨터 활용**이다. 
# 여기서는 컴퓨터를 이용한 문제 해결 분야에서 
# 가장 중요하게 활용되는 파이썬 프로그래밍의 기초를 전달한다. 

# ## 컴퓨터 과학

# 컴퓨터 과학이 단순히 컴퓨터에 대한 연구를 의미하지는 않는다.
# 컴퓨터 과학자는 주어진 문제를 해결하는 **알고리즘**<font size="2">algorithm</font>을 개발한다.
# 여기서 알고리즘은 주어진 문제<font size="2">problem</font>의 
# 모든 사례<font size="2">instance</font>를 일괄적으로 해결하는 
# **단계별 명령의 목록**이다.
# 
# 반면에 (여기서 자세히 설명하지 않겠지만) 컴퓨터로 해결이 불가능한 문제도 존재한다. 
# 따라서 컴퓨터 과학은 문제해결책뿐만 아니라,
# 해결책이 존재하지 않는 문제에 대한 연구도 포함한다. 
# 해결이 가능한 문제를 **계산 가능한**<font size="2">computable</font> 문제라고 말한다.
# 특정 컴퓨터나 특정 프로그래밍언어에 의존하는 해결책이 아니라
# 어느 정도의 기본만 갖추고 있는 컴퓨터나 프로그래밍언어를 이용하면
# 해결할 수 있는 문제를 의미함에 주의해야 한다. 

# ## 프로그래밍과 알고리즘

# (컴퓨터) **프로그래밍**은 특정 프로그래밍 언어를 이용하여 컴퓨터에서 실행 가능한 
# 프로그램으로 작성하는 과정이다. 
# 컴퓨터 과학이 프로그래밍에 대한 연구는 아니다.
# 하지만 프로그래밍은 컴퓨터 과학자의 주요 활동 중 하나이다. 
# 문제 해결을 위한 **알고리즘**은 
# 문제의 사례들을 표현하는 데에 필요한 데이터<font size="2">data</font>와
# 의도한 결과를 생성하는 데 필요한 과정<font size="2">step</font>을 묘사한다.

# 주어진 문제를 해결하려면 
# **API**<font size="2">Application Programming Interface</font>를
# 조합해야 한다.
# 경우에 따라 필요한 API를 직접 구현해야 하지만,
# 사용자 입장에서는 일반적으로 필요한 API의 기능과 활용법을 익히는 것에 집중해야 한다.
# 이런 의미에서 컴퓨터 과학을 **추상화**<font size="2">abstraction</font>에 대한 연구라 부르기도 한다.
# 
# 예를 들어, 제곱근을 계산하는 함수 `sqrt()`는 `math` 모듈에 정의되어 있으며 아래와 같이 활용한다.

# In[1]:


import math

math.sqrt(16)


# 위 코드는 **절차적 추상화**<font size="2">procedural abstraction</font>를 보여준다. 
# 즉, `sqrt()` 함수가 어떻게 정의되었는가는 전혀 중요하지 않다.
# 대신 제곱근을 계산하는 함수라는 사실과 어떻게 활용하는가를 알기만 하면 된다.
# 이런 의미에서 함수를 아래 그림에서처럼 **블랙박스**로 이해할 수 있다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/pythonds01-Introduction/Figures/blackbox.png" width="50%"></div>

# ## 파이썬 프로그래밍 언어

# 문제 해결을 위한 절차와 명령 등을 작성하기 위해 사용되는 언어를 프로그래밍 언어라 한다. 
# 파이썽, C, C++, C#, 자바, 자바스크립트, OCaml, Haskell 등 다양한 종류의 프로그래밍 언어가 존재한다.
# 
# 파이썬은 객체지향 프로그래밍(OOP) 언어이며
# 다양하며 중요한 자료형을 기본적으로 제공한다. 
# 또한 다른 언어에 비교해서 보다 쉽게 프로그램을 작성할 수 있는 프로그래밍의 기본 요소를 제공한다. 

# ### 필수 구성요소

# 파이썬을 비롯한 대부분의 프로그래밍 언어의 필수 구성요소는 다음과 같다.
# 
# - 값 저장 및 변경
# - `if ... else ...` 등의 조건문
# - `for`, `while` 반복문
# - 순차적 실행

# ### 기본 자료형

# 대부분의 프로그래밍언어는 아래 데이터에 대한 자료형<font size="2">data type</font>과
# 관련 함수를 기본으로 제공한다.
# 
# - 정수<font size="2">integer</font>
# - 문자열<font size="2">string</font>
# - 부동소수점<font size="2">floating point</font>
# - 진리값<font size="2">boolean</font>
# 
# 언급된 자료형과 관련된 연산 함수는 예를 들어 사칙연산,  논리 연산자 등이 포함된다.
# 원칙적으로는 언급된 필수 구성요소와 기본 자료형만을 이용하여 모든 문제를 해결할 수 있다. 
# 하지만 복잡한 문제를 순전히 필수 구성요소와 기본 자료형만을 이용하여 해결하는 일은 매우
# 복잡하고 비효율적이다. 
# 따라서 알고리즘의 복잡도와 효율성을 높혀주는 방법과 도구가 요구된다. 

# ### 추상 자료형과 클래스

# 파이썬과 같은 객체지향 프로그래밍 언어는
# 특정 데이터 및 그 데이터와 관련된 성질 및 기능을 
# 하나로 묶어 **클래스**<font size="2">class</font>라는
# **추상 자료형**<font size="2">abstract data type(ADT)</font>으로
# 정의하는 기능을 제공한다. 
# 이와같이 추상 자료형을 정의하는 방식을 **데이터 추상화**라고 한다. 
# 
# 앞서 소개한 절차적 추상화의 경우처럼 사용자의 입장에서 데이터와 함수가 어떻게 구현되었는가는
# 중요하지 않다. 
# 대신에 해당 데이터가 무엇을 표현하며 관련 함수의 기능이 무엇인가만이 중요하다.
# 이런 의미에서 데이터 추상화를 **데이터 캡슐화**라고 부르기도 한다. 
# 
# 아래 그림에서 볼 수 있듯이 사용자는 **인터페이스**<font size="2">interface</font>에서 
# 제공하는 함수인 **메서드**<font size="2">method</font>를 통해 데이터를 활용하며,
# 데이터와 함수가 어떻게 구현되었는가는 알 필요 없다. 

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/algopy/master/notebooks/pythonds01-Introduction/Figures/adt.png" width="30%"></div>

# ### 자료구조와 데이터

# **자료구조**는 구현된 추상 자료형을 가리킨다. 
# 추상 자료형을 구현하는 방식이 다양하다. 
# 하지만 앞서 설명하였듯이 구현된 자료구조는 기본적으로 구현 방식과 무관하게
# 의도한 데이터와 함수의 기능을 제공하기만 하면 된다. 
# 그럼에도 불구하고 구현방식에 따른 알고리즘의 효율성에는 차이가 발생할 수 있다.
# 
# 파이썬과 같은 객체지향 프로그래밍언어는 클래스를 이용하여 추상 자료형을 정의하며,
# 해당 추상 자료형의 데이터는 지정된 클래스의 **객체**<font size="2">instance</font>다.
# 앞서 언급한 기본 자료형 이외에 파이썬이 제공하는 주요 추상 자료형은 다음과 같다.
# 
# - 리스트<font size="2">list</font>
# - 튜플<font size="2">tuple</font>
# - 집합<font size="2">set</font>
# - 사전<font size="2">dictionary</font>
# 
# 앞으로 다양한 추상 자료형의 성질과 활용법을 학습하면서 파이썬 프로그래밍의 기초를 다지게 된다.