import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient
import time

import pymysql
import pandas as pd

driver = webdriver.Chrome(executable_path="../chromedriver.exe")
# driver.get(
#     "https://www.visitjeju.net/kr/detail/list?menuId=DOM_000001719001000000&cate1cd=cate0000000005#p1&region2cd"
#     "&pageSize=2000&sortListType=reviewcnt&viewType=thumb")

driver.get(
    "https://orangebottles.com/")

time.sleep(5)

host_name = "database-1.cyt5fnsjiaht.ap-northeast-2.rds.amazonaws.com"
username = "admin"
password = "root1234"
database_name = "dbtest"

db = pymysql.connect(
    host=host_name,
    port=3306,
    user=username,
    passwd=password,
    db=database_name,
    charset='utf8mb4'
)

cursor = db.cursor()

delete = """
DELETE FROM test;
"""
cursor.execute(delete)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

id_num = 0


# print(trs)
def main_scraper(category, category_name, id_num):
    i = 0
    for tr in category:
        i += 1
        id_num += 1
        try:
            img = tr.select_one('div:nth-child(' + str(i) + ') > div > div.item-thumbs > a > img')['data-original']
            title = tr.select_one('div:nth-child(' + str(i) + ') > div > div.item-detail > a > div > h2').text
            price = tr.select_one('div:nth-child(' + str(i) + ') > div > div.item-detail > a > div > div > p.pay').text
            description = tr.select_one('div:nth-child(' + str(i) + ') > div > div.item-detail > div.item-summary > p '
                                                                    '> span > strong > span').text
        except Exception as e:
            continue

        else:
            print("===================================" + str(i) + "==============================================")
            print('>>>>>>>>>>>>>>>>>>>>' + str(id_num) + '<<<<<<<<<<<<<<<<<')
            print(category_name)
            print(img)
            print(title)
            print(price)
            print(description)

            cursor.execute(
                f"INSERT INTO test VALUES('{id_num}','{category_name}','{img}','{title}','{price.strip()}','{description}')");

            db.commit()
    return id_num


best_wine = soup.select_one(
    '#container_w20210528bf509173d0cea > div.owl-stage-outer > div ')
id_num = main_scraper(best_wine, "????????? ??????", id_num)

prize_wine = soup.select_one(
    '#container_w2021092984a7b59f75039 > div.owl-stage-outer > div')
id_num = main_scraper(prize_wine, "????????? ??????", id_num)

vivino_4_wine = soup.select_one(
    '#container_w20210930ce37fd6a8919e > div.owl-stage-outer > div ')
id_num = main_scraper(vivino_4_wine, "?????????4.0 ?????? ????????? ????????? ??????", id_num)

reasonable_price_wine = soup.select_one(
    '#container_w20210930d50feea087638 > div.owl-stage-outer > div ')
id_num = main_scraper(reasonable_price_wine, "????????? ?????? ??????", id_num)

spirits = soup.select_one(
    '#container_w2021093040bf057aad764 > div.owl-stage-outer > div ')
id_num = main_scraper(spirits, "?????????", id_num)

Makgeolli = soup.select_one(
    '#container_w20210930229d886b118de > div.owl-stage-outer > div ')
id_num = main_scraper(Makgeolli, "?????????, ??????", id_num)

ricewine = soup.select_one(
    '#container_w20210930245a5bfde73a3 > div.owl-stage-outer > div ')
id_num = main_scraper(ricewine, "??????, ??????", id_num)

fruitwine = soup.select_one(
    '#container_w202109309b547ba4e5db8 > div.owl-stage-outer > div ')
id_num = main_scraper(fruitwine, "?????????, ?????????", id_num)

whiskey = soup.select_one(
    '#container_w20210930a64452f18f1f3 > div.owl-stage-outer > div ')
id_num = main_scraper(whiskey, "?????????", id_num)

beer = soup.select_one(
    '#container_w20210930044d097444547 > div.owl-stage-outer > div ')
id_num = main_scraper(beer, "??????", id_num)

sake = soup.select_one(
    '#container_w2021093083a3085e0ac37 > div.owl-stage-outer > div ')
id_num = main_scraper(sake, "??????", id_num)

chinaliquor = soup.select_one(
    '#container_w202109302e5212f0f79a5 > div.owl-stage-outer > div ')
id_num = main_scraper(chinaliquor, "??????", id_num)

print('!@#$%^&*() ?????? !@#$%^&*()')
db.close()
# driver.quit()


driver.quit()

#
# print("=================================================================================")
# print(trs)
