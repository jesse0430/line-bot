import pymysql
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer
import requests, json
import pandas as pd
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import re, random


ua = UserAgent()
user_agent = ua.random
headers = {'user-agent': user_agent}
url=[]
all_item=[]
    #抓url
def get_all(area,page_limit):
    try:
        for i in range(1,page_limit):
                res=requests.get(f'https://buy.yungching.com.tw/region/%E4%BD%8F%E5%AE%85_p/%E5%8F%B0%E4%B8%AD%E5%B8%82-{area}E5%B1%AF%E5%8D%80_c/_rm/?pg={i}',headers=headers)
                soup=bs(res.text,'lxml') 
                print(i,'complete')
                for l in range(len(soup.select('div.l-main-list > ul > li > a'))):
                    dic1={}
                    dic1['url']='https://buy.yungching.com.tw'+soup.select('div.l-main-list > ul > li > a')[l].get('href')
                    url.append(dic1)

        for i in range(len(url)):
                res=requests.get(url[i]['url'],headers=headers)
                print(url[i]['url'])
                soup=bs(res.text,'lxml')
                dic={}
                #總價
                try:
                    x=soup.select(' div.house-info-prices.right > em > span')[0].text
                    xx= "".join(re.findall(r'\d+',x))
                    total=int(xx)

                except:
                    xx=1
                    total=int(xx)
                #坪數
                y=soup.find('div','text').span.text
                yy=re.findall(r'\d+\.\d+',y)[0]
                per=float(yy)

                dic['title']=soup.find('h1','house-info-name').text.strip()
                try:
                    dic['house_type']=soup.find_all('div','text')[2].find_all('span')[1].text
                except:
                    dic['house_type']=""
                dic['address']=soup.select(' div.left > div.house-info-addr')[0].text
                try:
                    z=soup.select('div:nth-child(3) > div > span:nth-child(2)')[0].text
                    dic['house_age']=re.findall(r'\d+\.\d+',z)[0]
                except:
                    dic['house_age']=0
                dic['floor_space']=yy
                dic['price']=xx
                dic['per_price']=str(round(total/per,2))
                all_item.append(dic)
                    #dataframe
        df=pd.DataFrame(all_item)
        data = {'電梯大樓':'電梯大樓','公寓':'公寓','華廈':'華廈','透天厝':'透天厝','別墅':'透天厝','透天':'透天厝','':'未提供'}
        df['house_type'] = df['house_type'].map(data)
        df.fillna(value=0)
        return df
    except Exception as e:
        print(e)
print(get_all('%E5%8C%97%',146))
print(get_all('%E8%A5%BF%',141))
print(get_all('%E5%8D%97%',161))
