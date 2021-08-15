import requests 
# 導入 BeautifulSoup 模組(module)：解析HTML 語法工具
import bs4
import datetime
import time
import json




#while(1):
    #now_time = datetime.datetime.now().strftime('%H:%M:%S')
    #time.sleep(1)
    #print(now_time)

def get_one_page(URL):
    '''
    程式碼解說詳細請看：
    https://medium.com/p/a8216873a9d3
    '''
    
    # 設定Header與Cookie
    my_headers = {'cookie': 'over18=1;'}
    # 發送get 請求 到 ptt 八卦版
    response = requests.get(URL, headers = my_headers)
    
    
    # 2-1 把網頁程式碼(HTML) 丟入 bs4模組分析
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    
    # 2-2 查找所有html 元素 過濾出 標籤名稱為 'div' 同時class為 title 
    titles = soup.find_all('div','title')
    
    # 2-3 萃取文字出來。
    # 因為我們有多個Tags存放在 List titles中。
    # 所以需要使用for 迴圈將逐筆將List 
    for t in titles:

        with open('setting.json',mode='r',encoding='utf8') as jfile:
            jdata=json.load(jfile)
        jdata['URL'] = "https://www.ptt.cc"+t.a.get("href")
        #time.sleep(0.1)
        with open('setting.json',mode='w',encoding='utf8') as jfile:
            jdata=json.dump(jdata, jfile, indent = 4)
        print(t.text.strip())  #strip 是把空白去掉的意思。
        print("https://www.ptt.cc"+t.a.get("href"))
        

# 組成 正確 URL
link = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 執行單頁面網頁爬蟲
get_one_page(link)
# 避免被太快被 PTT 封鎖請求
    
        
        

    

