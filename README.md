# OpenKiosk(2019년이전 이름 : KioskAnyone)
### Leizy_Lee 그냥 해보는 프로젝트

외부 환경에서 파이썬2, 3버전이 *동시에 존재할때* 3 pip 쓰는 방법  
python3 -m pip install --upgrade pip  
  
Django에서 mysql.h가 없을 때 mysqlclient 설치 방법  
python -m pip install --only-binary :all: mysqlclient  
  
* 사용한 모듈
  * tkinter
  * pymysql
  
  
  
## 2018-09-28
- GUI를 대폭 수정
- 기존에 Text 파일에서 불러오는 데이터를 DB로 수정
- 코드 최적화

## 2018-11-09 
- GUI 결제창 개선
- DB 종료시 나타나는 에러 개선
- 기존에 1개의 메뉴만 고르는 프로그램에서 N개의 메뉴로 확장




## 2019-03-12
- GUI 코드 다시 작성함
- 다시 다 갈아엎음

## 2019-04-14
- GUI 클래스로 덮어 쓰는중
- 구글 API를 이용해서 음성인식을 통한 메뉴 검색 모듈을 만듦
- DB 접근과 DB 관리 모듈을 새롭게 만들어 이제 불러오기 뿐만 아닌 수정까지 가능함(물론 아직은 본 프로젝트 한정)  이 모듈은 나중에 따로 저장소를 
