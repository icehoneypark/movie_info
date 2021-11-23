import os
import json
import requests

client_id = "nSNNt9Iyb9ef1PxjBLPF"
client_secret = "yjeOVJx1Qz"

url = "https://openapi.naver.com/v1/vision/face" 

files = {'image': open('#', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
result = json.loads(response.text)

if(rescode==200):
    # 결과물 출력
    print (response.text)
else:
    print("Error Code:" + rescode)