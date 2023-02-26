import requests
from bs4 import BeautifulSoup

# 输入城市名称
city = input("请输入城市名称：")

# 根据城市名称获取天气信息
url = "https://www.tianqi.com/{}/".format(city)
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 解析页面获取天气信息
weather = soup.find("dd", class_="weather").text.strip()
temperature = soup.find("dd", class_="temperature").text.strip()
wind = soup.find("dd", class_="wind").text.strip()

# 输出天气信息
print("城市：{}".format(city))
print("天气：{}".format(weather))
print("温度：{}".format(temperature))
print("风力：{}".format(wind))
