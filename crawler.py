#(1, 12345, 'Name', 'Loc', 'Dep', 'Abb', 'Des', 'Req', 'Prf')

import requests
import re
from bs4 import BeautifulSoup
import dbconnect

def get_page(id):
	id = str(id)
	url = "https://www.amazon.jobs/en/jobs/"+id
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "html.parser")
        
	id = name = loc = dep = abb = des = req = prf = ""
	item = [id, name, loc, dep, abb, des, req, prf]
	soup.find("div", {"id": "job-detail-body"})
	drp = soup.findAll(class_='section')

	if drp:
		des = drp[0].find('p')
		req = drp[1].find('p')
		prf = drp[2].find('p')

	lda = soup.findAll(class_='association-content')

	if lda:

		if len(lda) == 2:
			loc = lda[0].find('a') or lda[0].find('p')
			dep = None
			abb = lda[1].find('a') or lda[1].find('p')
		elif len(lda) == 3:
			loc = lda[0].find('a') or lda[0].find('p')
			dep = lda[1].find('a') or lda[1].find('p')
			abb = lda[2].find('a') or lda[2].find('p')

	name = soup.find(class_='title')
	id = re.findall('\d+', str(soup.find('title')))

	if id:
		item[0] = id[0]
		ord = [name, loc, dep, abb, des, req, prf]
		for i in range(1,8):
			if ord[i-1]:
				item[i] = ord[i-1].text

	return item if id else None


def crawing(start, stop, loc, kw):
	cnt = 0
	start, stop = max(start, stop), min(start, stop)
	for id in range(start, stop, -1):
		item = get_page(id)
		if item:
			if loc in item[2] and kw in item[4]:
				cnt += 1
				print(f"The {cnt} Post Recorded, job title is {item[1]}")
				dbconnect.insert_item(tuple(item))
			else:
				print(f"Invalid post, job is at {item[2]} and job title is {item[1]} ")

def fetching(query):
	dbconnect.read(query)



if __name__ == "__main__":

	crawing(1243000, 1243200, "Washington", "Software")

	'''
	fetching("SELECT JOB_ID, REQ, PRF FROM amazonjb \
		  WHERE REQ LIKE '%AWS%' \
		  OR PRF LIKE '%AWS%' \
		  LIMIT 25")
		  '''
		  
	
