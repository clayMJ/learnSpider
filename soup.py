import bs4 from BeautifulSoup
url=""
r=requests.get(url)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
