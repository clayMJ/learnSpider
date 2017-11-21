##目标:获取上交所和深交所所有股票名称和交易信息 
##输出:保存到文件中
##候选网站:http://finance.sina.com.cn/stock/
##         http://gupiao.baidu.com/stock/
##         (静态)
##  步骤:从东方财富获取股票列表 
##       逐个输入股票信息
##       print
import reuqests
import re
from bs4 import BeautifulSoup
import traceback


def getHTMLText(url, code='utf-8'):
    try:
        r=request.get(url)
        raise_for_status
        r.encoding = r.apparent.encoding
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL,'GB2312')
    soup = BeautifulSoup(html, 'htmlparser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue

def getStockInfo(lst, stockURL, fpatch):
    count = 0
    for stock in lst:
        url = stockURL + stock ".html"
        html = getHTMLText(url)
        try:
            if html =="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count=count + 1
                print('\r当前速度: {:.2f}%'.format(count*100/len(lst)),end='')
        except:
            count=count+1
            traceback.print_exc()
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'http://gupiao.baidu.com/stock/'
    output_file = '/Users/bandaotiehe/learnspider'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()
