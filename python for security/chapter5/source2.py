import urllib2
url = "http://localhost/test/python.php"
headers = {}
headers['User-Agent'] = "Googlebot"
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
print response.read()
response.close()
