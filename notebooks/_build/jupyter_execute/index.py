#!/usr/bin/env python
# coding: utf-8

# # 데이터 과학과 파이썬

# **감사의 말**: [SciPy Lecture Notes](https://scipy-lectures.org/_downloads/ScipyLectures-simple.pdf)의 1장 내용을 많이 참고합니다. 

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

# 매트랩과 R은 수치계산 또는 통계 분석에 특화된 프로그래밍 언어이다.
# 반면에 파이썬은 모든 영역의 문제를 해결하는 데에 사용되는 
# 범용<font size="2">universal</font> 프로그래밍 언어이다.
# 데이터 과학용으로 파이썬을 사용할 때 사용되는 기본 구성요소는 다음과 같다.

# **파이썬 기본 패키지**
# 
# - 파이썬 프로그래밍 언어 기본: 변수, 표현식, 함수, 클래스, 모듈, 명령문 등등
# - 기본 자료구조: 정수(`int`), 부동소수점(`float`), 문자열(`string`), 
#     리스트(`list`), 튜플(`tuple`), 사전(`dict`), 집합(`set`) 등등
# - 웹 프로그래밍, 계산 과학 등 다양한 분야에 특화된 모듈 및 라이브러리
# - 테스트 자동화, 문서 생성 등의 개발툴

# **NumPy(넘파이) 패키지**
# 
# - 수치 계산 전용 라이브러리, 특히 행렬 연산에 효율적임. 
# - 참고: [http://www.numpy.org/](http://www.numpy.org/)

# **Scipy(싸이파이) 패키지**
# 
# - 최적화<font size="2">optimization</font>, 
# 회귀 분석<font size="2">regression analysis</font>, 
# 보간법<font size="2">interpolation</font> 등등과 관련된 고수준 라이브러리
# - 참고: [http://www.scipy.org/](http://www.scipy.org/)

# **Matplotlib(맷플롯립) 패키지**
# 
# - 2D 시각화
# - 참고: [http://matplotlib.org/](http://matplotlib.org/)
#     <br>
# 
# <div align="center"><img src="https://github.com/codingalzi/pyfast/blob/master/notebooks/images/random_c.jpg?raw=true" width="60%"></div>

# **대화식<font size="2">interactive</font> 개발환경**
# 
# * **IPython**: 개선된 파이썬 콘솔([http://ipython.org/](http://ipython.org/))
#     <br>
# 
#     <div align="center"><img src="https://github.com/codingalzi/pyfast/blob/master/notebooks/images/snapshot_ipython.png?raw=true" width="50%"></div>

# * **Jupyter notebooks**: 웹 브라우저 활용 파이썬 프로그래밍 인터페이스([http://jupyter.org/](http://jupyter.org/))
#     <br>
# 
#     <div align="center"><img src="https://jupyter.org/assets/homepage/jupyterpreview.webp" width="50%"></div>

# **도메인 특화 패키지**

# * **pandas**, **statsmodels**, **seaborn**: 통계

# * **sympy**: 기호 계산<font size="2">symbolic computing</font>

# * **scikit-image**: 이미지 처리

# * **scikit-learn**: 머신러닝

# * **tensorflow**, **pytorch**: 딥러닝

# * **mayavi**: 3D 시각화
# 
#     <div align="center"><img src="https://github.com/codingalzi/pyfast/blob/master/notebooks/images/example_surface_from_irregular_data.jpg?raw=true" width="50%"></div>

# ## 데이터 과학용 파이썬 설치 및 개발환경

# ### 파이썬 설치

# 앞서 언급된 라이브러리 중에 mayavi를 제외한 모든 것을
# 한 번에 설치하는 패키지로 **아나콘다**<font size="2">Anaconda</font>를 추천한다.

# ### 개발 환경

# **대화식 프로그래밍**
# 
# 간단한 파이썬 코딩 설명을 위해서 대화식 프로그래밍<font size="2">interactive programming</font>을
# 지원하는 
# 주피터 노트북<font size="2">Jupyter notebook</font>을 기본적으로 사용한다.
# 주피터 노트북은 IPython 콘솔<font size="2">console</font>을 포함한다.
# 
# 
# ```python
# In [1]: print('Hello world')
# Hello world
# ```

