# encoding:'utf-8'
import urllib.request
import urllib.parse
import json
from time import sleep

neeaID = '00000000'
time = '2018-05'
city = 'BEIJING_BEIJING'
city_cn = "北京"
jsonID = '11DD9F88BA948ECD804AE186E9C8FDD0'
city_encode = urllib.parse.quote(urllib.parse.quote(city_cn))
requestUrl = 'https://gre.etest.net.cn/testSites.do?p=testSites&m=ajax&ym={}&neeaID={}&cities={}%3B&citiesNames={}%3B&whichFirst=AS&isFilter=0&isSearch=1'.format(time,neeaID,city,city_encode)
header = {'Host': 'gre.etest.net.cn',
          'Connection': 'keep-alive',
          'Accept': 'application/json, text/javascript, */*; q=0.01',
          'X-Requested-With': 'XMLHttpRequest',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
          'Referer': 'https://gre.etest.net.cn/myStatus.do?neeaID=71466804',
          'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6',
          'Cookie': 'BIGipServerhw_gre_pool=302696458.22784.0000; BIGipServerHW_RuiShu_gre_test=2703149066.20480.0000; JSESSIONID={}; step=information.do; ajaxStep=searchSeats'.format(jsonID)}
req = urllib.request.Request(requestUrl)

def addHeader(obj, reqHeader):
    for item in obj.items():
        reqHeader.add_header(item[0], item[1])
        print('header added', item[0], item[1])
    return reqHeader


def sendRequest(req):
    response = urllib.request.urlopen(req)
    res = response.read()
    finished = False
    jsonobj = json.loads(res.decode('utf-8'))
    select_data = jsonobj[0]['dates']
    for sites in select_data:
        for site in sites['sites']:
            if site['realSeats'] == 1:
                print("you got one seats")
                print(site)
                finished = True
                
    return finished
    # print(json.dumps(select_data, indent=4, sort_keys=True,ensure_ascii=False))

def test():
    print('this is test',neeaID)



def main():
    finished = False
    while not finished:
        req = addHeader(header, req)
        finished = sendRequest(req)
        if finished :
            print('done.')
        else :   
            sleep(600)