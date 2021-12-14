import os
import zipfile
import shutil
import json


case = 'coco'
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


def jy():
    # json 파일 경로 지정
    path = input("Input path: ")

    # json 파일 경로 리스트에 저장
    file_list = os.listdir(path)
    file_list_json = [file for file in file_list if file.endswith(".json")]

    trn_img = []

    # json 파일 전체 탐색
    for i in range(len(file_list_json)):
        img_name = []

        # json 파일 로드
        file_path =  path + "\\" + file_list_json[i]
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            
            
            # 라벨링이 있는 이미지 파일 명 저장
            for e in data['images']:
                for f in data['annotations']:
                    if e['id'] == f['image_id']:
                        if f['segmentation'] != []:
                            img_name.append(e['file_name'])
            img_name = set(img_name)
            
        trn_img.extend(img_name)
    
    # 해당 이미지 분리: 총 16031     
    print(len(trn_img))


def main():
    # image_dir = input('압축 이미지 폴더의 주소: ')
    json_dir = input('압축 json 폴더의 주소: ')

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

    jy()


if __name__ == '__main__':
    main()