from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import date

global today
today = date.today()

def main2():
    myurl = "https://gamesite.zoznam.sk/"
    uClient = uReq(myurl)
    page_html = uClient.read()

    uClient.close()

    page_soup = soup(page_html, 'html.parser')

    titles = page_soup.find_all(class_ = "uk-article-title")
    dates = page_soup.find_all('time')
    i = 0

    titles_list = []
    dates_list = []


    d1 = today.strftime("%d. %m. %Y")

    for item in titles:
        date = dates[i].get_text()
        title = item.get_text()
        if date == d1:
            dates_list.append(date)
            titles_list.append(title)
        i += 1
    len_of_l = len(titles_list)
    return titles_list, dates_list, len_of_l
