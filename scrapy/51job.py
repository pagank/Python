import requests
from lxml import etree
import json

url = 'https://search.51job.com/list/080200,000000,0000,00,9,99,\
python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&\
cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary\
=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=\
9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "zh-CN,zh;q=0.9",
          "Cache-Control": "max-age=0",
          "Connection": "keep-alive",
          "Host": "search.51job.com",
          "Sec-Fetch-Dest": "document",
          "Sec-Fetch-Mode": "navigate",
          "Sec-Fetch-Site": "same-origin",
          "Sec-Fetch-User": "?1",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36" }


response = requests.get(url = url, headers = header)
response.encoding = 'gbk'
# print(response.text)
html_51job = etree.HTML(response.text)
all_div = html_51job.xpath("//div[@id='resultList']//div[@class='el']")
# print(all_div)
info_li = []
for item in all_div:
    info = {}
    info['job_name'] = item.xpath("./p/span/a/@title")[0]
    info['cmpany_name'] = item.xpath(".//span[@ class='t2']/a/@title")[0]
    try:
        info['salary'] = item.xpath(".//span[@ class='t4']/text()")[0]
    except IndexError:
        info['salary'] = None
    info_li.append(info)
    # print(info)

print(json.dumps(info_li))