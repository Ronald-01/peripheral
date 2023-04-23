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

# 初始化键盘列表
keyboard_list = []

# 获取前三页
for num in range(1, 4):

    url = 'https://detail.zol.com.cn/keyboard/' + str(num) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
    }
    # 获取键盘页面的html文档
    page_text = requests.get(url=url, headers=headers).text
    # 将其实例化至tree中
    compare_tree = etree.HTML(page_text)
    keyboard_li = compare_tree.xpath('//*[@id="J_PicMode"]/li')
    for index in keyboard_li:
        keyboard_id = index.xpath('./@data-follow-id')
        keyboard_name = index.xpath('./a/img/@alt')
        if keyboard_id:
            # print(mice_id[0].split('p')[1])
            # print(mice_name[0])
            keyboard = classdemo.Keyboard(
                id=int(keyboard_id[0].split('p')[1]),
                name=keyboard_name[0]
            )
            keyboard_list.append(keyboard)
        else:
            continue

# print(mice_list)
# for index in mice_list:
#     print(index.id,index.name)

x = int(1)
for index in keyboard_list:
    # index.id = '1358848'
    if index.id == 1358848:
        continue
    compare_url = 'https://detail.zol.com.cn/ProductComp_param_1358848-' + str(index.id) + '.html'
    response = requests.post(url=compare_url, headers=headers).text
    # with open('对比2.html','w',encoding='utf-8') as fp:
    #     fp.write(response)

    compare_tree = etree.HTML(response)
    print(index.id, index.name)

    # 抓取图片
    img_url = compare_tree.xpath('//*[@class="pic"]/a/img/@src')
    print(img_url[1])
    img_data = requests.get(url=img_url[1], headers=headers).content
    # with open('./picture/' + str(index.id) + '.jpg', 'wb') as fp:
    with open('./picture/' + str(x) + '_keyboard.jpg', 'wb') as fp:
        fp.write(img_data)

    # 抓取键盘数据：上市时间
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"上市时间")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.list_date = temp

    # 抓取键盘数据：产品定位
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"产品定位")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.product_position = temp

    # 抓取键盘数据：连接方式
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"连接方式")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.connect_method = temp

    # 抓取键盘数据：键盘接口
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"键盘接口")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.keyboard_interface = temp

    # 抓取键盘数据：按键数
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"按键数")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.key_number = temp

    # 抓取键盘数据：键盘布局
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"键盘布局")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.keyboard_layout = temp

    # 抓取键盘数据：轴体
    data = compare_tree.xpath(
        '//*[@data-rel-num="2"]/th[contains(text(),"轴体")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.axis = temp

    # 抓取键盘数据：键盘颜色
    data = compare_tree.xpath(
        '//*[@data-rel-num="3"]/th[contains(text(),"键盘颜色")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.color = temp

    # 抓取键盘数据：键盘尺寸
    data = compare_tree.xpath(
        '//*[@data-rel-num="3"]/th[contains(text(),"键盘尺寸")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.size = temp

    # 抓取键盘数据：键盘重量
    data = compare_tree.xpath(
        '//*[@data-rel-num="3"]/th[contains(text(),"键盘重量")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.weight = temp

    # 抓取键盘数据：供电模式
    data = compare_tree.xpath(
        '//*[@data-rel-num="3"]/th[contains(text(),"供电模式")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.supply_mode = temp

    index.id = x
    # 将键盘数据保存为json文件
    index_dic = index.__dict__
    index_json = json.dumps(index_dic)
    with open('./data/' + str(index.id) + '_keyboard.json', 'w', encoding='utf-8') as fp:
        fp.write(index_json)

    try:
        index.id = x
        # 将鼠标数据保存为json文件
        index_dic = index.__dict__
        index_json = json.dumps(index_dic)
        with open('./data/' + str(index.id) + '_keyboard.json', 'w', encoding='utf-8') as fp:
            fp.write(index_json)
        # type_name = file_name.split('_')[1].split('.')[0]
        url = 'http://127.0.0.1:8000/' + 'keyboard' + '/create'
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
