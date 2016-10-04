from urllib.request import urlopen

url = 'http://spaceweather.rra.go.kr/api/kindex'

response = urlopen(url)
print(response.read().decode('utf-8'))