# :::{admonition} 아나콘다 설치와 주피터 노트북 사용법
# :class: tip
# 
# [나도코딩의 동영상](https://www.youtube.com/watch?v=dJfq-eCi7KI&t=2298s)에서 아나콘다의 설치 과정과
# 주피터 노트북의 기초 사용법에 대한 상세한 설명을 들을 수 있다.
# :::
# 

# **IDE(통합 개발 환경)**

# 보다 복잡한 파이썬 코딩을 위해서는 코드 편집과 실행, 디버깅 등 
# 프로그래밍 관련 모든 작업을 통합해서 지원하는 
# 통합 개발 환경을 사용한다.
# 
# 일명 **IDE**<font size="2">Interactive Development Environment</font>라고 불리는
# 통합 개발 환경을 지원하는 다양한 툴이 존재하며, 
# 대표적으로 다음과 같다.
# 
# * [Spyder](https://www.spyderide.org/): 아나콘다 패키지에 포함되어 있다.
# * [PyCharm](https://www.jetbrains.com/pycharm): 가장 인기있는 상용 프로그램이다.
#     Pro 와 Community 두 버전을 지원하며 무료 버전인 Community 만으로도 입문용으로 충분하다.
# * [Visual Studio Code](https://code.visualstudio.com/docs/languages/python): 
#     마이크로소프트에서 지원하며, 현재 가장 인기 있는 무료 프로그램이다. 
#     파이썬 뿐만 아니라 거의 모든 프로그래밍 언어를 위한 통합 개발 환경을 지원한다.
# * [Atom](https://atom.io): 소스코드 저장소로 가장 유명한 
#     [GitHub](https://github.com/)에서 개발한 IDE. 
#     Visual Studio Code 처럼 거의 모든 프로그래밍 언어를 지원한다.

# 여기서는 일명 **VS Code**라 불리는 
# 비주얼 스튜디오 코드<font size="2">Visual Studio Code</font>를 사용할 것을 추천한다.

# :::{admonition} VS Code 설치와 사용법
# :class: tip
# 
# [생활코딩의 동영상](https://www.youtube.com/watch?v=K8qVH8V0VvY&t=337s)에서 
# VS Code의 설치와 사용법에 대한 상세한 설명을 들을 수 있다.
# :::
# 

# :::{prf:example}
# :label: my_file
# 
# 아래 내용을 담은 *my_file.py* 파일을 작성하고 저장하라.
# 여기서는 *codes* 라는 하위 디렉터리(폴더)에 저장되어 있다고 가정한다.
# 
# ```
# s = 'Hello world'
# print(s)
# ```
# 
# 이제 주피터 노트북의 코드 셀에서 아래 명령문을 실행해보자.
# 
# ```python
# In [1]: %run codes/my_file.py
# 파이썬 안녕
# ```
# 
# `%run my_file.py`은 IPython에서 *my_file.py* 파일에 포함된 모든 코드를 실행한다.
# 그리고 이제는 코드에서 정의된 변수와 변수가 가리키는 값을 확인할 수 있다.
# 
# ```python
# In [2]: s
# Out[2]: 'Hello world'
# ```
# 
# `%whos`는 선언된 변수에 대한 정보를 보여준다.
# 여기서는 변수 `s`는 `'파이썬 안녕'` 이라는 문자열(`str`)을 가리키고 있음을 확인해준다. 
# 
# ```python
# In [3]: %whos
# Variable   Type    Data/Info
# ----------------------------
# s          str     파이썬 안녕
# ```
# :::

# :::{admonition} 매직 커맨드
# :class: info
# 
# 퍼센트 기호 `%`로 시작하는 명령어는 파이썬 명령어가 아니며,
# 파이썬 코드 파일 및 디렉터리 경로 관리 등에 사용하는 IPython 전용 명령어이다.
# **매직 커맨드**<font size="2">magic command</font>라 불리며,
# 앞으로 기회될 때마다 하나씩 소개될 것이다.
# 매직 커맨드에 자세한 정보는 [IPython 공식 문서](https://ipython.readthedocs.io/en/stable/interactive/magics.html)에서 확인할 수 있다.
# :::
