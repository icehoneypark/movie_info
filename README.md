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

