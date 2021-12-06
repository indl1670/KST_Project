import sys
import os
import zipfile
import shutil


case = 'datumaro'
folder_name = '//result//'


def json_extract(z, json_dir):
    nm = z[:-4]
    print(nm)
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
    print('json 파일이 바탕화면의 ' + folder_name + ' 폴더 안의 result 폴더에 저장되었습니다.')


if __name__ == '__main__':
    main()
