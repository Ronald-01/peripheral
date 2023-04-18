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

    url = 'https://detail.zol.com.cn/lcd/' + str(num) + '.html'
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
            keyboard = classdemo.Lcd(
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
    if index.id == 1434594:
        continue
    compare_url = 'https://detail.zol.com.cn/ProductComp_param_1434594-' + str(index.id) + '.html'
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
    with open('./picture/' + str(x) + '_lcd.jpg', 'wb') as fp:
        fp.write(img_data)

    # 抓取显示器数据：产品类型
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"产品类型")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.product_type = temp

    # 抓取键盘数据：屏幕尺寸
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"屏幕尺寸")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.screen_size = temp

    # 抓取键盘数据：屏幕比例
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"屏幕比例")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.screen_ratio = temp

    # 抓取键盘数据：响应时间
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"响应时间")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.response_time = temp

    # 抓取键盘数据：最佳分辨率
    data = compare_tree.xpath(
        '//*[@data-rel-num="1"]/th[contains(text(),"最佳分辨率")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.optimal_resolution = temp


    # 抓取键盘数据：显示颜色
    data = compare_tree.xpath(
        '//*[@data-rel-num="2"]/th[contains(text(),"显示颜色")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.display_color = temp

    # 抓取键盘数据：亮度
    data = compare_tree.xpath(
        '//*[@data-rel-num="2"]/th[contains(text(),"亮度")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.brightness = temp

    # 抓取键盘数据：刷新率
    data = compare_tree.xpath(
        '//*[@data-rel-num="2"]/th[contains(text(),"刷新率")]/following-sibling::td[2]/div//text()')
    # print(data)
    temp = ''
    for k in data:
        temp += k
    print(temp)
    index.refresh_rate = temp

    index.id = x
    # 将键盘数据保存为json文件
    index_dic = index.__dict__
    index_json = json.dumps(index_dic)
    with open('./data/' + str(index.id) + '_lcd.json', 'w', encoding='utf-8') as fp:
        fp.write(index_json)

    x += 1
    # demo = classdemo.Mice(1314775, 'Razer 毒蝰迷你版有线游戏鼠标', '竞技游戏', '普通鼠'
    #                       , '光电', '有线', 'USB', '6个', '双向滚轮', '黑色', '1.8m',
    #                       '118.3×56.1×38.3mm', '61g')
    # with open('对比1.html','w',encoding='utf-8') as fp:
    #     fp.write(response)
    # break
