# PJT Final

## 🔔 목표

➕ 영화 정보 기반 추천 서비스 구성

➕ 커뮤니티 서비스 구성

➕ HTML, CSS, JS, DB 등을 활용한 실제 서비스 설계



## ✍ 시작하기 전 구상

📄 `FE : 박지유 (JS)`    `BE : 장세영 (Django)`

📄 `소통 수단 : Notion`

📄 `ERD : erdcloud`

📄 `DB Seeding`  영화 정보를 엑셀로 받은 뒤에 Json 파일로 변환 후 PJT에 적용 예정



## 📜 타임라인

#### 1117

##### FE

- 디자인 상황

1. http://127.0.0.1:8000/movies/

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1054f7df-a663-4759-8a22-cc57e1029cfd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211125T011913Z&X-Amz-Expires=86400&X-Amz-Signature=c1e92cbd101b764448e39cf1362137d030b04f0467804553cd270652563e3617&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

1. http://127.0.0.1:8000/community/

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/91893940-8e72-48d1-88f4-1c3879fef6d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211125T011923Z&X-Amz-Expires=86400&X-Amz-Signature=779c83f8f58efdb21dbc2a91438d918c49913616c51f3a1957c8e38624d7be3f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

1. http://127.0.0.1:8000/community/create/

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ce2b1155-fb02-4656-bc11-f1144551ac1c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211125T011934Z&X-Amz-Expires=86400&X-Amz-Signature=29c89370c9ef71aa7d4df919f6ad7be6ff7caa289be42650d4bacadc59b3c377&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 배경색, 버튼, 네이게이션바 등 기본 틀을 구성
- 영화 DB를 받아온 후 캐러셀(Carousel)로 구성할 예정
- 커뮤니티와 게시글 제작 배치 변경 필요



##### BE

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

##### FE

- 디자인 상황

1. http://127.0.0.1:8000/movies/

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/dbaef17e-fdd6-4a83-84e0-d7317e250664/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211125T012102Z&X-Amz-Expires=86400&X-Amz-Signature=cc81b3d428cee1e915b31312e4b2af3735bcfb8f6b3d17ae37c97e25d272648c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

1. http://127.0.0.1:8000/community/

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7f8fbe18-27c6-4318-a21d-150e58cf749a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211125T012114Z&X-Amz-Expires=86400&X-Amz-Signature=741df5abdf065b7d12760045dcc4137aa82faab34b6b120663b212c5f8ecde8e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

1. http://127.0.0.1:8000/community/pk/

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9e075ce7-8882-4345-b78a-4f6c16aaa8f7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211125T012123Z&X-Amz-Expires=86400&X-Amz-Signature=85c3f04428065d8513c5d5c230b1de1a841111a8e5909103f50bf4b6a960f24d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- Navbar에 있던 계정 관련 기능을 Dropdown으로 구현
- Modal 기능을 활용해 Login기능을 구현(Navbar를 통해서 사용)
- 배치를 좀 더 다듬었음
- 내일 DB를 추가한 후 캐러셀 구상해야함
- 커뮤니티 내용과 영화리스트에 Pagination을 구현해야함
- 회원가입, 계정정보 수정 폼을 수정해야함



##### BE

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

##### FE

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/29ff034b-4c21-4a64-9a46-c2efe9e7aaaf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211125T012147Z&X-Amz-Expires=86400&X-Amz-Signature=45fa890a31a2881ecddb0ce7076db1ea216f57960e84e4c5c8f8c55f017b50d6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 캐러셀을 구현함
- 순위를 표현하기 위해 views.py에서 일일이 변수로 지정해 순위를 표현함
- 영화리스트와 영화 상세페이지를 더 꾸며야 함



##### BE

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

##### FE

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/254086a5-bfe6-4460-975b-1e212015a976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211125T012412Z&X-Amz-Expires=86400&X-Amz-Signature=50d880ffe0096ff11ff38691e975fafd0374ef43a24ff17424981749decd82a1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- TOP10 페이지에 리스트로도 추가
- 영화 리스트에도 캐러셀 구현

- 커뮤니티 작성 페이지 구성 변경



##### BE

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



#### 1121

##### FE

- 프로필 페이지 구성 수정
- 프로젝트 시작페이지를 부트스트랩 캐러셀로 구성하려했으나 실패함



##### BE

- Apps

  ```markdown
  # movies
  
  - 혼동 방지 차원에서 comment -> review로 변경
  - 리뷰평점이 안뜨던 문제 해결
  ```



#### 1122

##### FE

- 프로젝트 시작페이지를 캐러셀로 구성
- 팔로우, 좋아요, 회원정보 수정, 비밀번호 변경 페이지 버튼을 한글 및 골드버튼으로 구성



##### BE

```markdown
# accounts
- 회원탈퇴 파트 오탈자 수정
- templates / views
profile -> 팔로우 기능 JS로 구현
# community
- templates / views
likes -> 좋아요 기능 JS로 구현
pagination 추가
# movies
- genres 숫자로 저장돼 있던 부분 한글로 치환
- templates / views
pagination 추가
```

- 댓글작성 기능도 JS로 구현해보려 했는데 생각 이상으로 감이 잘 안잡힌다...
- 영화를 조건에 맞추어 정렬할 때, 순위값을 어떻게 넘길지 고민해봐야 할 것 같다.



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

