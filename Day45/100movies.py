from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movies_text = ""

for movie in movies[::-1]:
    movies_text += f"{movie.getText()}\n"

print(movies_text)

with open("movies.txt", mode="w") as file:
     file.write(movies_text)