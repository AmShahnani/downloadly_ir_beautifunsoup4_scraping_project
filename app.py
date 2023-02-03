import requests
from bs4 import BeautifulSoup
import csv


# get response of Downloadly web page
# https://downloadly.ir/page/259/
BASE_URL = 'https://downloadly.ir/'

courses_title_dict = []

filename = 'courses.csv'
headers = ['title', 'link', 'image']


for i in range(1,5) :
    URL_TO_SCRAPE = "{BASE_URL}page/{p_no}/".format(BASE_URL=BASE_URL, p_no=i)

    print("Start Scraping URL :" + URL_TO_SCRAPE)

    r = requests.get(URL_TO_SCRAPE)
    soup = BeautifulSoup(r.text, 'html.parser')
    courses = soup.select('#us_grid_1 .align_right')

    

    for item in courses :
        row = {}
        title = item.a
        row['title'] = item.get_text()
        row['link'] = item.a['href']
        row['image'] = item.img['src']
        courses_title_dict.append(row)

    print("Finished Scraping URL : " + URL_TO_SCRAPE)


with open(filename, 'w', newline='', encoding="utf-8") as f:
    w = csv.DictWriter(f,headers)
    w.writeheader()
    for item in courses_title_dict :
            w.writerow(item)
