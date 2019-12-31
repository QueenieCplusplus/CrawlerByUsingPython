# CrawlerByUsingPython
使用 Python 爬蟲主題

To Be Done...

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

如下，說明了瀏覽器的程式碼運作內容

          from urllib.request import urlopen

          html = urlopen('https://github.com/QueenieCplusplus/CrawlerByUsingPython')
          print(html.read())
          
此程式執行後，會輸出 https://github.com 網域上的伺服器<web root>/UserID 目錄下的 CrawlerByUsingPython 頁面這 html 檔案。

_________________

Core Module:

* BeautifulSoup and its find() method

* Scrapy

* CAPTCHA

* NumPy

* Pillow

* Tesseract

Core API:

TBD

_________________

Code:

* single domain

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






