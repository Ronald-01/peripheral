import json, os

import requests

folder_path = "./data"  # change this to your folder path
for file_name in os.listdir(folder_path):
    # print()
    # break
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        # 将json读取为字典
        with open(file_path, "r", encoding="utf8") as fp:
            json_data = fp.read()
            # 不用将其转化为字典，因为fastapi接口是双引号，而字典是单引号
            # json_data = json.load(fp)
        type_name = file_name.split('_')[1].split('.')[0]
        url = 'http://127.0.0.1:4000/' + type_name + '/create'
        # print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
        }
        response = requests.post(url=url, data=json_data, headers=headers)
        print(response)
