### 데이터베이스

- 몇 개의 자료 파일을 조직적으로 통합하여 자료항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체

---

### 관계형 데이터베이스

- 키와 값들의 간단한 관계를 표 형태로 정리한 데이터베이스
- 스키마: 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술한 것
- 테이블: 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합
  - 각 열에는 고유한 데이터 형식이 지정됨
  - 행: 실제 데이터가 저장되는 형태
- 기본키(PK): 각 행의 고유 값

---

### RDBMS(관계형 데이터베이스 관리 시스템)

- Sqlite 데이터 타입
  - null
  - integer
  - real
  - text
  - blob( 별다른 타입 없이 그대로 저장)
- Type Affinity(데이터 타입 선호도)

---

### SQL

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 프로그래밍 언어

---

### CRUD

- CREATE
  - INSERT
    - 테이블에 단일 행 삽입
    - `INSERT INTO 테이블이름 (컬럽1,컬럼2,..) VALUES (값1, 값2,...);`
    - 모든 열에 데이터가 있는 경우 데이터 명시없이 바로 벨류 작성 가능

- READ
  - `SELECT 컬럼명 FROM 테이블명 WHERE 조건;`
    - 테이블에서 데이터를 조회 다양한 절과 함께 사용
    - LIMIT
      - 쿼리에서 반환되는 행 수 를 제한
      - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
    - WHERE
      - 쿼리에서 반환된 행에 대한 특정 __검색 조건__을 지정
    - SELECT DISTINCT
      - 조회 결과에서 중복 행을 제거
      - SELECT 바로 뒤에 작성
- DELETE
  - `DELETE FROM 테이블이름 WHERE 조건;`
  - AUTOINCREMENT
    - 테이블 생성단계에서 컬럼 속성에 추가해서 사용
    - SQlite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
    - 장고에서는 이걸 기본 값으로 사용

- UPDATE
  - 기존 행의 데이터를 수정
  - SET절에서 테이블의 각 열에 대해 새로운 값을 설정
  - `UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2,... WHERE 조건;`

---

### Aggregate Functions

- 집계함수
- 값 집합에 대한 계산을 수행하고 단일 값을 반환
- SELECT 구문에서만 사용됨
  - COUNT
  - AVG
  - MAX
  - MIN
  - SUM
  - `SELECT 함수명(컬럼) FROM 테이블이름;`

---

### LIKE

- 패턴 일치를 기반으로 데이터를 조회하는 방법
  - `%`
    - 0개 이상의 문자
    -  이자리에 문자열이 있을수도, 없을 수 도 있다.
  - `_`
    - 임의의 단일 문자
    - 반드시 이자리에 한 개의 문자가 존재해야 한다.
- ` SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';`

---

### ORDER BY

- 조회 결과 집합을 정렬
- SELECT문에 추가하여 사용
  - ASC - 오름차순(디폴트)
  - DESC - 내림차순
- `SELECT * FROM 테이블 ORDER BY 컬럼 ASC;`

---

### GROUP BY

- 행 집합에서 요약 행 집합을 만듦
- SELECT 문의 옵션절
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
- 문장에 WHERE절이 포함된 경우 반드시 WHERE절 뒤에 작성해야 함

- `SELECT 컬럼1, aggregate(컬럼2) FROM 테이블 GROUP BY 컬럼1,컬럼2;`

---

### ALTER TABLE

- 4가지 기능

  - table 이름 변경
    - `ALTER TABLE 기존이름 RENAME TO 바꿀이름;`

  - 테이블에 새로운 column 추가
    - ` ALTER TABLE 테이블명 ADD COLUMN 컬럼이름 컬럼타입;`

  - column 이름 수정
    - `ALTER TABLE 테이블명 RENAME COLUMN 기존컬럼명 TO 바꿀컬럼명;`
  - 컬럼 삭제
    - `ALTER TABLE 테이블명 DROP COLUMN 삭제할컬럼명;`


























































































