# PJT Final

## 🔔 목표

➕ 영화 정보 기반 추천 서비스 구성

➕ 커뮤니티 서비스 구성

➕ HTML, CSS, JS, DB 등을 활용한 실제 서비스 설계



## ✍ 시작하기 전 구상

📄 `FE : JS`    `BE : Django`

📄 `ERD : erdcloud`

📄 `DB Seeding`  영화 정보를 엑셀로 받은 뒤에 Json 파일로 변환 후 PJT에 적용 예정



## 📜 타임라인

#### 1117

- Apps

  ````markdown
  # accounts	계정 인증 및 Follow / Like
  - templates
  signup / login / profile
  
  - forms
  CustomUserCreationForm 사용
  
  - models
  follow 기능에 ManyToManyField 사용 예정
  
  - urls / views
  signup / login / logout / profile / follow
  ````

  ```markdown
  # community	커뮤니티 서비스 제공용 App
  - templates
  index / form / detail (CRUD)
  
  - models
  Post 클래스 생성 ( 커뮤니티 글 게시용도 )
  
  - urls / views
  `community_`index / create / detail / update / delete
  ```

  ```markdown
  # movies	영화 정보 표시
  - templates
  index / detail / detail_review
  
  - models
  Movie, Comment 클래스 생성( 영화 정보와 그에 대한 평점 작성용 )
  
  - urls / views
  movie_index / movie_detail
  ```

  - 각 코드마다 주석 추가 필요
  - NoReverseMatchError 주의!

- 이전의 작업들에 익숙해져서 아무 생각없이 Vue연동에 필요한 코드를 작성해서 시간 순삭.... 시간 날리지 않게 좀 더 생각해보고 코드를 짤 필요가 있음.
- DB 시드는 영화진흥위원회에서 받아오려 했는데 엑셀 파일에 포스터 이미지 경로가 없어서 다른 방법이 있을 지 탐색 중
- 기본 뼈대만 만들어 놓은 뒤에 ERD 재작성 예정



#### 1118

- Apps

  ````markdown
  # accounts
  - templates
  change 추가
  
  - forms
  CustomUserChangeForm 추가
  
  - urls / views
  change / delete 추가
  ````

  ```markdown
  # community
  - models
  created_at, updated_at 추가
  
  - urls / views
  `community_`comment_create, comment_delete 추가
  ```

- 댓글을 수정할 수 있는 기능을 만들고 싶었는데... 하루를 다 투자해도 해결이 안됨. 추후에 더 고민해봐야 할 과제로..

- 회원정보수정 기능을 만들었는데, 코드 어딘가를 잘못 수정했는지 다시 또 동작을 안함. 다시 찾아볼 예정

- 회원탈퇴를 별도의 인증없이 가능하게 구현했고, 기본적인 기능들을 전부 완료하면 인증도 추가해보고 싶긴 하다.



### 1119

- Apps

  ```markdown
  # accounts
  - templates
  profile -> 프로필 이미지 업로드 추가
  
  - models
  커스텀 모델에 이미지 필드 추가
  
  - urls / views
  change -> request.FILES 추가
  ```

  ```markdown
  # community
  - templates
  form -> 게시글 내 이미지 업로드 추가
  
  - models
  이미지 필드 추가
  
  - urls / views
  `community_`index / create / detail / update / delete
  ```

  ```markdown
  # movies
  - fixtures
  TMDB API를 이용해 영화 데이터 추가
  
  - models
  영화 정보를 받아오기 위한 모델필드 조정
  ```

- 어제 서버를 킬 때는 문제가 없었는데 오늘 코드를 추가하는 도중에 프로필과 커뮤니티 댓글을 불러오는 부분에서 pk값을 인식하지 못하는 에러가 났었다. 문제를 찾아내는 데 시간이 꽤 오래 걸렸는데 이 경험을 기회 삼아 문제가 생겼을 때 정보가 이동하는 경로를 천천히 찾아보는 습관을 들여야 할 것 같다.



### 1120

- Apps

  ```markdown
  # accounts
  - templates
  signup -> 생년월일 양식 추가
  
  - models
  비밀번호 검증용 필드 추가
  ```

  ```markdown
  # community
  
  
  - templates
  detail -> 좋아요 버튼 추가
  
  - models
  필드 추가
  
  - urls / views
  `community_`likes
  ```

  ```markdown
  # movies
  - urls / views
  `movie_comment_`create / update / delete
  ```

- 어느 순간부터 회원가입이 안되는데 내일 날잡고 손을 봐야할 것 같다.

- 영화 Detail 항목에서 댓글 기능을 넣었는데 양식이 안떠서 추가적인 확인 필요



## 🎞 

### A. 

❔ 

💯 

```

```

✔ 

✔ 

✔ 이미지 주소를 바인딩으로 보내줄 때, 전체 URL로 보내줬어야 하는데, 관리자 모드에서 뜬  URL만으로 요청을 하려다가 이미지가 뜨지 않아 해결하는 데 애를 먹었다.





### B. 

❔ 

💯 

```

```

✔ 

✔  



### C. 

❔ 

💯 

```

```

✔ 



## 🔎 자가 진단

❕ 

❕ 공부를 하면서 JS에 비해 그래도 어느 정도는 감을 잡았다고 생각했는데, 터무니 없는 생각이였다는 것을 새삼 느꼈다.

❕ 



## 💾 추가 코드

```python

```

