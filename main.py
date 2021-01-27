import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.naver.co.kr")
print(res.text)