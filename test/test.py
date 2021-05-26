# -*- coding: utf-8 -*-
"""
Created on Wed May 26 14:48:48 2021

@author: 郭耸
"""

"""
一、编程题
新冠疫情实时数据获取，例如从百度找到原始页面
https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4
1. 把画面保存成htm文件
2. 用代码解析文件，获取疫情信息
3. 按照疫情地区、新增、现有、累计、治愈、死亡的顺序，保存成csv文件，
"""


""" 说明：把画面保存成htm文件没会做"""

from selenium import webdriver
import time
import csv
import pandas as pd
url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4'
driver = webdriver.Chrome(executable_path=r'E://chromedriver.exe')
driver.get(url)
time.sleep(1)

element=driver.find_element_by_xpath('//*[@id="nationTable"]/div')
driver.execute_script("arguments[0].click();", element)

driver.find_elements_by_class_name('Common_1-1-303_3lDRV2')[2].click()


cla=driver.find_elements_by_class_name("VirusTable_1-1-303_26gN5Z")
names=cla[0].text.split("\n")

a=driver.find_elements_by_class_name("VirusTable_1-1-303_3m6Ybq")
namelist=[]
for i in a:
    name=i.text.split("\n")
    namelist.append([name[0]]+name[1].split(" "))
df1=[names]+namelist
df1=pd.DataFrame(df1)
df1.to_csv("国内各地区疫情统计汇总.csv",index=None,header=None)


names1=cla[1].text.split("\n")
a=driver.find_elements_by_class_name("VirusTable_1-1-303_2AH4U9")
namelist1=[]
for i in a:
    name=i.text.split("\n")
    namelist1.append([name[0]]+name[1].split(" "))
