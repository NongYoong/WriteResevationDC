import requests
from bs4 import BeautifulSoup

#Login
url = 'https://dcid.dcinside.com/join/member_check.php'

soup = BeautifulSoup(requests.get("https://www.dcinside.com/").text, features='html.parser')
loginForm = soup.find('form', attrs={'id' : 'login_process'})
authKey = loginForm.find_all('input', attrs={'type' : 'hidden'})[2]

header = {
    'Referer': 'https://www.dcinside.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}

data = {
    's_url': '//www.dcinside.com/',
    'ssl': 'Y',
    authKey['name'] : authKey['value'],
    'user_id': 'hwangchimyong',
    'pw': 'A1vvays!!'
}

session = requests.session()

res = session.post(url,headers=header,data=data)
soup = BeautifulSoup(res.text, features='html.parser')
 
isLogined = False if soup.find('meta', attrs={'http-equiv':'refresh'}) == None else True 
if isLogined == True:
    print("Login succeed!")
else:
    print("Login failed")
    sys.exit(1)