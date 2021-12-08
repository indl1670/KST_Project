import json
import os

path = './result'

# json 파일 경로 리스트에 저장
file_list = os.listdir(path)
file_list_json = [file for file in file_list if file.endswith(".json")]

# json 파일 전체 탐색
for i in range(len(file_list_json)):

    # json 파일 로드
    file_path = 'result/' + file_list_json[i]
    with open(file_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        
        # 라벨링이 있는 경우
        for e in data['items']:
            if e['annotations'] != []:
                for t in e['annotations']:
                    # bounding box가 존재하는 경우
                    if t['type'] == 'bbox':
                        # 이미지 명으로 txt파일 생성
                        filename = e['id'] + '.txt'
                        
                        # 리스트를 str 형태로 변환하고, 가공
                        bbox_str = t["bbox"]
                        
                        # 가로 1920, 세로 1080
                        bbox_str[0] = float(bbox_str[0])/1920
                        bbox_str[1] = float(bbox_str[1])/1080
                        bbox_str[2] = float(bbox_str[2])/1920
                        bbox_str[3] = float(bbox_str[3])/1080
                        
                        bbox_str = str(bbox_str)
                        bbox_str = bbox_str.replace("[", "")
                        bbox_str = bbox_str.replace("]", "")
                            
                        # e['id'] : Image name, t['bbox'] : bounding box 좌표
                        f = open(filename, 'a')
                        data = str(t['id']) + ' ,' + bbox_str + '\n'
                        data = data.replace(',', "")
                        f.write(data)
