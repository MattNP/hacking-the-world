import requests

page = requests.get('http://www.thisislegal.com/includes/randCode.php')
code = page.text[39:48]
address = 'http://www.thisislegal.com/challenge/programming/1/'
url = address + code
cookies = dict(PHPSESSID='li807a7gq6lnuei80ere4ma3r7')
r = requests.get(url, cookies=cookies)
