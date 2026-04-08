import requests
from bs4 import BeautifulSoup
import json

gainers_list = []

url = "https://api.bseindia.com/BseIndiaAPI/api/MktRGainerLoserDataeqto/w?GLtype=gainer&IndxGrp=group&IndxGrpval=A&orderby=all"

payload = {}
headers = {
  'path': '/BseIndiaAPI/api/MktRGainerLoserDataeqto/w?GLtype=gainer&IndxGrp=group&IndxGrpval=A&orderby=all',
  'scheme': 'https',
  'authority': 'api.bseindia.com',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
  'referer': 'https://www.bseindia.com/'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

with open(f'data\\raw_gainers.json', 'w') as file:
    file.write(response.text)