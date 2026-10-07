# pyright: reportMissingModuleSource=false
import requests
# 通过发送http请求获取网页内容
url = 'https://v1.hitokoto.cn/'
params = {
    'c': 'i',
    'encode': 'json'
}
response = requests.get(url=url, params=params)
if response.status_code == 200:
    print('请求成功')
    data = response.json()
    print(data)
else:
    print('请求失败')