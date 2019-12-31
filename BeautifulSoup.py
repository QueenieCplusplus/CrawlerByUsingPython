Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import bs4
>>> from bs4 import BeautifulSoup
>>> 
from urllib.request import urlopen
>>> 
>>> html = urlopen('http://www.pythonscraping.com/pages/page1.html')
b
>>> bs = BeautifulSoup(html.read(), 'html.parser')
>>> print(bs.h1)
<h1>An Interesting Title</h1>
>>> 
