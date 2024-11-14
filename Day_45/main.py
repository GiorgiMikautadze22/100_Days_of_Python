from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soap = BeautifulSoup(data, "html.parser")
titles = [title.getText() for title in soap.find_all(name="h3", class_="title")]
titles.reverse()

with open("movies.txt", mode="w",encoding="utf-8") as file:
    for title in titles:
        file.write(f"{title}\n")
