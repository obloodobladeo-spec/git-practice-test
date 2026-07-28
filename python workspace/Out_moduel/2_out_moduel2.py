from urllib import request
from bs4 import BeautifulSoup
import csv

# 서로 다른 주소지만 반복되는 같은 주소일 경우

names = ['LG전자', "SK이터닉스", "현대차"]
codes = ["066570", "475150", "005380"]

# zip : 두 개의 리스트 요소를 하나로 합치기
stocks = list(zip(names, codes)) # 같은 index 값에 따라 묶인다.

url = "https://finance.naver.com/item/sise.naver?code={}"

with open("stock_prices.csv", "w", encoding="utf-8", newline="") as file:
    write = csv.write(file)
    file.write("종목명,현재가\n")
    for stock in stocks :
        stock_url = url.format(stock[1])

        response = request.urlopen(stock_url)
        html = response.read()

        soup = BeautifulSoup(html, "html.parser")
        data = soup.select_one("#_nowVal")
        price = data.text.replace(",", "")

        file.write(f"{stock[0]},{price}\n")