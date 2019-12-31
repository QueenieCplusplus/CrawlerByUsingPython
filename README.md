# CrawlerByUsingPython
使用 Python 爬蟲主題
_________________

HTML connection:

網路擷取必須深入網路連線的原理和介面，不僅僅受限於瀏覽器的層次。
當一台電腦與另一台伺服器交談時，會發生如下動作：

(1) 客戶端電腦發送一系列0和1，就是電壓起伏，這些電子訊號的位元構成了某種資訊，包含了 Header 和 Body，Header 還包含了本地 router 的 MAC 和伺服器端的 IP 位址。Body 則帶有向伺服器發出的 Request。

(2) 客戶端的 Local Gateway (a router) 接收這些0與1的電子訊號，並且被路由解釋成自己的 MAC 地址和伺服器的 IP 的 Packet，此封包會被本地路由加上路由自己的 IP 位址作為 from，並且發出至網際網路中。 

(3) 客戶端封包由實體線路穿越網路上伺服器到達目的地伺服器。

(4) 伺服器以自己具有的 IP 位址接收該封包。

(5) 伺服器讀取 Header 的 Port 號，並傳送給與之對應的 app，本案適用於網頁伺服器 Web Server App。（顯示方式： Port:80, 及其 IP 位址）

(6) 伺服器中的 Web Service App 接收伺服器收到並處理程序的資料流 Stream，資料流帶著訊息：

     HTTP method: GET
     
     Request Target: index.html

(7) 伺服器找出正確的 HTML 檔案，將它包裝成 Packet 透過本地路由以(1)-(5)步驟回到客戶端。

_________________

WWW & Browser

從 1990 年代起發明了瀏覽器，瀏覽器從而取代了 WWW。

瀏覽器建構了這些 Packet，告訴 OS 送出 Packet，將取得的資料解釋成為人類可以認知的格式的應用程式。
格式包含了圖像、聲音、文字、影片。其實瀏覽器就是程式碼，此程式碼能執行客戶端的請求，瀏覽器能要求處理器發送資料給無線或是有線介面的應用程式。

urllib 是 Python 標準函式庫，即無須額外安裝其他東西，內容從網路請求資料、處理 cookies 、 處理 header 和 user agent 等 metadata 功能。

urlopen 是其中一個打開跨網域的遠端物件並讀取。（可讀取 html 檔、影像檔案、其他檔案）

如下，說明了瀏覽器的程式碼運作內容

          from urllib.request import urlopen

          html = urlopen('https://github.com/QueenieCplusplus/CrawlerByUsingPython')
          print(html.read())
          
此程式執行後，會輸出 https://github.com 網域上的伺服器<web root>/UserID 目錄下的 CrawlerByUsingPython 這個網頁。
     
然而爬蟲時，最好是針對 Html 檔案，而非網頁。大部分網頁包含了很多格式的檔案，所以如果想取得網頁中的某檔案，可能是文字或是圖案亦或聲音檔案，例如這樣的標籤：

        <img src="cutePoupou.jpg">
        
因為 urlopen 功能只是打開網頁而已，即僅能讀取 html 檔案，如果要能取得檔案功能，則要使用能解析檔案的工具。

_________________

虛擬機安裝：

          $pip install virtualenv

          $virtualenv crawlEnv

          $cd crawlEnv/

啟動環境：

          $source bin/activate
          
離開環境：

          (crawlEnv)$deactivate
          
也可以選擇用 Anaconda 取代 pip:

          conda install -c conda-forge <module name>
_________________

Core Framework:

* Scrapy

      pip3 install scrapy
      
      create a dir, says QsSpider
      
      cd <dir>
      
      scrapy startproject Spider
      
     https://github.com/QueenieCplusplus/CrawlerByUsingPython/blob/master/QsSpider.Spider.png
      
     
Poject Structure

         spider
             *scrapy.cfg
             *sipder dir/
                     _init_.py
                     _pycache_ dir/
                     items.py
                     middlewares.py
                     pipelines.py
                     settings.py
                     *spiders dir/
                             _init.py
                             _pycache_dir/
  
Create New Class under spiders dir

https://github.com/QueenieCplusplus/CrawlerByUsingPython

         spider
             scrapy.cfg
             sipder dir/
                     _init_.py
                     _pycache_ dir/
                     items.py
                     middlewares.py
                     pipelines.py
                     settings.py
                     *spiders dir/
                            *ArticleSpider.py
                             _init.py
                             _pycache_dir/
                             
https://github.com/QueenieCplusplus/CrawlerByUsingPython

執行腳本>>>

      $cd <專案::目錄::腳本檔案所在目錄>
      
      $scrapy runspider article.py
 
_________________

Core Module:

* BeautifulSoup4 and its find() method

       sudo easy_install pip

       pip install --upgrade pip

       pip3 install beautifulsoup4
     
>>>   

       import bs4
       
       from bs4 import BeautifulSoup

* CAPTCHA

* NumPy

* Pillow

* Tesseract

Core API:

TBD

_________________

Code:

* single domain

https://github.com/QueenieCplusplus/CrawlerByUsingPython/blob/master/BeautifulSoup.py

* cross sites

_________________

Data Storage:

* CSV

* MySQL

* Mail

* PDF

* .docx

_________________

Data Cleansing:

* REX

* OpenRefine

_________________

Content:

Login

JS

_________________

Parallel

IP






