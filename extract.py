import sys
import os
import zipfile
import shutil
import json


case = 'datumaro'
folder_name = '//result//'

def json_extract(z, json_dir):
    nm = z[:-4]
    n = nm.split('_')
    rename = n[1] + '_' + n[3].upper() + '_' + n[5].split('-')[0] + '.json'
    if not os.path.exists(json_dir + folder_name):
        os.makedirs(json_dir + folder_name)
    with zipfile.ZipFile(os.path.join(json_dir, z), 'r') as zip:
        if case == 'datumaro':
            json_name = 'dataset/annotations/default.json'
        if case == 'coco':
            json_name = 'annotations/instances_default.json'
        zip.extract(json_name, json_dir)
        shutil.move(os.path.join(json_dir, json_name), json_dir + folder_name + rename)


def jy(json_dir):
    path = json_dir + folder_name
    if not os.path.exists(os.path.join(json_dir, 'txt')):
        os.makedirs(os.path.join(json_dir, 'txt'))
    # json 파일 경로 리스트에 저장
    file_list = os.listdir(path)
    file_list_json = [file for file in file_list if file.endswith(".json")]

    # json 파일 전체 탐색
    for i in range(len(file_list_json)):

        # json 파일 로드
        file_path = os.path.join(path, file_list_json[i])
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
                            bbox_str = str(t['bbox'])
                            bbox_str = bbox_str.replace("[", "")
                            bbox_str = bbox_str.replace("]", "")

                            with open(os.path.join(json_dir, 'txt', filename), 'w') as f:
                                f.write('')

                            # e['id'] : Image name, t['bbox'] : bounding box 좌표
                            f = open(os.path.join(json_dir, 'txt', filename), 'a')

                            # yolov5 annotation 형식에 맞추어 재설정
                            data = str(t['id']) + ' ,' + bbox_str + '\n'
                            data = data.replace(',', "")
                            f.write(data)


def main():
    # image_dir = input('이미지 폴더의 주소: ')
    json_dir = input('json 폴더의 주소: ')

    zip_list = os.listdir(json_dir)
    len_cnt = 0

    # 압축풀기
    for z in zip_list:
        if 'zip' in z and 'task' in z:
            json_extract(z, json_dir)
            len_cnt += 1

    if os.path.exists(json_dir + '//dataset'):
        shutil.rmtree(json_dir + '//dataset')
    print('총 ' + str(len_cnt) + '개 완료')

    jy(json_dir)


if __name__ == '__main__':
    main()
