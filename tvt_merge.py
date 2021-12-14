import os
import json
import shutil


def coco_merge(json_dir, dest, cls):
    json_list = os.listdir(json_dir)
    file_list_json = [file for file in json_list if file.endswith(".json")]

    theone = os.path.join(json_dir, file_list_json[0])
    thetwo = os.path.join(json_dir, file_list_json[1])
    cls = cls + '.json'
    target = os.path.join(dest, 'annotations', cls)

    os.system('pyodi coco merge %s %s %s' % (theone, thetwo, target))
    els = file_list_json[2:]

    for e in els:
        sac = os.path.join(json_dir, e)
        os.system('pyodi coco merge %s %s %s' % (target, sac, target))


def image_split(dest, data_pick):
    img_dir = input('image 파일들의 경로:')

    ann_dir = os.path.join(dest, 'annotations')
    img_dest = os.path.join(dest, 'images')

    with open(os.path.join(ann_dir, 'train.json'), 'r', encoding='utf8') as ann:
        data = json.load(ann)
        img_list = data['images']
        for img in img_list:
            fn = img['file_name']
            if fn in data_pick:
                shutil.copy(os.path.join(img_dir, fn), os.path.join(img_dest, 'train'))

    with open(os.path.join(ann_dir, 'val.json'), 'r', encoding='utf8') as ann:
        data = json.load(ann)
        img_list = data['images']
        for img in img_list:
            fn = img['file_name']
            if fn in data_pick:
                shutil.copy(os.path.join(img_dir, fn), os.path.join(img_dest, 'val'))

    with open(os.path.join(ann_dir, 'test.json'), 'r', encoding='utf8') as ann:
        data = json.load(ann)
        img_list = data['images']
        for img in img_list:
            fn = img['file_name']
            if fn in data_pick:
                shutil.copy(os.path.join(img_dir, fn), os.path.join(img_dest, 'test'))


def main():
    print('--coco data merge--')
    train_json = input('train json 파일들의 경로: ')
    val_json = input('valid json 파일들의 경로: ')
    test_json = input('test json 파일들의 경로: ')

    dest = input('split한 데이터셋을 저장할 경로: ')

    # 폴더 생성
    if not os.path.exists(dest + '//images'):
        os.makedirs(dest + '//images')
        os.makedirs(dest + '//images//train')
        os.makedirs(dest + '//images//val')
        os.makedirs(dest + '//images//test')
    if not os.path.exists(dest + '//annotations'):
        os.makedirs(dest + '//annotations')

    coco_merge(train_json, dest, 'train')
    coco_merge(val_json, dest, 'val')
    coco_merge(test_json, dest, 'test')

    data_pick = ['a.jpg', 'b.jpg']

    print('--image split--')
    image_split(dest, data_pick)


if __name__ == "__main__":
    main()
