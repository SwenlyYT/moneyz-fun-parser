extended_arg = 0
from bs4 import BeautifulSoup as BS
import requests
from time import sleep
import json

while True:
	link = input('Ссылка: ')
	if 'moneyz.fun/' in link:
		key = link.split('moneyz.fun/')[1]
	else:
		key = link

	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
	}
	cookies = {
		"__cf_bm": "YYXeMub76RbkPQ1.723e.aHhMAXVgMosg9g4UavRKEM-1654092964-0-AQdIM1AvZJ9EKeti2BW3cb38ZiTzUFe/eBRFV5oN6KlK2ebEhpAtjME/xAoEPy3c496Lj3ofzIMmNjtYjOPAZAsbo71Vbf8kW3wkkbIboatxUhrdbtK1t+1H3sis5ikWmA==",
		"_client_id": "H3XEAYS5PZU4",
		"_ym_d": "1654092965",
		"_ym_isad": "1",
		"_ym_uid": "1648758768136258494",
		"_ym_visorc": "b",
		"allow_click_usual_link": "1"
	}
	data = {
		'click_link_key': key
	}

	r = requests.post(f'https://moneyz.fun/action.php', data=data, cookies=cookies, headers=HEADERS)
	soup = BS(r.content, 'html.parser')

	json_object = json.loads(r.text)

	print(json_object['link_full_val'])
