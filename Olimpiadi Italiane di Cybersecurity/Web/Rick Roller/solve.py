import requests

print(requests.get('http://roller.challs.olicyber.it/get_flag.php', allow_redirects=False).text)