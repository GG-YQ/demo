# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import csv

def swipeUp(driver, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5     # x坐标
    y1 = l['height'] * 0.75   # 起始y坐标
    y2 = l['height'] * 0.25   # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)
        
def swipeRight(driver, t=500, n=1):
    '''向右滑动屏幕'''
    l = driver.get_window_size()
    y1 = l['height'] * 0.5     # y坐标
    x1 = l['width'] * 0.75   # 起始x坐标
    x2 = l['width'] * 0.25   # 终点x坐标
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
        
def swipeLeft(driver, t=500, n=1):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    y1 = l['height'] * 0.5     # y坐标
    x1 = l['width'] * 0.75   # 起始x坐标
    x2 = l['width'] * 0.25   # 终点x坐标
    for i in range(n):
        driver.swipe(x2, y1, x1, y1, t)       

def swipe1(driver, t=500, n=1,d=0.05):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.75        # 起始y坐标
    y2 = y1-l['height'] * d         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)




server = 'http://localhost:4723/wd/hub'
desired_caps={"platformName": "Android",
              "deviceName": "Redmi_4",
              "appPackage": "com.autonavi.minimap",
              "appActivity": "com.autonavi.map.activity.NewMapActivity",
              "automationName": "UiAutomator1",
              "unicodeKeyboard":True ,#是使用unicode编码方式发送字符串
              "resetKeyboard": True #隐藏键盘
              }
desired_caps['noReset'] = True #检查如果程序已经安装就不会再重复安装，直接启动
driver = webdriver.Remote(server,desired_caps)
sleep(5) #休眠五秒等待页面加载完成

try:
    el1 = driver.find_element_by_id("android:id/button1")
    el1.click()
    el1.click()
    el1.click()
except: 
    pass

try:
    swipeRight(driver, t=500, n=1)
    el2 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"高德地图\"]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
    el2.click() #打开高德
except: 
    pass
try:
    swipeRight(driver, t=500, n=1)
    el3 = driver.find_element_by_id("com.autonavi.minimap:id/btnStart") #进入
    el3.click()
    el4 = driver.find_element_by_id("com.autonavi.minimap:id/bt_terms_right") #同意
    el4.click()
    el5 = driver.find_element_by_id("com.autonavi.minimap:id/button1") #忽略
    el5.click()
except: 
    pass

driver.find_element_by_android_uiautomator('text(\"探索附近\")').click() #搜附近
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[5]/android.widget.ImageView")
el7.click() #更多
el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[8]/android.view.ViewGroup/android.widget.ImageView")
el8.click() #超市

swipeUp(driver, t=500, n=1)

driver.find_element_by_android_uiautomator('text(\"查找地点、公交、地铁\")').click()
driver.find_element_by_android_uiautomator('text(\"搜索\")').send_keys(u"超市")
sleep(10) #休眠10秒等待页面加载完成
driver.find_element_by_android_uiautomator('text(\"搜索\")').click()
swipeUp(driver, t=500, n=1)

driver.find_element_by_android_uiautomator('text(\"5000米\")').click() #5000
driver.find_element_by_android_uiautomator('text(\"全部范围\")').click() #范围
driver.find_element_by_android_uiautomator('text(\"全部分类\")').click() #分类
driver.find_element_by_android_uiautomator('text(\"超市\")').click() #超市
driver.find_element_by_android_uiautomator('text(\"推荐排序\")').click() 
driver.find_element_by_android_uiautomator('text(\"距离优先\")').click()

#数据提取
try:
    #数据提取
    i=[]
    j=[]
    element = driver.find_elements_by_class_name("android.widget.TextView") #android.widget.TextView
    for k in element:
        j.append(k.text)
    i.extend(j[4:-3]) 
    
    while True:
        swipe1(driver, t=500, n=1,d=0.33)
        j=[]
        element = driver.find_elements_by_class_name("android.widget.TextView") #android.widget.TextView
        for k in element:
            j.append(k.text)
        j1=j[4:-3]
        lej1=len(j1)
        lei=len(i)
        lag=0
        for k in range(lej1):
            if i[lei-k-3]==j1[0] and i[lei-k-2]==j1[1] and i[lei-k-1]==j1[2]:
                lag=1
                i=i[:lei-k-3]
                i.extend(j1)
                break
        if lag==0:
            for k in range(lej1):
                if i[lei-k-2]==j1[0] and i[lei-k-1]==j1[1]:
                    lag=1
                    i=i[:lei-k-2]
                    i.extend(j1)
                    break
        if lag==0:                        
            i.extend(j1)
        if j[-4]=="没有更多结果了":break
        else:continue
except: 
    pass

#输出
with open(r'E:\pytest\yuanmingyuan_beijingchasohi_14km.csv', 'w', newline='') as f:
    writer  = csv.writer(f)
    for row in i:
        writer.writerow([row])
