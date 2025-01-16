import requests

from bs4 import BeautifulSoup

# url='https://aimicrodegree.org/'
# url='https://www.cricbuzz.com/'
url='https://www.amazon.in/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2'
res=requests.get(url)
soup=BeautifulSoup(res.content,'html.parser')

title=soup.title.text
body=soup.body.text


print (title)
print(body)

