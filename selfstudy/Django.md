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
- DTL Syntax
  - Variable
    - render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것
    - `.`를 사용하여 변수 속성에 접근할 수 있음
    - render()의  세번째 인자로 {'key': value}