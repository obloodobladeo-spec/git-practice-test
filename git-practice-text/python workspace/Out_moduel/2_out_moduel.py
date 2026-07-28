from bs4 import BeautifulSoup
from urllib import request

url = "https://finance.naver.com/item/sise.naver?code=005930"
response = request.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, "html.parser") 
# html.parser : html 구조적으로 쪼개는것

price = soup.select_one("#_nowVal")

print(price.text)