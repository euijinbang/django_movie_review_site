# movies 구현

![movies](/Users/euijinpang/django_movie_review_site/README.assets/movies.jpg)

## 목표

- 데이터 생성, 조회, 수정, 삭제
- 데이터 조작
- ORM
- 관리자 페이지를 통한 데이터 관리
- Django ModelForm 활용한 HTML 과 사용자 요청 데이터 유효성 검증
- Authentication(사용자 인증) 에 대한 이해

## 키워드 
- CRUD 기본
- Forms
- Auth
- Admin
- Static

## 기능

1. 계정관리
   1. 회원가입
   2. 로그인
   3. 로그아웃
   4. 비밀번호 변경
   5. 회원탈퇴
2. 커뮤니티앱
   1. 신규 리뷰 생성
   2. 전체 리뷰 목록 조회
   3. 단일 리뷰 상세 조회
   4. 기존 리뷰 수정
   5. 단일 리뷰 삭제
3. 사용자 인증여부에 따른 네비게이션 변화
4. 어드민 페이지로 관리
5. 부트스트랩으로 꾸미기


## 상세정보
1. 계정관리 앱 (accounts)
   1. 회원가입 : 신규 사용자 생성
      - 이미 인증된 사용자가 요청을 보낸 경우 전체 리뷰 목록 페이지로 redirect
      - UserCreationForm 사용
      - HTTP method GET
        - 응답으로 signup.html 제공
        - form 작성정보는 POST 방식으로 제출
        - 회원가입 form 요소
        - 
      - HTTP method POST
        - 데이터 유효하면 전송된 데이터를 데이터베이스에 저장
        - 그 후 사용자를 인증(로그인)하고 전체 리뷰 목록 페이지로 redirect
        - 데이터가 유효하지 않다면 데이터를 작성하는 form을 에러메세지와 함께 표시
   2. 로그인 : 기존 사용자 인증
      - 인증되어있는 사용자는 전체 리뷰 목록 페이지로 redirect
      - AuthenticationForm 사용
      - HTTP method GET
        - 응답으로 login.html 제공
        - POST방식으로 form 제출
        - 로그인 form
        - 
      - HTTP method POST
        - 데이터 유효시 사용자 인증(로그인)
          - 로그인 하기 전 페이지 URL 이 함께 전송된 경우, 로그인 이후 해당 URL로 redirect
          - 이젠 페이지의 URL이 함께 전송되지 않았다면, 전체 리뷰 목록 조회 페이지로 redirect
   3. 로그아웃 : 인증된 사용자 해제
      - HTTP method 는 GET, POST 중 선택
      - 사용자 인증을 해제(로그아웃)하고 전체 리뷰 목록 페이지로 redirect
   4. 비밀번호 변경
   
2. 커뮤니티 앱 (community)
   1. 신규 리뷰 생성
      - 인증된 사용자만 새로운 리뷰 작성 가능
      - HTTP method GET
        - form.html 제공
        - 리뷰 작성할 form 표시
        - 
      - HTTP method POST
        - 데이터 유효시 데이터베이스에 저장하고 상세 조회 페이지로 redirect
        - 유효하지 않을시 데이터 작성 form 을 에러메세지와 함께 사용자 화면에 표시
   2. 전체 리뷰 목록 조회
      - index.html 
      - 제목 클릭시 해당 리뷰의 상세조회 페이지로 이동
   3. 단일 리뷰 상세 조회
      - detail.html
      - 리뷰데이터 없으면 404 에러페이지 표시
   4. 기존 리뷰 수정
      - 인증된 사용자만 리뷰수정 가능
      - HTTP method GET
        - 리뷰 수정 Form 표시
        - 
      - HTTP method POST
        - 데이터 유효시 데이터베이스 저장, 상세조회 페이지로 redirect
        - 데이터 미유효시 에러메세지 포함하여 다시 Form 표시
   5. 단일 리뷰 삭제
      - 삭제 완료시 전체 리뷰 목록 조회 페이지로 redirect

3. 인증 여부에 따른 화면 변화
   1. 네비게이션바 : 
      1. 사용자 인증여부 관계없이 전체 리뷰 목록 조회로 이동
      2. 사용자 미인증시 로그인과 회원가입 링크
      3. 사용자 인증시 새로운 리뷰작성 페이지 및 로그아웃 링크

4. 어드민 페이지 제작
   1. 관리자 페이지에서 Review, User 모델의 데이터 생성, 조회, 수정, 삭제 가능



## 모델

1. Review 모델
2. 사용자(User) 모델 : 장고 기본모델 사용

## Form

1. Review 모델의 데이터 검증, 저장, 에러메세지, HTML 관리 위해 ModelForm 사용
2. User 모델의 데이터 검증, 저장, 에러메세지, HTML 관리 위해 장고제공 ModelForm, Form 사용

## URL

app_name, name 사용

## View & Template

- 공유 템플릿 생성 및 사용













