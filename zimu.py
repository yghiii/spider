import requests
import urllib.request
from lxml import etree
import random
import time
import re
import json
import jsonpath

user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]
proxies = {
    'http': '140.246.45.153:3828',
    'http': '36.111.191.243:3828',
    'http':'140.246.151.112:3828',
    'http':'140.246.117.104:3828'
 }
headers = {
    'User-Agent':random.choice(user_agent),

}

starturl = 'http://www.zmz2019.com/subtitle?page={}&category=&format=&lang=&sort='
url_tail = 'http://www.zmz2019.com'

def download(url,num_retries):
    res_headers = {
        'User-Agent': random.choice(user_agent),
        'Connection': 'keep-alive',
        'Cookie':'UM_distinctid=16f1d25bc00445-05507b138fc039-6701434-100200-16f1d25bc01cf9; CNZZDATA1273422572=1503752653-1576737864-null%7C1576894799',
        'host':'got001.com'
    }
    download_headers = {
        'User-Agent': random.choice(user_agent) ,
        'Referer': url,
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive'
    }
    print(url)

    try:
        res = requests.get(url,headers = res_headers).text
    except:
        print('获取json失败，重试')
        if num_retries >0:
            download(url,num_retries-1)


    print('json页面',res)
    doc = json.loads(res)
    zip_url = doc['data']['info']['file']
    if doc['data']['info']['filename']=='':
        print('被反爬')
        return
    print(zip_url)

    with open('zip_url.txt','a+',encoding='utf-8')as f:
        f.write(zip_url+ '\n')
    f.close()
    print('字幕链接保存完毕')

def get_share_page(url,retries):
    try:
        response = requests.get(url, headers=headers).text
        # print(requests.get(url, headers=headers).status_code)
        content = etree.HTML(response)
        downloadpage_url = content.xpath('//div[@class="subtitle-links tc"]/a/@href')[0]
        print('到达下载页面')
        # print(downloadpage_url)
        # http://got001.com/subtitle.html?code=p1Sb92
        response_download = requests.get(downloadpage_url,headers = headers).text
        content_download = etree.HTML(response_download)
        # 获取请求传回的json拼接获得zip链接
        tmp = re.findall("code=[\S\s]+",downloadpage_url)[0]
        download_url = 'http://got001.com/api/v1/static/subtitle/detail?'+ tmp
        download(download_url,3)
    except:
        print('获取分享页失败，重试')
        if retries>0:
            get_share_page(url, retries-1)


for i in range(1799,2558,1):
    print('*************************爬取第%d页*************************'%i)
    response = requests.get(starturl.format(i),headers = headers).text
    content = etree.HTML(response)
    url_list = content.xpath('//div[@class="box subtitle-list" ]//a/@href')
    # //div[@class='box subtitle-list' ]//a/@href
    if url_list:
        for url in url_list:
            get_share_page(url_tail+url,3)
    #         time.sleep(2)
    #
    # time.sleep(3)







