import os
import shutil

from sklearn.model_selection import train_test_split


def Numcheck(image_dir, json_dir):
    image_list = os.listdir(image_dir)
    json_list = os.listdir(json_dir)

    print('image 개수: ', len(image_list))
    print('json 개수: ', len(json_list))
    cnt = 0
    no_match = []
    for j in json_list:
        j2i = j[:-4] + 'jpg'
        if j2i in image_list:
            cnt += 1
        else:
            no_match.append(j)
    print('매칭 이미지, json 수: ', cnt)
    print('매치 안되는 json, ', str(no_match))


def TVTSplit(image_dir, json_dir):
    dest = input('split한 데이터셋을 저장할 경로: ')
    if not os.path.exists(dest + '//train'):
        os.makedirs(dest + '//train')
    if not os.path.exists(dest + '//valid'):
        os.makedirs(dest + '//valid')
    if not os.path.exists(dest + '//test'):
        os.makedirs(dest + '//test')

    json_list = os.listdir(json_dir)
    image_list = os.listdir(image_dir)
    train_set, test_set = train_test_split(json_list, test_size=0.3, random_state=1)
    valid_set, test_set = train_test_split(test_set, test_size=0.4, random_state=1)

    for tr in train_set:
        j2i = tr[:-4] + 'jpg'
        shutil.copy(os.path.join(json_dir, tr), dest + '//train//labels//' + tr)
        if j2i in image_list:
            shutil.copy(os.path.join(image_dir, j2i), dest + '//train//images//' + j2i)
    for va in valid_set:
        j2i = va[:-4] + 'jpg'
        shutil.copy(os.path.join(json_dir, va), dest + '//valid//labels//' + va)
        if j2i in image_list:
            shutil.copy(os.path.join(image_dir, j2i), dest + '//valid//images//' + j2i)
    for te in test_set:
        j2i = te[:-4] + 'jpg'
        shutil.copy(os.path.join(json_dir, te), dest + '//test//labels//' + te)
        if j2i in image_list:
            shutil.copy(os.path.join(image_dir, j2i), dest + '//test//images//' + j2i)


def main():
    image_dir = input('이미지 폴더 주소: ')
    json_dir = input('json 폴더 주소: ')

    Numcheck(image_dir, json_dir)
    TVTSplit(image_dir, json_dir)


if __name__ == "__main__":
    main()
