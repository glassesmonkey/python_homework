import os
import re
import time
import urllib.request

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

# #webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
# #输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
# driver =webdriver.PhantomJS(executable_path="phantomjs.exe")
 
# #使用浏览器请求页面
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# #加载3秒，等待所有数据加载完毕
# time.sleep(3)
# #通过id来定位元素，
# #.text获取元素的文本数据
# print(driver.find_element_by_id('content').text)
 
# #关闭浏览器
# driver.close()
#my_text = driver.find_element_by_id("img_load")

# time.sleep(3)
#print("xiaolaojjjjjjjjjjjj"+driver.page_source)
#print(driver.find_element_by_id('img').text)

#下载图片模块
def download(soup,chapter,page):
    i=0
    items = soup.find_all('img')
    # print('-------------soup-----------------')
    # print(soup)
    # print('---------------items----------------')
    # print(items)
    # print(chapter)
    folder_path = './photo/'+chapter+'/'
    if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
        os.makedirs(folder_path)  # 创建文件夹
    
    for index,item in enumerate(items):
        
        i = i + 1
        if (item and index == 0):
            src = item.get('src')
            # print('-------------src-------------------')
            # print(src)
            html = requests.get(src)   # get函数获取图片链接地址，requests发送访问请求
            img_name = folder_path + str(page)+"."+str(index) +'.png'
            time.sleep(0.1)
            with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
                file.write(html.content)
                file.flush()
            file.close()  # 关闭文件
            print('第%d张图片下载完成' %(i))
            #print(html.content)
            time.sleep(0.1)  # 自定义延时


#提取初始地址
def extract_url(parameter_list):
    list1=[]
    
    i = 0
    soup = BeautifulSoup(parameter_list, 'html.parser')
    items = soup.find_all(href=re.compile("page"))
    #print("items")
    #print(items)
    for index,item in enumerate(items):
        url_split=item.get('href')
        list1.append("http://www.1manhua.net"+url_split)

    
    for index in range(len(list1)):
        soup = open_bs(list1[index])#打开第一页
        max_page = soup.find_all(onclick=find_max_page)#获取该章节总页数
        url_transfer = list1[index]
        #print('---------result----------------')
        #print(url_transfer)
        for index,item in enumerate(max_page):
            onclicks = item.get('onclick')
            pattern = r'1\.'
            result = re.split(pattern, url_transfer)

            pattern_2 = r'/'
            result_2 = re.split(pattern_2,url_transfer)
            print("----------------------result-----------------------")
            print(result_2)
            i=index+1
            url_final=result[0]+str(i)+'.'+result[1]
            # print(url_final)
            soup_1 = open_by_drive(url_final)
            download(soup_1,result_2[3],i)

        



#创建bs对象
def open_bs(_url):
    url  = _url
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)  # 使用headers避免访问受限
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

#soup查找函数
def find_max_page(onclick):
        return onclick and re.compile("csel2").search(onclick)

def open_by_drive(url_fin):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    driver.get(url_fin)
    element = WebDriverWait(driver, 200).until(lambda x:x.find_element_by_id(r'^img[0-9]+$'))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    print('-------------------------close driver-------------------------------')
    return soup

#main
if __name__=='__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    urllink = "http://www.1manhua.net/manhua27411.html"
    driver.get(urllink)
    time.sleep(5)
    #soup = BeautifulSoup(driver.page_source, 'html.parser')
    extract_url(driver.page_source)
    driver.close()
