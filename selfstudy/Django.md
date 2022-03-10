# Django

__Framework Architecture__

- MVC Design Pattern (model-view-controller)
- 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
- Django는 MTV Pattren이라고 함
  -  Model
    - 응용프로그램의 데이타 구조를 정의하고 데이터베이스의 기록을 관리
  - Template
    - 파일의 구조나 레이아웃을 정의
    - 실제 내용을 보여주는데 사용
  - View 
    - HTTP 요청을 수신하고 HTTP 응답을 반환
    - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
    - template에게 응답의 서식 설정을 맡김

__가상환경 생성 및 활성화__

`python -m venv venv`

`source venv/Scripts/activate`

__깃으로 관리할 때 venv말고 이걸로 만든 파일을 올린다__

`pip freeze > requirements.txt`

---

### Template

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- Django Template Language(DTL)
  - Django template에서 사용하는 built-in system
  - 단순히 python이 html에 포함된 것이 아니며
    프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- __DTL Syntax__
  - Variable
    - render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것
    - `.`를 사용하여 변수 속성에 접근할 수 있음
    - render()의  세번째 인자로 {'key': value}전달

---

### HTML Form

- 웹에서 사용자 정보를 입력하는 여러 방식을 제공하고 사용자로부터 입력받은 데이터를 서버로 전송하는 역할을 담당
- 핵심속성
  - action: 입력 데이터가 전송될 URL 지정
  - method: 입력 데이터 전달 방식 지정
- input element
  - 사용자로부터 데이터를 입력 받기 위해 사용
  - type 속성에 따라 동작 방식이 달라짐
  - 핵심속성
    - name
    - 중복가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
    - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터로 전달
- label element
  - 사용자 인터페이스 항목에 대한 설명을 나타냄
  - label에는 input의 id와 동일한 값의 for속성 필요
- HTTP request method - "GET"
  - 서버로부터 정보를 조회하는 데 사용
  - 데이터를 가져올 때만 사용
  - 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송
- POST사용할 때는 `{% csrf_token %}` 무조건 작성

---

### URL

- Variable Routing
  - URL 주소를 변수로 사용하는 것
  - URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
  - `<타입:변수명>` 기본형태

---

### Namesapce

URL은 app_name으로 관리

templates는 임의의 폴더하나 더 끼워넣기

---

### MODEL

- 단일한 데이터에 대한 정보를 가짐
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- django는 model을 통해 데이터에 접속하고 관리
- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨
- 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구

__데이터베이스__

- 체계화된 데이터의 모임

__쿼리__

- 데이터를 조회하기 위한 명령어

- 조건에 맞는 데이터를 추출하거나 조작하는 명령어
- Query를 날린다 =>DB를 조작한다.

__스키마__

- 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조

__테이블__

- 열: 필드or 속성(데이터 형식이 지정)
- 행: 레코드 or 튜플(실제 데이터)

__PK__

- 각 행의 고유값으로 Primary KEY로 불린다.
- 반드시 설정하여야하며, 데이터베이스 관리 및 관계설정시 주요하게 활용
- 장고에선 id를 PK로 설정

__ORM__

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에
   데이터를 변환하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터 베이스와 객체 지향 프로그래밍 언어간의
   호환되지 않는 데이터를 변환하는 프로그래밍 기법

- 장점
  -  SQL을 잘 알지 못해도 DB조작 가능
  - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
- 단점
  - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음

`CharField` 

- 길이의 제한이 있는 문자열을 넣을 때 사용

- max_length가 필수 인자(필드의 최대길이)

`TextField`

- 글자의 수가 많을 때 사용
- max_length 옵션 작성시 자동 양식 필드인 textarea위젯에 반영은 되지만 
  모델과 데이터베이스 수준에는 적용되지 않음

`models.DateTimeField(auto_now_add=True)`

- 데이터가 생성될 때 시간을 자동으로 저장

`models.DateTimeField(auto_now=True)`

- 현재 시간을 자동으로 저장

---

### Migrations

- django가 model에 생긴 변화를 반영하는 방법
- 명령어
  - `makemigrations`
    - model을 변경한 것에 기반한 새로운 마이그레이션(설계도)을 만들 때 사용
  - `migrate`
    - 마이그레이션을 DB에 반영하기 위해 사용
    - 설계도를 실제 DB에 반영하는 과정
    - 모델에서의 변경사항들과 DB의 스키마가 동기화를 이룸
    - __테이블 이름규칙 = 앱이름_클래스명__
  - `sqlmigrate`
    - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
    - 마이그레이션이 SQL문으로 어떻게 해석되어서 동작할지 미리 확인 가능
    - `python manage.py sqlmigrate 앱이름 설계도번호`
  - `showmigrations`
  - 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
  - 마이그레이션 파일들이 migrate 되었는지 여부를 확인 가능

---

### DB API

- DB를 조작하기 위한 도구
- 장고가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- Model을 만들면 장고는 객체들을 만들고 읽고 수정하고 지울 수 있는
   database-abstract API를 자동으로 만듦

__DB API 구문__

`class Name.objects.QuerySet API`

---

### CRUD

- __CREATE__ 
  - 인스턴스를 생성
    - `std =Student(name='lee', nick_name='so-reyong',gitlab='dragon_lee', major='actor', mbti='INFP', phone='010-9999-6666', age=30)`
  - objects의 create 사용
    - `Student.objects.create(name='son', nick_name='world class', gitlab='tot', major= 'soccer player', mbti='ESFJ', phone='010-1212-3434', age=30)`

- CREATE 관련 메서드
  - `save()`
    - 객체를 데이터베이스에 저장함
    - 데이터 생성시 save()를 호출하기 전에는 객체의 ID 값이 무엇인지 알 수 없음
    - 단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save()가 필요
  - `__str__`
    - 매직 메소드인 str()을 재정의 하여 각각의 object가 사람이 읽을 수 있는 문자열을 반환하도록 한다.

- __READ__
  - `all()`
    - 현재 QuerySet의 복사본을 반환
  - `get()`
    - 주어진 lookup 매개변수와 일치하는 객체를 반환
    - 객체를 찾을 수 없으면 DoesNotExist
    - `from django.shortcuts import get_object_or_404`
      - 객체를 찾을 수 없으면 404페이지를 띄워줌
  - `filter()`
    - 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
    - 객체 찾을 수 없으면 빈 쿼리셋을 반환
- __UPDATE__
  - DB에서 수정할 data를 가져온다.
  - 가져온 데이터의 값을 변경한다.
  - save()한다.
- `delete()`

---

### Admin

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- Model class를 admin.py에 등록하고 관리
- django.contrib.auth 모듈에서 제공됨
- record 생성 여부 확인에 매우 유용하며, 직접 record를 삽입할 수도 있음

 ` python manage.py createsuperuser`로 아이디 비밀번호 생성

- admin.py에 아래와 같이 작성하여 모델을 등록

```python
from .models import Student
admin.site.register(Student)
```

---

### 



















































































