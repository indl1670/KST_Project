import os


def main():
    image_dir = input('image폴더의 주소: ')
    json_dir = input('json폴더의 주소: ')

    image_list = os.listdir(image_dir)
    json_list = os.listdir(json_dir)

    print('image 개수: ', len(image_list))
    print('json 개수: ', len(json_list))

    cnt = 0
    no_match = []
    data_pick = []

    for j in data_pick:
        if j in image_list:
            # image가 image_dir에 있으면 bboximage 폴더로 이동
            cnt += 1
        else:
            no_match.append(j)
    print('매칭 이미지, json 수: ', cnt)
    print('매치 안되는 json: ', str(no_match))


if __name__ == "__main__":
    main()
