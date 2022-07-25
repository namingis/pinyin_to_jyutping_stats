# import os
# print(os.environ)
import requests
from lxml import etree
from urllib import parse
from pandas import DataFrame
# print(requests)

url = "https://www.zdic.net/zd/zb/cc1/"
resp = requests.get(url)
# print(resp.text)
tree = etree.HTML(resp.text)  # or .XML seems to work too.
results1 = tree.xpath("/html/body/main//div[@class='bs_index3']/li/a/@href")
for i in range(len(results1)):
    results1[i] = results1[i][6:]
# print(results)
# print(id(results1))
resp.close()
url = "https://www.zdic.net/zd/zb/cc2/"
resp = requests.get(url)
tree = etree.HTML(resp.text)  # or .XML seems to work too.
results2 = tree.xpath("/html/body/main//div[@class='bs_index3']/li/a/@href")
for i in range(len(results2)):
    results2[i] = results2[i][6:]
# print(id(results2))
# print(id(results1))
results1.extend(results2)  # 会返回空类型，需注意不要再赋值了
characters = results1
# print(id(characters))
resp.close()

cantonese = []
mandarin = []
for char in characters:
    cantonese.append(list(char))
    mandarin.append(list(char))
# print(cantonese)
prefix = "http://m.yueyv.com/?keyword="
# prefix = "http://m.yueyv.com/?keyword=" + parse.quote("人".encode('gbk'))  # 测试用例
# 关于转码的问题参考：http://www.360doc.com/content/22/0120/14/30155531_1014166520.shtml
for i in range(3500):  # !:这循环太慢了，下次要爬虫的时候学点 Python 多线程吧，不过一下建立太多连接也不好，毕竟是小网站
    print(i+1, '/', len(characters), ':', characters[i])
    url = prefix + parse.quote(characters[i].encode('gbk'))
    resp = requests.get(url)
    resp.encoding = 'gbk'  # gbk 兼容 gb2312，这个网站用的应该是 gbk
    # print(resp.text)
    tree = etree.HTML(resp.text)  # or .XML seems to work too.
    results3 = tree.xpath("//span[@class='phonetic']//text()")
    results4 = tree.xpath("//div[@class='search-result']/table/tr/td[4]/text()")  # td[4] represents the 4th
    # <td>...</td>
    cantonese[i].extend(results3)
    if len(results4) > 0:
        results4[0] = results4[0][4:].strip()
    for j in range(1, len(results4)):
        results4[j] = results4[j].strip()
        if results4[j] == "":
            results4 = results4[:j]
            break
    mandarin[i].extend(results4)
    resp.close()
print(cantonese)  # 注意string中的转义字符在list中打印出来是不会体现功能的，如“\t”只会显示“\t”
print(mandarin)
cantonese_csv = DataFrame(data=cantonese)
cantonese_csv.to_csv("./cantonese.csv", encoding="utf8", index=False, header=False)  # index 和 header 设置为 False
# 来取消行首和列首的数字
mandarin_csv = DataFrame(data=mandarin)
mandarin_csv.to_csv("./mandarin.csv", encoding="utf8", index=False, header=False)
# 这个网站爬的普通话读音有的还是错的，比如鳄鱼的鳄，它就给标成了三声，不知道还有没有其他我没发现的
