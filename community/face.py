import os
import sys
import requests

# 등록된 client_id, client_secret 정보를 입력합니다.
client_id = "nSNNt9Iyb9ef1PxjBLPF"
client_secret = "yjeOVJx1Qz"

# 얼굴 사진을 통한 나이 추정을 위해서는 아래 url을 사용합니다. (face: 얼굴 분석, celebrity: 닮은 유명인 찾기)
url = "https://openapi.naver.com/v1/vision/face" 

# 분석할 이미지의 파일명을 입력합니다.
files = {'image': open('iu.jpg', 'rb')}

# API 입력 설정
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

# API 사용
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code

if(rescode==200):
    # 결과물 출력
    print (response.text)
else:
    print("Error Code:" + rescode)