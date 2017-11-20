##爬取大学排名
##输入L大学排名URL链接；输出：大学信息(排名，大学，总分)
##可行性：
##步骤:1.从网络中获取大学排名页面内容        getHTMLText()
##     2.提取网页内容放到合适数据结构中      fillUnivList()
##     3.利用数据结构输出                    printUnivList()
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
    return "链接失败"

def fillUnivList(ulist, html):
    soup = BeautifulSoup(r.text, "htmlparser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])
    pass
 
def printUnivList(ulist, num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分"), chr(12288))
    for i in range (num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))  ##对中英文排版进行优化

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaimin'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 nuivs
main()



