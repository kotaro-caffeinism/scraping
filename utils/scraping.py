import pprint
import base64
import requests
from bs4 import BeautifulSoup

def scrape(): 

  url = "https://www.notion.so/ja-jp/help/guides"
  r = requests.get(url)

  soup = BeautifulSoup(r.content, "html.parser")
  # soup = BeautifulSoup(r.content, "html.parser")

  # headline = soup.h2.a.contents[0]
  # url = "https://www.notion.so" + soup.h2.a.attrs['href']

  # print(headline)
  # print(url)

  elms = soup.select("h2")
  # print(elms)

  notion_guide = []

  for elm in elms:

    headline = elm.a.contents[0]
    url = "https://www.notion.so" + elm.a.attrs['href']

    notion_guide.append({
      "headline": headline,
      "url": url,
    })
    
  elms2 = soup.find_all(class_= "subtitle")
  # print(elms2[0])

  for i in range(len(elms2)):

    subtitle = elms2[i]["title"]
    notion_guide[i]["text"] = subtitle

  # imgs = soup.find_all(class_= "thumbnail")

  # for i in range(len(imgs)):

  #   # img = "data:image/png;base64," + imgs[i].span.img["src"]
  #   img = imgs[i].span.img.get("src")
  #   notion_guide[i]["img"] = img

  # print(notion_guide[0]["img"])
  # https://www.notion.so/cdn-cgi/image/format=auto,width=1200,quality=100/https://images.ctfassets.net/spoqsaf9291f/OLBVmUUtVDV9UbCsemZc0/4f8ed5158e378ddaac560dcb3ce3066a/subtasks-dependencies.png

  # print("result: ")
  pprint.pprint(notion_guide)

  return notion_guide

