#use urllib fetch baidu content
import urllib.request
from urllib import parse
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read();
print(html)

