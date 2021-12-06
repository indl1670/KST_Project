import json
import os

path = './result'

# json 파일 경로 리스트에 저장
file_list = os.listdir(path)
file_list_json = [file for file in file_list if file.endswith(".json")]

# 삭제 요청 이미지가 있는 json 파일의 리스트 출력
print("Are They Delete File List?: ", file_list_json, '\n')
img_name = []

# json 파일 전체 탐색
for i in range(len(file_list_json)):

    # json 파일 이름 확인
    print("Json File name: ", file_list_json[i])

    # json 파일 로드
    file_path = 'result/' + file_list_json[i]
    with open(file_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)

        # 라벨링이 없는 경우 이미지파일의 이름 리스트에 추가
        for e in data['items']:
            if e['annotations'] != []:
                for t in e['annotations']:
                    if t['type'] == 'bbox':
                        img_name.append(e['id'] + '.jpg')

print(img_name)