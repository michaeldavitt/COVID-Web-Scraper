import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"


def scrape():
    web_site = requests.get(URL)
    soup = BeautifulSoup(web_site.text, "lxml")
    data_wrap = soup.find_all("div", id="maincounter-wrap")
    data_list = []
    for wrap in data_wrap:
        data = wrap.find("div", class_="maincounter-number")
        data = int(data.text.replace(",", ""))
        data_list.append(data)
    return data_list


if __name__ == "__main__":
    scrape()
