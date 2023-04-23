import json
import os.path

import requests
from lxml import etree
import classdemo

# 建立放置图片的文件夹
if not os.path.exists('./picture'):
    os.mkdir('./picture')

# 建立放置外设数据（json文件）的文件夹
if not os.path.exists('./data'):
    os.mkdir('./data')
# 初始化鼠标列表
mice_list = []

for num in range(1,4):

    url = 'https://detail.zol.com.cn/mice/'+str(num)+'.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
    }
    # 获取鼠标页面的html文档
    page_text = requests.get(url=url, headers=headers).text
    # 将其实例化至tree中
    compare_tree = etree.HTML(page_text)
    mice_li = compare_tree.xpath('//*[@id="J_PicMode"]/li')
    for index in mice_li:
        mice_id = index.xpath('./@data-follow-id')
        mice_name = index.xpath('./a/img/@alt')
        if mice_id:
            # print(mice_id[0].split('p')[1])
            # print(mice_name[0])
            mice = classdemo.Mice(
                id=int(mice_id[0].split('p')[1]),
                name=mice_name[0]
            )
            mice_list.append(mice)
        else:
            continue

# print(mice_list)
# for index in mice_list:
#     print(index.id,index.name)

x = int(1)
for index in mice_list:
    # index.id = '1314775'
    if index.id == 1314775:
        continue
    compare_url = 'https://detail.zol.com.cn/ProductComp_param_1314775-' + str(index.id) + '.html'
    response = requests.post(url=compare_url, headers=headers).text
    compare_tree = etree.HTML(response)
    print(index.id, index.name)

    # 抓取图片
    img_url = compare_tree.xpath('//*[@class="pic"]/a/img/@src')
    print(img_url[1])
    img_data = requests.get(url=img_url[1], headers=headers).content
    # with open('./picture/' + str(index.id) + '.jpg', 'wb') as fp:
    with open('./picture/' + str(x) + '_mice.jpg', 'wb') as fp:
        fp.write(img_data)

    # 抓取鼠标数据：适用类型
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"适用类型")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.aplicable_type = temp

    # 抓取鼠标数据：鼠标大小
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"鼠标大小")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.mice_size = temp

    # 抓取鼠标数据：工作方式
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"工作方式")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.work_way = temp

    # 抓取鼠标数据：连接方式
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"连接方式")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.connect_method = temp

    # 抓取鼠标数据：连接方式
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"连接方式")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.connect_method = temp

    # 抓取鼠标数据：鼠标接口
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"鼠标接口")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.mice_interface = temp

    # 抓取鼠标数据：按键数
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"按键数")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.key_number = temp

    # 抓取鼠标数据：滚轮方向
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"滚轮方向")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.wheel_direction = temp

    # 抓取鼠标数据：鼠标颜色
    data = compare_tree.xpath(
        '//*[@data-rel-num="3"]/th[contains(text(),"鼠标颜色")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.color = temp

    # 抓取鼠标数据：鼠标线长
    data = compare_tree.xpath(
        '//*[@data-rel-num="3"]/th[contains(text(),"鼠标线长")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.line_lenght = temp

    # 抓取鼠标数据：鼠标尺寸
    data = compare_tree.xpath(
        '//*[@data-rel-num="3"]/th[contains(text(),"鼠标尺寸")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.size = temp

    # 抓取鼠标数据：鼠标重量
    data = compare_tree.xpath(
        '//*[@data-rel-num="3"]/th[contains(text(),"鼠标重量")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.weight = temp


    try:
        index.id = x
        # 将鼠标数据保存为json文件
        index_dic = index.__dict__
        index_json = json.dumps(index_dic)
        with open('./data/' + str(index.id) + '_mice.json', 'w', encoding='utf-8') as fp:
            fp.write(index_json)
        # type_name = file_name.split('_')[1].split('.')[0]
        url = 'http://127.0.0.1:8000/' + 'mice' + '/create'
        # print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
        }
        response = requests.post(url=url, data=index_json, headers=headers)
        x += 1

    except:
        continue
    finally:
        print(response)

    # demo = classdemo.Mice(1314775, 'Razer 毒蝰迷你版有线游戏鼠标', '竞技游戏', '普通鼠'
    #                       , '光电', '有线', 'USB', '6个', '双向滚轮', '黑色', '1.8m',
    #                       '118.3×56.1×38.3mm', '61g')
    # with open('对比1.html','w',encoding='utf-8') as fp:
    #     fp.write(response)
    # break
    # folder_path = "./data"  # change this to your folder path
    # for file_name in os.listdir(folder_path):
    #     # print()
    #     # break
    #     if file_name.endswith(".json"):
    #         file_path = os.path.join(folder_path, file_name)
    #         # 将json读取为字典
    #         with open(file_path, "r", encoding="utf8") as fp:
    #             json_data = fp.read()
    #             # 不用将其转化为字典，因为fastapi接口是双引号，而字典是单引号
    #             # json_data = json.load(fp)
    #         type_name = file_name.split('_')[1].split('.')[0]
    #         url = 'http://127.0.0.1:8000/' + type_name + '/create'
    #         # print(url)
    #         headers = {
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
    #         }
    #         response = requests.post(url=url, data=json_data, headers=headers)
    #         print(response)