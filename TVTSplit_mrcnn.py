import os
import shutil

from sklearn.model_selection import train_test_split


def main():
    json_dir = input('json폴더의 주소: ')

    json_list = os.listdir(json_dir)

    if not os.path.exists(json_dir + '//train'):
        os.makedirs(json_dir + '//train')
    if not os.path.exists(json_dir + '//val'):
        os.makedirs(json_dir + '//val')
    if not os.path.exists(json_dir + '//test'):
        os.makedirs(json_dir + '//test')

    # train:valid:test = 7:2:1
    train_set, test_set = train_test_split(json_list, test_size=0.3, random_state=123)
    valid_set, test_set = train_test_split(test_set, test_size=0.4, random_state=123)

    # json과 매칭되는 이미지 파일을 이동
    for tr in train_set:
        shutil.copy(os.path.join(json_dir, tr), json_dir + '//train//' + tr)
    for va in valid_set:
        shutil.copy(os.path.join(json_dir, va), json_dir + '//val//' + va)
    for te in test_set:
        shutil.copy(os.path.join(json_dir, te), json_dir + '//test//' + te)


if __name__ == "__main__":
    main()
