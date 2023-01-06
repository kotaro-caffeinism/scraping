import pprint
import requests
from bs4 import BeautifulSoup

def scrape(): 

  url = "https://www.notion.so/ja-jp/help/guides"
  r = requests.get(url)

  soup = BeautifulSoup(r.content, "html.parser")

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
    
  elms2 = soup.find_all(class_="subtitle")
  # print(elms2[0])

  for i in range(len(elms2)):

    # print(elms2[i])
    subtitle = elms2[i]["title"]
    # print(subtitle)

    # subtitle2 = elms2[i].span.contents[0]
    # print(subtitle2 + "\n")


    notion_guide[i]["text"] = subtitle


  # print(notion_guide[0])
  # print("result: ")
  # pprint.pprint(notion_guide)

  return notion_guide

