import requests
import os
url = ""
root = ""
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = r.requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件已保存')
    else:
        print('文件已存在')
except:
    print("爬取失败")
