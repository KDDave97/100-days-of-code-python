from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_titles = soup.find_all(class_="titleline")
scores = soup.find_all(class_="score")

article_score = []
article_title = []
article_links = []

for article in article_titles:
    article_title.append(article.find(name="a").getText())
    article_links.append(article.find(name="a").get("href"))

for score in scores:
    article_score.append(int(score.getText().split()[0]))

highest_score_index = article_score.index(max(article_score))

print(f"{article_score[highest_score_index]} points: {article_title[highest_score_index]}\n"
      f"{article_links[highest_score_index]}")