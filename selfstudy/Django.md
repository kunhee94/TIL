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

---

### URL

- Variable Routing
  - URL 주소를 변수로 사용하는 것
  - URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
  - `<타입:변수명>` 기본형태



































































