df2=[names1]+namelist1
df2=pd.DataFrame(df2)
df2.to_csv("国外各国家疫情统计汇总.csv",index=None,header=None)
print("爬取成功")
"""
二、编程题
数据整理
原始数据格式如下：
{
 "StateCode": 1,
 "Reason": "成功",
 "Result": {
  "StartDate": "2020-10-09",
  "EndDate": "2020-11-07",
  "pc": "16994,18287,12019,17697,17706,18025,18042,16645,11614,11730,18692,17577,17226,17607,16437,11687,11243,19179,21807,21020,19757,18059,11848,11036,18498,18720,30578,22214,18464,12710",
  "mobile": "56205,60619,54847,53336,53818,55124,56898,55286,54882,53794,51338,51081,51288,51385,49601,52956,51385,52032,74519,73008,67925,61114,60770,56928,52806,55550,97643,74485,65163,61676"
 }
}
需要转换成下面格式：
{
 'status': 0,
 'data': [{
  'date': '2020-10-09',
  'pc': '16994',
  'mobile': '56205'
 }, {
  'date': '2020-10-10',
  'pc': '18287',
  'mobile': '60619'
 }, {
  'date': '2020-10-11',
  'pc': '12019',
  'mobile': '54847'
 }, {
  'date': '2020-10-12',
  'pc': '17697',
  'mobile': '53336'
 }, {
  'date': '2020-10-13',
  'pc': '17706',
  'mobile': '53818'
 }, {
  'date': '2020-10-14',
  'pc': '18025',
  'mobile': '55124'
 }, {
  'date': '2020-10-15',
  'pc': '18042',
  'mobile': '56898'
 }, {
  'date': '2020-10-16',
  'pc': '16645',
  'mobile': '55286'
 }, {
  'date': '2020-10-17',
  'pc': '11614',
  'mobile': '54882'
 }, {
  'date': '2020-10-18',
  'pc': '11730',
  'mobile': '53794'
 }, {
  'date': '2020-10-19',
  'pc': '18692',
  'mobile': '51338'
 }, {
  'date': '2020-10-20',
  'pc': '17577',
  'mobile': '51081'
 }, {
  'date': '2020-10-21',
  'pc': '17226',
  'mobile': '51288'
 }, {
  'date': '2020-10-22',
  'pc': '17607',
  'mobile': '51385'
 }, {
  'date': '2020-10-23',
  'pc': '16437',
  'mobile': '49601'
 }, {
  'date': '2020-10-24',
  'pc': '11687',
  'mobile': '52956'
 }, {
  'date': '2020-10-25',
  'pc': '11243',
  'mobile': '51385'
 }, {
  'date': '2020-10-26',
  'pc': '19179',
  'mobile': '52032'
 }, {
  'date': '2020-10-27',
  'pc': '21807',
  'mobile': '74519'
 }, {
  'date': '2020-10-28',
  'pc': '21020',
  'mobile': '73008'
 }, {
  'date': '2020-10-29',
  'pc': '19757',
  'mobile': '67925'
 }, {
  'date': '2020-10-30',
  'pc': '18059',
  'mobile': '61114'
 }, {
  'date': '2020-10-31',
  'pc': '11848',
  'mobile': '60770'
 }, {
  'date': '2020-11-01',
  'pc': '11036',
  'mobile': '56928'
 }, {
  'date': '2020-11-02',
  'pc': '18498',
  'mobile': '52806'
 }, {
  'date': '2020-11-03',
  'pc': '18720',
  'mobile': '55550'
 }, {
  'date': '2020-11-04',
  'pc': '30578',
  'mobile': '97643'
 }, {
  'date': '2020-11-05',
  'pc': '22214',
  'mobile': '74485'
 }, {
  'date': '2020-11-06',
  'pc': '18464',
  'mobile': '65163'
 }, {
  'date': '2020-11-07',
  'pc': '12710',
  'mobile': '61676'
 }]
}
"""
# import datetime
# x={
#  "StateCode": 1,
#  "Reason": "成功",
#  "Result": {
#   "StartDate": "2020-10-09",
#   "EndDate": "2020-11-07",
#   "pc": "16994,18287,12019,17697,17706,18025,18042,16645,11614,11730,18692,17577,17226,17607,16437,11687,11243,19179,21807,21020,19757,18059,11848,11036,18498,18720,30578,22214,18464,12710",
#   "mobile": "56205,60619,54847,53336,53818,55124,56898,55286,54882,53794,51338,51081,51288,51385,49601,52956,51385,52032,74519,73008,67925,61114,60770,56928,52806,55550,97643,74485,65163,61676"
# }
# }
# data={}
# list1=[]
# list2=[]
# timed=[]
# start=x.get("Result").get('StartDate')
# end=x.get("Result").get('EndDate')
# pc=x.get("Result").get('pc')
# pclist=pc.split(',')
# mobile=x.get("Result").get('mobile')
# mobilelist=mobile.split(',')

# timed.append(start)
# datestart=datetime.datetime.strptime(start,'%Y-%m-%d')
# dateend=datetime.datetime.strptime(end,'%Y-%m-%d')

# while datestart<dateend:
#     datestart+=datetime.timedelta(days=1)
#     timed.append(datestart.strftime('%Y-%m-%d'))
# time1=-1
# for i in pclist:
#     time1+=1
#     data2={}
#     data2['date']=timed[time1]
#     data2['pc']=i
#     # list1.append(data2)
#     data2['mobile']=mobilelist[time1]
#     list2.append(data2)
# data['status']=0
# data['data']=list2
# print(data)
"""
三、简答题
一个文件中保存有1亿个url地址，每个地址的最大长度是1KB。如果想要找到所有重复的url，该如何设计程序。

解法1：因为数据量很大，可以用分布式计算：hadoop  mapreduce来计算，通过相同的键（url），来计算出现的次数。
解法2： 1.计算每个url的哈希值hash,然后用 hash % 500得到值i,至此，将文件a划分为a0,a1,...,a499，
        2.把a0到a499分成2大部分为aa1和aa2，接着遍历 aa1，把 URL 存储到一个 HashSet 集合中。然后遍历 aa2中每个 URL，看在 HashSet 集合中是否存在，若存在，说明这就是共同的 URL，可以把这个 URL 保存到一个单独的文件中。

"""

