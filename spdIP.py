import requests
url = "http://m.ip138.com/ip.sap?ip="
try:
    r = request.get(url + '202.204.20.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.test[-500:])
except:
    print("获取失败")
