import urllib.request

request_url = "http://www.baidu.com"
response = urllib.request.urlopen(request_url)
print(response.read().decode('utf-8'))
print(response.info().decode('utf-8'))
# print(response.geturl(),response.getcode())