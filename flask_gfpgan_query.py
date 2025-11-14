import requests

def test():
    # 默认超分4倍
    url = 'http://127.0.0.1:20018/sr'
    img_path = "/mnt/nas/shengjie/datasets/reid_sysu30k/sysu_test_set_all/gallery/000028311/000028311_c1_1.jpg"
    with open(img_path, 'rb') as f:
        files = {'image': f}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            with open('tmp.jpg', 'wb') as out:
                out.write(response.content)
            print('Saved result to tmp.jpg')
        else:
            print(f'Failed, status code: {response.status_code}, content: {response.text}')

if __name__ == '__main__':
    test()
