#use urllib post data
from urllib import request,parse
url = 'http://www.someserver.com/register.cgi'
headers = {
    'name' : 'WHY',
    'location' : 'SDU',
    'language' : 'Python'
}

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'Python'
}

data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data)
page = request.urlopen(req).read()
page = page.decode('utf-8')

