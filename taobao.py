##目标:获取淘宝搜索页面信息，提取其中商品名称和价格
##理解:淘宝的搜索接口翻页的处理
##技术路线：requests-re
##步骤：提交商品搜索请求，循环获取页面
##      对于每个页面获取商品名称和信息价格
##      信息输出到屏幕上
##
import requests
import re

def getHTMLText(url):
    try:
        r=requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent.encoding
        return r.text
    excpet:
        return ""

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("")

def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' +goods
    infoList = []
    for i in range (depth):
        try:
            url = start_url + '&s=' +str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodList(infoList)
main()

