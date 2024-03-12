import requests
import json

# CVAT API의 주소와 접근을 위한 사용자 인증 정보
cvat_api_url = "http://cvat-instance.com/api/"

# 개인 api 토큰
api_token = "api 토큰"

#요청 헤더에 토큰 추가
headers = {
    'Authorization': f'Token {api_token}'
}

# 특정 작업에 대한 주석 데이터를 가져오는 API 엔드포인트
task_id = "1" #예시로 사용된 작업 id
annotations_url = f"{cvat_api_url}tasks/{task_id}/annotations"

# API를 통해 데이터 가져오기
response = requests.get(annotations_url, auth=auth)
if response.status_code == 200:
    annotations_data = response.json()

    #가져온 데이터를 db.json 파일에 저장
    with open("db.json", "w") as db_file:
        json.dump(annotations_data, db_file, indent=4)

else:
    print("데이터를 가져오는 데 실패했습니다. 상태 코드:", response.status_code)