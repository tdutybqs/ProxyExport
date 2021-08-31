import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
url = "https://hidemy.name/ru/proxy-list/"

headers = CaseInsensitiveDict()
headers["Host"] = "hidemy.name"
headers["cache-control"] = "max-age=0"
headers["sec-ch-ua"] = '''""Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92""'''
headers["sec-ch-ua-mobile"] = "?0"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["sec-fetch-site"] = "none"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-user"] = "?1"
headers["sec-fetch-dest"] = "document"
headers["accept-language"] = "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"


resp = requests.get(url, headers=headers).text
parsed_html = BeautifulSoup(resp, "html.parser")
list_tr = list(parsed_html.find_all("td"))
temp_str = ""
for elemIndex in range(7, len(list_tr), 7):
    temp_str += f"'{list_tr[elemIndex+4].getText()}':'{list_tr[elemIndex].getText()}:{list_tr[elemIndex+1].getText()}',\n"
file = open("text.txt", "a+")
file.write(temp_str[:-2])
file.close()

